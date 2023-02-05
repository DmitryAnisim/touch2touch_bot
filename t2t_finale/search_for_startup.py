from bot_settings import dp
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_settings import bot
from config import database_names
from keyboards import search_kb, search_text_all
from sql_bases.sql import sql_get_random_inv_start, sql_get_all_user_data
from make_an_asset import make_an_asset


@dp.message_handler(state=UserData.search_for_startup)
async def selection(message: types.Message, state: FSMContext):
    await message.answer("Посмотрите анкеты других людей и оцените, тех кто больше для Вас подходит", reply_markup=search_kb)
    other_user_ids = sql_get_random_inv_start(database_names)
    counter = int(sql_get_all_user_data(message.from_user.id, database_names)['counter'])
    print(counter)
    try:
        single_asset_id = other_user_ids[counter]
        asset, photo = make_an_asset(single_asset_id, database_names)
        state.update_data(like_id = asset["user_id"])
        await bot.send_photo(message.from_user.id, photo, asset)
        await UserData.assets_for_algorithm.set()
    except IndexError:
        await message.answer('Недостаточно анкет для поиска, подождите регистрации других пользователей и нажмите на кнопку ещё раз')
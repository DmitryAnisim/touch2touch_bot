from bot_settings import dp
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_settings import bot
from keyboards import search_kb, search_text_all
from sql_bases.sql_for_relationship import sql_find_right_sex
from sql_bases.sql import sql_get_all_user_data
from config import database_names
from make_an_asset import make_an_asset


@dp.message_handler(state=UserData.search_for_relationship)
async def selection(message: types.Message, state: FSMContext):
    await message.answer("Посмотрите анкеты других людей и оцените, тех кто больше для Вас подходит", reply_markup=search_kb)
    """Вывод анкеты должен быть здесь, если парень то выводится девушка, если девушка, то выводится парень"""
    user_id = message.from_user.id
    try:
        data = await state.get_data()
        sex = data['sex']
    except KeyError:
        data = sql_get_all_user_data(user_id,database_names)
        sex = data['sex']
    other_user_sex = sql_find_right_sex(sex)
    counter = int(sql_get_all_user_data(message.from_user.id,database_names)['counter'])
    try:
        if other_user_sex is None:
            raise IndexError
        single_asset_id = other_user_sex[counter]
        asset, photo = make_an_asset(single_asset_id, database_names)
        state.update_data(like_id = asset["user_id"])

        
        await bot.send_photo(message.from_user.id, photo, asset)
        await UserData.assets_for_algorithm.set()
    except IndexError:
        await message.answer('Недостаточно анкет для поиска, подождите регистрации других пользователей и нажмите на кнопку ещё раз',reply_markup=search_kb)


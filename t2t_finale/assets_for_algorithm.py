from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from make_an_asset import make_an_asset
from config import database_names
from bot_settings import bot
from sql_bases.sql_for_relationship import sql_add_user_likes
from sql_bases.sql_for_investment import *
from sql_bases.sql import sql_get_all_user_data, sql_find_user_database


@dp.message_handler(state = UserData.assets_for_algorithm)
async def assets_for_algorithm(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    try:
        data = await state.get_data()
        if data == {}:
            raise TypeError
        database = data['database']
        my_like = data['like_id']
    except TypeError:
        data = sql_get_all_user_data(user_id, database_names)
        database = sql_find_user_database(message.from_user.id)
        my_like = data['user_likes']
    if message.text == "👍":
        sql_add_user_likes(user_id, my_like)
        counter = sql_get_all_user_data(user_id, database_names)['counter']
        if counter >= 5:
            await message.answer('Находим пару...')
            await UserData.search_pair.set()
        else:
            if database == 'relationship_db.db':
                await UserData.search_for_relationship.set()
            elif database == 'investment_db.db':
                await UserData.search_for_investment.set()
            else:
                await UserData.search_for_startup.set()
    if message.text == "👎":
        if database == 'relationship_db.db':
            await UserData.search_for_relationship.set()
        elif database == 'investment_db.db':
            await UserData.search_for_investment.set()
        else:
            await UserData.search_for_startup.set()
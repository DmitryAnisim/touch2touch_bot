from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from sql_bases.sql import sql_get_all_user_likes, sql_get_all_user_data
from config import database_names
from make_an_asset import make_an_asset
from keyboards import kb_check_pair


@dp.message_handler(state = UserData.search_pair.set())
async def search_pair(message: types.Message, state: FSMContext):
    main_user_id = message.from_user.id
    main_user_likes = sql_get_all_user_likes(main_user_id, database_names)
    for other_user_id in main_user_likes:
        if main_user_id in sql_get_all_user_likes(other_user_id,database_names):
            asset = make_an_asset(other_user_id, database_names)
            await message.answer(asset)
            break
    else:
        message.answer('Пока что мы не нашли вам пару',reply_markup = kb_check_pair)
        

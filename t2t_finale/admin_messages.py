from bot_settings import *
from config import admins_ids
from aiogram import types
from sql_bases.sql import sql_get_all_user_ids

@dp.message_handler(commands=['рассылка'], state = None)
async def sendall(message: types.Message):

    if message.from_user.id in admins_ids:
        text = message.text[10:]
        menu = sql_get_all_user_ids()
        for user_id in menu:
            await bot.send_message(user_id, text)

@dp.message_handler(commands=['фоторассылка'], state = None)
async def sendallphoto(message: types.Message):

    if message.from_user.id in admins_ids:
        text = message.text [14:]
        photo = message.photo[-1].file_id
        menu = sql_get_all_user_ids()
        for user_id in menu:
            await bot.send_photo(user_id, photo, text)
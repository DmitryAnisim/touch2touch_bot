from aiogram import types
from UserDataClass import UserData
from keyboards import kb_register, search_kb
from bot_settings import dp, bot
from sql_bases.sql import sql_get_all_user_ids
from sql_bases.sql_for_startup import sql_startup
from sql_bases.sql_for_investment import sql_investment
from sql_bases.sql_for_relationship import sql_relationship
from sql_bases.sql_ofline_networking import sql_networking
from sql_bases.sql_for_tracking import sql_zero_complete
from config import database_names, admins_ids


def on_startup():
    print("Бот вышел в онлайн")
    sql_investment()
    sql_startup()
    sql_relationship()
    sql_networking()

@dp.message_handler(commands=['start', 'старт', 'help'], state=None)
async def command_start(message: types.Message):
    await message.answer('👋Привет, это умный помощник Touch2Touch!\n1️⃣ Создай профиль\n2️⃣ Дойди до 5 лайков\n3️⃣ Проведи встречу')
    try:
        all_ids = sql_get_all_user_ids(database_names).to_dict('records')
        all_ids = set([i['user_id'] for i in all_ids])
    except AttributeError:
        all_ids = []
    print(all_ids)
    if message.from_user.id in all_ids:
        await message.answer('Анкеты',reply_markup=search_kb)
        await UserData.assets_for_algorithm.set()
    else:
        await message.answer('💬Давайте пройдем короткий опрос', reply_markup = kb_register)
        # username = message.from_user.username
        # await sql_zero_complete(username)
        await UserData.register.set()


@dp.message_handler(commands=['рассылка'], state = None)
async def sendall(message: types.Message):

    if message.from_user.id in admins_ids:
        text = message.text[10:]
        menu = sql_get_all_user_ids(database_names)
        menu = menu.to_dict()
        menu = [i for i in menu.values()][0]
        menu = [i for i in menu.values()]
        for user_id in menu:
            await bot.send_message(user_id, text)

@dp.message_handler(commands=['photosend'], state = None)
async def sendallphoto(message: types.Message):

    if message.from_user.id in admins_ids:
        text = message.text[12:]
        photo = message.photo[-1].file_id
        menu = sql_get_all_user_ids(database_names)
        menu = menu.to_dict()
        menu = [i for i in menu.values()][0]
        menu = [i for i in menu.values()]
        print(menu)
        for user_id in menu:
            await bot.send_photo(user_id, photo, text)

@dp.message_handler(state = None)
async def wrong_command(message: types.Message):
    await message.answer('Введите команду /start, /старт или /help')

    

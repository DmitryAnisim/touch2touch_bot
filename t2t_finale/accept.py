from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_settings import bot 
from keyboards import accept_all, kb_accept, accept_b1_text, accept_b2_text, kb_register,kb_next_step
from sql_bases.sql_for_investment import sql_add_investment
from sql_bases.sql_for_relationship import sql_add_relationship
from sql_bases.sql_for_startup import sql_add_startup
from utility.get_user_profile_photo import get_user_profile_photo


@dp.message_handler(lambda message: message.text in accept_all, state = UserData.accept)
async def accept(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        database_path = data['database']

    data = await state.get_data()
    photo = await bot.get_user_profile_photos(message.from_user.id)
    data.update({'user_id': message.from_user.id, "username": message.from_user.username, 'photo': get_user_profile_photo(photo), 'user_likes': ' ', 'counter': 0})
    data.pop("database")
    if message.text == accept_b1_text:
        if database_path == "relationship_db.db":
            await sql_add_relationship(data)
            await message.answer('Вы зарегистрированы',reply_markup=kb_next_step)
            await UserData.search_for_relationship.set()
        if database_path == "investment_db.db":
            await sql_add_investment(data)
            await message.answer('Вы зарегистрированы',reply_markup=kb_next_step)
            await UserData.search_for_investment.set()
        if database_path == "startup_db.db":
            print(data)
            await sql_add_startup(data)
            await message.answer('Вы зарегистрированы',reply_markup=kb_next_step)
            await UserData.search_for_startup.set()
    if message.text == accept_b2_text:
        await message.answer('Давайте пройдем анкету заново',reply_markup=kb_register)
        await state.finish()
        await UserData.register.set()


@dp.message_handler(state = UserData.accept)
async def wrong_accept(message: types.Message):
    
    await message.answer('Выберите из предложенных вариантов', reply_markup=kb_accept)
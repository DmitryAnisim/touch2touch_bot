from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import register_b1_text, register_b2_text, register_b3_text, kb_employment, register_all, kb_sex, kb_investment


@dp.message_handler(lambda message: message.text in register_all, state = UserData.register)
async def register(message: types.Message, state: FSMContext):
    await message.answer("Какая ваша роль?")
    
    if message.text == register_b1_text:
        await state.update_data(database = "relationship_db.db")
        await message.answer('Выберите ваш пол', reply_markup = kb_sex)
        await UserData.sex.set()
        
    if message.text == register_b2_text:
        await state.update_data(database="startup_db.db")
        await message.answer('Из какой вы сферы?', reply_markup = kb_investment)
        await UserData.employment.set()

    if message.text == register_b3_text:
        await state.update_data(database="investment_db.db")
        await message.answer('В проекты из какой сферы вы инвестируете?', reply_markup = kb_investment)
        await UserData.investments.set()


@dp.message_handler(state = UserData.register)
async def wrong_register(message: types.Message):
    await message.answer('Выберите из предложенных вариантов')
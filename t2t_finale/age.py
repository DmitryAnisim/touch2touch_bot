from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(regexp = '[0-9]{1,2}', state = UserData.age)
async def age(message: types.Message, state: FSMContext):
    await state.update_data(age = message.text)
    await message.answer('Введите информацию о себе')
    await UserData.about_myself.set()

@dp.message_handler(state = UserData.age)
async def wrong_age(message: types.Message):
    await message.answer('Введите корректный возраст')


from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import sex_all
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(lambda message: message.text in sex_all, state = UserData.sex)
async def sex(message: types.Message, state: FSMContext):
    await state.update_data(sex = message.text)
    await message.answer('Введите возраст', reply_markup=ReplyKeyboardRemove())
    await UserData.age.set()

@dp.message_handler(state = UserData.sex)
async def wrong_sex(message: types.Message):
    await message.answer('Выберите из предложенных вариантов')

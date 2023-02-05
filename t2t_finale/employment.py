from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import *
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(lambda message: message.text in employment_all, state=UserData.employment)
async def employment(message: types.Message, state: FSMContext):
    if message.text in employment_all:
        await state.update_data(employment=message.text)
        await message.answer('Выберите Вашу направленность из предложенных вариантов', reply_markup=ReplyKeyboardRemove())
        if message.text == "Бизнес":
            await message.answer("Выберите один из вариантов", reply_markup=kb_business)
        if message.text == "IT-сфера":
            await message.answer("Выберите один из вариантов", reply_markup=kb_it)
        if message.text == "Маркетинг":
            await message.answer("Выберите один из вариантов", reply_markup=kb_marketing)
        if message.text == "Наука и образование":
            await message.answer("Выберите один из вариантов", reply_markup=kb_science)
        if message.text == "Творчество":
            await message.answer("Выберите один из вариантов", reply_markup=kb_art)
        await UserData.job.set()


@dp.message_handler(state = UserData.employment)
async def wrong_employment(message: types.Message):
    await message.answer('Выберите из предложенных вариантов',reply_markup=kb_employment)
from bot_settings import dp
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import kb_skip


@dp.message_handler(state=UserData.job)
async def load_job(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer("Расскажите о себе подробнее", reply_markup=kb_skip)
    await UserData.problem.set()

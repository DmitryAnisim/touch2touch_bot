from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import kb_skip, kb_next_step, employment_all
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(lambda message: message.text in kb_skip, state = UserData.problem)
async def skip_problem(message: types.Message,state: FSMContext):
    await state.update_data(problem = message.text)
    await message.answer('👍',reply_markup = kb_next_step)
    await UserData.asset.set()

@dp.message_handler(state = UserData.problem)
async def problem(message: types.Message, state: FSMContext):
    await state.update_data(problem = message.text)
    await message.answer('👍',reply_markup = kb_next_step)
    await UserData.asset.set()
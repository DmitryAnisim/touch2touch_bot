from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import kb_next_step

@dp.message_handler(state = UserData.about_myself)
async def about_myself(message: types.Message, state: FSMContext):
    await state.update_data(about_myself = message.text)
    await message.answer('👍',reply_markup=kb_next_step)
    await UserData.asset.set()
from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import investment_all, kb_investment, kb_next_step, kb_skip

@dp.message_handler(lambda message: message.text in investment_all, state = UserData.investments)
async def investments(message: types.Message, state: FSMContext):
    await state.update_data(investments = message.text)
    await message.answer('👍',reply_markup=kb_next_step)
    await UserData.asset.set()

@dp.message_handler(state = UserData.investments)
async def wrong_investments(message: types.Message):
    await message.answer('Выберите из предложенных вариантов')


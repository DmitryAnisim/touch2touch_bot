from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from captchas.captchas import delete_all_captchas

@dp.message_handler(state = UserData.captcha_confirm)
async def captcha_confirm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        key = data['key']
    delete_all_captchas()
    if message.text == key:
        await message.answer('Капча пройдена')
        await UserData.asset.set()
    else:
        await message.answer('Капча пройдена')
        await UserData.pre_asset.set()

    
from bot_settings import dp
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_settings import bot 
from captchas.captchas import generate_captcha


@dp.message_handler(state = UserData.pre_asset)
async def pre_asset(message: types.Message, state: FSMContext):
    key,path = generate_captcha(message.from_user.id)
    await state.update_data(key = key)
    await bot.send_photo(message.from_user.id, photo = open(path,'rb'))
    await UserData.captcha_confirm.set()
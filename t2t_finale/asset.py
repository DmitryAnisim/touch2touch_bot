from bot_settings import dp 
from UserDataClass import UserData
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot_settings import bot 
from utility.get_user_profile_photo import get_user_profile_photo
from keyboards import kb_accept

@dp.message_handler(state = UserData.asset)
async def asset(message: types.Message, state: FSMContext):
    await message.answer('Вот ваша анкета')
    data = await state.get_data()
    photo = await bot.get_user_profile_photos(message.from_user.id)
    photo = get_user_profile_photo(photo)
    data.update({'user_id': message.from_user.id, 'username': message.from_user.username, 'photo': photo})
    print(data)
    asset = "\n".join([str(i) for i in data.values()])
    if data['database'] == 'relationship_db.db':

        await bot.send_photo(message.from_user.id, data["photo"], f'@{data["username"]}, {data["age"]}\n\n\
О себе: {data["about_myself"]}')
    if data['database'] == 'startup_db.db':

        await bot.send_photo(message.from_user.id, data["photo"], f'@{data["username"]}\n\n\
Сфера деятельности: {data["employment"]}\n\nНаправленность: {data["job"]}\n\nО себе: {data["problem"]}')
    if data["database"] == 'investment_db.db':

        await bot.send_photo(message.from_user.id, data["photo"], f'@{data["username"]}\n\nКуда инвестирую: {data["investments"]}\n')
    await message.answer('Подтвердите вашу анкету', reply_markup=kb_accept)
    await UserData.accept.set()
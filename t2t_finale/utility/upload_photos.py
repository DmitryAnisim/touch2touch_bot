from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor
from aiogram import types


async def on_startup(_):
    print('ready to get photos')

main_bot_api = '5519749341:AAGQvvX22Fwk-af2bZueYJmVzqiAxRVre7E'
storage = MemoryStorage()
bot = Bot(main_bot_api)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(content_types = ['photo'], state=None)
async def command_start(message: types.Message):
    print(message.photo[0].file_id)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
from config import main_bot_api, test_bot_api, test2_bot_api
from UserDataClass import UserData


storage = MemoryStorage()
bot = Bot(main_bot_api)
dp = Dispatcher(bot, storage=storage)


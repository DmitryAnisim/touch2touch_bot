from start import *
from register import *
from age import *
from about_myself import *
from employment import *
from problem import *
from investments import *
from asset import *
from sex import *
from pre_asset import *
from captcha_confirm import *
from accept import *
from job import *
from assets_for_algorithm import *
from search_for_investment import *
from search_for_relationship import *
from search_for_startup import *
from search_pair import *
from bot_settings import dp
from aiogram import executor



executor.start_polling(dp, skip_updates=True, on_startup=on_startup())



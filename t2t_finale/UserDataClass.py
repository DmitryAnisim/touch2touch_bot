from aiogram.dispatcher.filters.state import State, StatesGroup

class UserData(StatesGroup):
    start = State()
    menu = State()
    register = State()
    age = State()
    about_myself = State()
    employment = State()
    job = State()
    problem = State()
    investments = State()
    pre_asset = State()
    captcha_confirm = State()
    asset = State()
    sex = State()
    accept = State()
    assets_for_algorithm = State()
    search_for_relationship = State()
    search_for_investment = State()
    search_for_startup = State()
    search_pair = State()

    
    
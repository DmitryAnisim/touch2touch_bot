from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


register_b1_text = "Парень/Девушка (ищу новые знакомства)"
register_b2_text = "Специалист/Предприниматель"
register_b3_text = "Эксперт/Инвестор"
register_all = [register_b1_text, register_b2_text, register_b3_text]
register_b1 = KeyboardButton(register_b1_text)
register_b2 = KeyboardButton(register_b2_text)
register_b3 = KeyboardButton(register_b3_text)
kb_register = ReplyKeyboardMarkup(resize_keyboard=True)
kb_register.row(register_b1, register_b2, register_b3)



employment_b1_text = 'Бизнес'
employment_b2_text = 'IT-сфера'
employment_b3_text = "Маркетинг"
employment_b4_text = "Наука и образование"
employment_b5_text = "Творчество"
employment_b6_text = "Учусь"
employment_all = [employment_b1_text, employment_b2_text, employment_b3_text, employment_b4_text, employment_b5_text, employment_b6_text]
employment_b1 = KeyboardButton(employment_b1_text)
employment_b2 = KeyboardButton(employment_b2_text)
employment_b3 = KeyboardButton(employment_b3_text)
employment_b4 = KeyboardButton(employment_b4_text)
employment_b5 = KeyboardButton(employment_b5_text)
employment_b6 = KeyboardButton(employment_b6_text)
kb_employment = ReplyKeyboardMarkup(resize_keyboard=True)
kb_employment.row(employment_b1,employment_b2,employment_b3).row(employment_b4, employment_b5,employment_b6)

investment_b1_text = 'Бизнес'
investment_b2_text = 'IT-сфера'
investment_b3_text = "Маркетинг"
investment_b4_text = "Наука и образование"
investment_b5_text = "Творчество"
investment_all = [investment_b1_text, investment_b2_text, investment_b3_text, investment_b4_text, investment_b5_text]
investment_b1 = KeyboardButton(investment_b1_text)
investment_b2 = KeyboardButton(investment_b2_text)
investment_b3 = KeyboardButton(investment_b3_text)
investment_b4 = KeyboardButton(investment_b4_text)
investment_b5 = KeyboardButton(investment_b5_text)
kb_investment = ReplyKeyboardMarkup(resize_keyboard=True)
kb_investment.row(investment_b1,investment_b2,investment_b3).row(investment_b4, investment_b5)


skip_b1_text = 'Пропустить'
skip_all = [skip_b1_text]
skip_b1 = KeyboardButton(skip_b1_text)
kb_skip = ReplyKeyboardMarkup(resize_keyboard=True)
kb_skip.row(skip_b1)



sex_b1_text = 'Мужчина'
sex_b2_text = 'Женщина'
sex_all = [sex_b1_text,sex_b2_text]
kb_sex = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sex.row(sex_b1_text, sex_b2_text)


accept_b1_text = 'Подтверждаю'
accept_b2_text = 'Не подтверждаю'
accept_all = [accept_b1_text, accept_b2_text]
kb_accept = ReplyKeyboardMarkup(resize_keyboard=True)
kb_accept.row(accept_b1_text,accept_b2_text)


next_step_b1_text = 'Следующий шаг'
next_step_all = ['Следующий шаг']
kb_next_step = ReplyKeyboardMarkup(resize_keyboard=True)
kb_next_step.row(next_step_b1_text)

"""Клавиатура бизнес"""
business_text_b1 = "Стартап"
business_text_b2 = "Производство"
business_text_b3 = "Франшиза"
business_text_b4 = "Торговля"
business_text_b5 = "Посредничество"
business_all = [business_text_b1, business_text_b2, business_text_b3, business_text_b4, business_text_b5]
business_b1 = KeyboardButton(business_text_b1)
business_b2 = KeyboardButton(business_text_b2)
business_b3 = KeyboardButton(business_text_b3)
business_b4 = KeyboardButton(business_text_b4)
business_b5 = KeyboardButton(business_text_b5)
kb_business = ReplyKeyboardMarkup(resize_keyboard=True)
kb_business.row(business_b1, business_b2, business_b3).row(business_b4, business_b5)

"""Клавиатура IT"""
it_text_b1 = "Сисадмин"
it_text_b2 = "Frontend"
it_text_b3 = "Backend"
it_text_b4 = "Аналитик"
it_text_b5 = "Тестировщик"
it_all = [it_text_b1, it_text_b2, it_text_b3, it_text_b4, it_text_b5]
it_b1 = KeyboardButton(it_text_b1)
it_b2 = KeyboardButton(it_text_b2)
it_b3 = KeyboardButton(it_text_b3)
it_b4 = KeyboardButton(it_text_b4)
it_b5 = KeyboardButton(it_text_b5)
kb_it = ReplyKeyboardMarkup(resize_keyboard=True)
kb_it.row(it_b1, it_b2, it_b3).row(it_b4, it_b5)

"""Клавиатура Маркетинг"""
marketing_text_b1 = "PR-менеджер"
marketing_text_b2 = "Контент-маркетолог"
marketing_text_b3 = "Digital-маркетолог"
marketing_text_b4 = "Аналитик"
marketing_all = [marketing_text_b1, marketing_text_b2, marketing_text_b3, marketing_text_b4]
marketing_b1 = KeyboardButton(marketing_text_b1)
marketing_b2 = KeyboardButton(marketing_text_b2)
marketing_b3 = KeyboardButton(marketing_text_b3)
marketing_b4 = KeyboardButton(marketing_text_b4)
kb_marketing = ReplyKeyboardMarkup(resize_keyboard=True)
kb_marketing.row(marketing_b1, marketing_b2).row(marketing_b3, marketing_b4)

"""Клавиатура Наука и образование"""
science_text_b1 = "Преподаватель"
science_text_b2 = "Учёный"
science_text_b3 = "Ed-tech"
science_text_b4 = "Техническая сфера"
science_text_b5 = "Гуманитарная сфера"
science_all = [science_text_b1, science_text_b2, science_text_b3, science_text_b4, science_text_b5]
science_b1 = KeyboardButton(science_text_b1)
science_b2 = KeyboardButton(science_text_b2)
science_b3 = KeyboardButton(science_text_b3)
science_b4 = KeyboardButton(science_text_b4)
science_b5 = KeyboardButton(science_text_b5)
kb_science = ReplyKeyboardMarkup(resize_keyboard=True)
kb_science.row(science_b1, science_b2, science_b3).row(science_b4, science_b5)

"""Клавиатура творчество"""
art_text_b1 = "Web-дизайнер"
art_text_b2 = "Графический дизайнер"
art_text_b3 = "Музыка"
art_text_b4 = "Фото/видео съёмка"
art_text_b5 = "Блогер"
art_all = [art_text_b1, art_text_b2, art_text_b3, art_text_b4, art_text_b5]
art_b1 = KeyboardButton(art_text_b1)
art_b2 = KeyboardButton(art_text_b2)
art_b3 = KeyboardButton(art_text_b3)
art_b4 = KeyboardButton(art_text_b4)
art_b5 = KeyboardButton(art_text_b5)
kb_art = ReplyKeyboardMarkup(resize_keyboard=True)
kb_art.row(art_b1, art_b2, art_b3).row(art_b4, art_b5)


check_pair_b1_text = 'Посмотреть пару'
check_pair_all = [check_pair_b1_text]
check_pair_b1 = KeyboardButton(check_pair_b1_text)
kb_check_pair = ReplyKeyboardMarkup(resize_keyboard=True)
kb_check_pair.row(check_pair_b1)

search_text_b1 = "👍"
search_text_b2 = "👎"
search_text_all = [search_text_b2, search_text_b1]
search_b1 = KeyboardButton(search_text_b1)
search_b2 = KeyboardButton(search_text_b2)
search_kb = ReplyKeyboardMarkup(resize_keyboard=True)
search_kb.row(search_text_b1, search_text_b2)
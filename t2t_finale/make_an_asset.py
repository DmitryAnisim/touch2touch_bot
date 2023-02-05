from sql_bases.sql import *


'''
Функция ищет данные пользователя с определенным user_id во всех базах
и сохраняет словарь с данными в переменную data

Как только данные найдены мы можем сохранить ссылку на фото 
в отдельную переменную и удалить из data

Дальше мы удаляем все ненужные для анкеты данные из data с помощью метода .pop()

Начинаем составлять анкету:
    1) Берем username и сохраняем его с @ в качестве префикса
    2) Удаляем username
    3) Сохраняем все остальные данные через \n

Возвращаем составленную анкету и фото
'''

def make_an_asset(user_id, database_names):
    data = sql_get_all_user_data(user_id, database_names)
    print(data)
    photo = data['user_profile_photo']
    data.pop('user_profile_photo')
    data.pop('user_id')
    data.pop('database_name')
    data.pop
    asset = f'''Анкета:\n@{data['username']}\n\n'''
    data.pop('username')
    for i in data.values():
        asset += str(i)
        asset += '\n'
    return asset, photo 

if __name__ == '__main__':
    print(make_an_asset(542541752, database_names))
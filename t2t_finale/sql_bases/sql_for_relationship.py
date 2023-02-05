import sqlite3 as sq
import pandas as pd
from random import shuffle


def sql_relationship():
    global base, cur
    base = sq.connect("relationship_db.db")
    cur = base.cursor()
    if base:
        print("База данных для отношений работает!")
    cur.execute("""CREATE TABLE IF NOT EXISTS menu
                (sex TEXT, 
                age INTEGER,
                about_myself TEXT,
                user_id INTEGER,
                username TEXT,
                user_profile_photo TEXT,
                user_likes TEXT,
                counter INTEGER)"""
                )
    base.commit()

async def sql_add_relationship(data):
    cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
    base.commit()

def sql_add_user_likes(user_id, my_like):
    con = sq.connect("relationship_db.db")
    cur = con.cursor()
    sql_pick = f'SELECT user_likes FROM menu WHERE user_id = {user_id}'
    cur.execute(sql_pick)
    record = cur.fetchone()[-2]
    record_counter = cur.fetchone()[-1]
    sql_add_likes = f'UPDATE menu SET user_likes = "{record} {my_like}" WHERE user_id = {user_id}'
    sql_change_counter = f'UPDATE menu SET counter = {record_counter + 1} WHERE user_id = {user_id}'
    cur.execute(sql_change_counter)
    cur.execute(sql_add_likes)

def sql_find_right_sex(sex):
    con = sq.connect("relationship_db.db")
    cur = con.cursor()
    if sex == "Мужчина":
        sql_pick = f'SELECT user_id FROM menu WHERE sex = "Женщина"'
    if sex == "Женщина":
        sql_pick = f'SELECT user_id FROM menu WHERE sex = "Мужчина"'
    df = pd.read_sql(sql_pick, con)
    if df.empty:
        return None
    user_ids = [i for i in df.to_dict('records')]
    shuffle(user_ids)
    return user_ids

if __name__ == '__main__':
    print(sql_find_right_sex("Женщина"))



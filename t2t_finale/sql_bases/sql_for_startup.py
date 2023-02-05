import sqlite3 as sq
import pandas as pd

def sql_startup():
    global base, cur
    base = sq.connect("startup_db.db")
    cur = base.cursor()
    if base:
        print("База данных для стартапов работает!")
    cur.execute("""CREATE TABLE IF NOT EXISTS startup_menu
                (employment TEXT, 
                job TEXT,
                problem TEXT,
                user_id INTEGER,
                username TEXT,
                user_profile_photo TEXT,
                user_likes TEXT,
                counter INT)"""
                )
    base.commit()

async def sql_add_startup(data):
    cur.execute("INSERT INTO startup_menu VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
    base.commit()

def sql_add_user_likes(user_id, my_like):
    con = sq.connect("startup_db.db")
    cur = con.cursor()
    sql_pick = f'SELECT user_likes FROM startup_menu WHERE user_id = {user_id}'
    cur.execute(sql_pick)
    record = cur.fetchone()[-2]
    record_counter = cur.fetchone()[-1]
    sql_add_likes = f'UPDATE startup_menu SET user_likes = "{record} {my_like}" WHERE user_id = {user_id}'
    sql_change_counter = f'UPDATE startup_menu SET counter = {record_counter + 1} WHERE user_id = {user_id}'
    cur.execute(sql_change_counter)
    cur.execute(sql_add_likes)
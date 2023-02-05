import sqlite3 as sq
import pandas as pd

def sql_investment():
    global base, cur
    base = sq.connect("investment_db.db")
    cur = base.cursor()
    if base:
        print("База данных для инвесторов работает!")
    cur.execute("""CREATE TABLE IF NOT EXISTS investment_menu
                (investments TEXT,
                user_id INTEGER,
                username TEXT,
                user_profile_photo TEXT,
                user_likes TEXT,
                counter INT)"""
                )
    base.commit()

async def sql_add_investment(data):
    cur.execute("INSERT INTO investment_menu VALUES (?, ?, ?, ?, ?, ?)", tuple(data.values()))
    base.commit()

def sql_change_counter(user_id):
    con = sq.connect("investment_db.db")
    cur = con.cursor()
    sql_pick = f'SELECT * FROM investment_menu WHERE user_id = {user_id}'
    cur.execute(sql_pick)
    record = cur.fetchone()[-1]
    sql_change = f'UPDATE menu SET assets_counter = {record + 1} WHERE user_id = {user_id}'
    cur.execute(sql_change)

def sql_add_user_likes(user_id, my_like):
    con = sq.connect("investment_db.db")
    cur = con.cursor()
    sql_pick = f'SELECT * FROM investment_menu WHERE user_id = {user_id}'
    cur.execute(sql_pick)
    try:
        record = cur.fetchone()[-2]
        record_counter = cur.fetchone()[-1]
    except TypeError:
        record = ''
        record_counter = 0
    sql_add_likes = f'UPDATE investment_menu SET user_likes = "{record} {my_like}" WHERE user_id = {user_id}'
    sql_change_counter = f'UPDATE investment_menu SET counter = {record_counter + 1} WHERE user_id = {user_id}'
    cur.execute(sql_change_counter)
    cur.execute(sql_add_likes)


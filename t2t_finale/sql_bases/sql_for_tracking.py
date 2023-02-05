import sqlite3 as sq
import pandas as pd

def sql_tracking():
    global base, cur
    base = sq.connect("sql_for_tracking.db")
    cur = base.cursor()
    if base:
        print("База данных для трекинка работает!")
    cur.execute("""CREATE TABLE IF NOT EXISTS menu
                (username TEXT,
                complete INTEGER)"""
                )
    base.commit()

async def sql_add_tracking(data):
    cur.execute("INSERT INTO tracking_menu VALUES (?, ?)", tuple(data.values()))
    base.commit()

def sql_zero_complete(username):
    con = sq.connect("sql_for_tracking.db")
    cur = con.cursor()
    change_complete = f'UPDATE menu SET complete = 0 WHERE username = {username}'
    cur.execute(change_complete)

def sql_add_complete(username):
    con = sq.connect("sql_for_tracking.db")
    cur = con.cursor()
    change_complete = f'UPDATE menu SET complete = 1 WHERE username = {username}'
    cur.execute(change_complete)
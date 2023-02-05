import sqlite3 as sq
import pandas as pd

def sql_networking():
    global base, cur
    base = sq.connect("networking_db")
    cur = base.cursor()
    if base:
        print("База данных для нетворкингов работает!")
    cur.execute("""CREATE TABLE IF NOT EXISTS networking_menu
                (time TEXT
                networking TEXT)"""
                )
    base.commit()

async def sql_add_networking(data):
    cur.execute("INSERT INTO networking_menu VALUES (?, ?)", tuple(data.values()))
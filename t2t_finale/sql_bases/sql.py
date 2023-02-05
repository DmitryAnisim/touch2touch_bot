import sqlite3 as sq
import pandas as pd
from config import database_names
from random import shuffle

async def sql_delete_user(user_id, database_names):
    for database_name, table_name in database_names:
        base = sq.connext(database_name)
        cur = base.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE user_id = ?", (user_id, ))
        base.commit()

def sql_get_all_user_data(user_id, database_names):
    for database_name, table_name in database_names:
        con = sq.connect(database_name)
        df = pd.read_sql(f"SELECT * FROM {table_name} WHERE user_id = {user_id}", con)
        if df.empty:
            continue
        else:
            break
    if df.empty:
        return None
    return [i for i in df.to_dict('records')][0]

def sql_change_counter(user_id, database_names):
    for database_name, table_name in database_names:
        con = sq.connect(database_name)
        cur = con.cursor()
        sql_pick = f'SELECT * FROM {table_name} WHERE user_id = {user_id}'
        cur.execute(sql_pick)
        record = cur.fetchone()[-1]
        sql_change = f'UPDATE menu SET assets_counter = {record + 1} WHERE user_id = {user_id}'
        cur.execute(sql_change)

def sql_get_all_user_ids(database_names):
    ids = []
    for database_name, table_name in database_names:
        con = sq.connect(database_name)
        cur = con.cursor()
        sql_pick = f'SELECT user_id FROM {table_name}'
        df = pd.read_sql(sql_pick, con)
        ids.extend(df)
    if df.empty:
        return []
    return df

# def get_user_counter(user_id, database_names):
#     for database_name, table_name in database_names:
#         con = sq.connect(database_name)
#         cur = con.cursor()
#         sql_pick = f'SELECT counter FROM {table_name} WHERE user_id = {user_id}'




def sql_get_random_inv_start(database_names):
    ans = []
    for database_name, table_name in database_names:

        if database_name == 'relationship_db.db':
            break

        con = sq.connect(database_name)
        cur = con.cursor()
        sql_pick = f'SELECT user_id FROM {table_name}'
        df = pd.read_sql(sql_pick,con)
        df = df.to_dict('records')
        ans.extend([i for i in df.values()])
    shuffle(ans)
    return ans
    
def sql_get_random_start(database_names):
    ans = []
    for database_name, table_name in database_names:
        if database_name == 'relationship_db.db':
            break
        if database_name == 'investment_db.db':
            break
        
        sql_pick = f'SELECT user_id FROM {table_name}'

        con = sq.connect(database_name)
        cur = con.cursor()
        df = pd.read_sql(sql_pick,con)
        df = df.to_dict('records')
        ans.extend([i for i in df.values()])
    shuffle(ans)
    return ans

def sql_get_all_user_likes(user_id, database_names):
    for database_name, table_name in database_names:
        con = sq.connect(database_name)
        df = pd.read_sql(f"SELECT user_likes FROM {table_name} WHERE user_id = {user_id}", con)
        if df.empty:
            continue
        else:
            break
    if df.empty:
        return None
    df = df.to_dict('records')
    return [i for i in df.values()][0].split()

def sql_find_user_database(user_id, database_names = database_names):
    for database_name, table_name in database_names:
        con = sq.connect(database_name)
        df = pd.read_sql(f"SELECT * FROM {table_name} WHERE user_id = {user_id}", con)
        if df.empty:
            continue
        else:
            return database_name
            break
    return ''
    

def sql_():
    pass

if __name__ == '__main__':
    pass
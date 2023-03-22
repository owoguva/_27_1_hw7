import random
import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.db')
    cursor = db.cursor()

    if db:
        print('Connect!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, "
               "username VARCHAR (100), "
               "name VARCHAR (100),"
               "direction INTEGER,"
               "age INTEGER,"
               "\"group\" VARCHAR (100))")
    db.commit()
async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO mentors values (?, ?, ?, ?, ?, ?)',
                       tuple(data.values()))
        db.commit()

async def sql_command_random():
    result = cursor.execute("SELECT * FROM mentors ;").fetchall()
    random_user = random.choice(result)
    return random_user

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE ID = ?", (id,))
    db.commit()

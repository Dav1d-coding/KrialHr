import sqlite3

def save_user(id):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
     id INTEGER   
    )""")
    connect.commit()
    #add
    users_list = [id]
    cursor.execute("""INSERT INTO login_id VALUES(?);""", users_list)
    connect.commit()


def check_user(id):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT id FROM login_id WHERE id = {id}""")
    data = cursor.fetchone()
    if data is None:
        return True
    else:
        return False

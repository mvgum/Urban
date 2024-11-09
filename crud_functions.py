import sqlite3


def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.commit()
    connection.close()
    return prod


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (user, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT user FROM Users')
    result = cursor.fetchall()
    print(username)
    print(result)
    flag = False
    for name in result:
        if username in name:
            flag = True
            break
    connection.commit()
    connection.close()
    print(flag)
    return flag


initiate_db()

# connection = sqlite3.connect('not_telegram.db')
# cursor = connection.cursor()
#
# cursor.execute("INSERT INTO Products (title, description, price) VALUES('Витамин A', 'Описание A', 100)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES('Витамин B', 'Описание B', 200)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES('Витамин C', 'Описание C', 300)")
# cursor.execute("INSERT INTO Products (title, description, price) VALUES('Витамин D', 'Описание D', 400)")
#
# connection.commit()
# connection.close()

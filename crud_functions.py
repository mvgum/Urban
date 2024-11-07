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


# initiate_db()
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

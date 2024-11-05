# Домашнее задание по теме "Выбор элементов и функции в SQL запросах.".
import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute("DELETE FROM Users WHERE id = 6")
cursor.execute("SELECT SUM(balance) FROM Users")
cursor.execute("SELECT COUNT(*) FROM Users")
total_count = cursor.fetchone()[0]
print(total_count)
total_sum = cursor.fetchone()[0]
print(total_sum)
print(total_sum / total_count)

connection.commit()
connection.close()

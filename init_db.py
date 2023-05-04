import sqlite3

DATABASE_NAME = 'database.db'

connection = sqlite3.connect(DATABASE_NAME)

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()


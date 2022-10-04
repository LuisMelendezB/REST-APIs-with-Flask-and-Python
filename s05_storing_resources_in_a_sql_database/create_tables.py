import sqlite3


connection = sqlite3.connect("data.db")
coursor = connection.cursor()

query = "CREATE TABLE items (name TEXT, price REAL)"

coursor.execute(query)

query = "CREATE TABLE users (id PRIMARY_KEY, username TEXT, password TEXT)"

connection.commit()

connection.close()
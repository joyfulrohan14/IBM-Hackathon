import sqlite3

'''
This file creates the database
Declan, since your working on this (atm), you can configure it the way you see fit

Right now, this is run before app.py to get db.
'''

conn = sqlite3.connect('database.db')       # creates a database in database.db which is the name DATABASE uses
print("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, school TEXT, major TEXT, role TEXT)')       # for testing purposes
print("Table created successfully")
conn.close()

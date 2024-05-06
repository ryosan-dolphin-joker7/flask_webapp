import sqlite3

DATABASE = 'database.db'

def create_books_table():
    conn = sqlite3.connect('database.db')
    #c = conn.cursor()
    conn.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER)')
    conn.close()
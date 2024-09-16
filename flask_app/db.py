# SQLite3を使ってデータベース操作を行う
import sqlite3

# データベースファイルのパスを定義
DATABASE = 'database.db'

# booksテーブルを作成する関数
def create_books_table():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INTEGER)')
    conn.close()

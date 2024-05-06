from flask import Flask
app = Flask(__name__)
from flask_app import main

from flask_app import db
db.create_books_table()
from flask import Flask
app = Flask(__name__)
from . import app

from flask_app import db
db.create_books_table()
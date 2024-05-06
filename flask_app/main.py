from flask_app import app
from flask import render_template

@app.route('/')
def index():
    books = [
        {'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year': 1925},
        {'title': 'M',
        'author': 'Fritz Lang',
        'year': 1931}
    ]
    return render_template('index.html', books=books)

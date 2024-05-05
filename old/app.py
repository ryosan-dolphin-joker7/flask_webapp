from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask backend'

@app.route('/api/data')
def get_data():
    return 'Data from Flask backend'

if __name__ == '__main__':
    app.run(debug=True)

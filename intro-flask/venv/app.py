from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() :
    return 'hola mundo'

@app.route('/lala')
def lala() :
    return 'lala'
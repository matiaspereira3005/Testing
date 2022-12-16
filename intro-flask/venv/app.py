from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index() :
    return 'hola mundo'

#GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id) :
    if request.method== 'GET':
        return 'El id del post es: ' + post_id 
    else:
        return 'Este es otro metodo y no GET'

#curl.exe -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/lele
@app.route('/lele', methods=['POST'])
def lele() :
    print (request.form)
    print (request.form['llave1'])
    print (request.form['llave2'])
    return 'lele'
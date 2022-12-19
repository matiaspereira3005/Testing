from flask import Flask, request, url_for, redirect, abort,render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='Morpheus',
    password='Theflash*3022',
    database='prueba'
)

cursor = midb.cursor(dictionary=True)

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
@app.route('/lele', methods=['POST','GET'])
def lele() :
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    #abort(403)
    #return redirect(url_for('lala', post_id=2))
    #print (request.form)
    #print (request.form['llave1'])
    #print (request.form['llave2'])
    #return render_template('lele.html')
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola mundo')

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = 'insert into usuario (username, email, edad) values (%s, %s, %s)'
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()

        return redirect(url_for('lele'))
    return render_template('crear.html')
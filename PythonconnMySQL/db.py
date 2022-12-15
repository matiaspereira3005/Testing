import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='Morpheus',
    password='Theflash*3022',
    database='prueba'
)

cursor = midb.cursor()

#listar datos
cursor.execute('select * from Usuario')
resultado = cursor.fetchall()
print(resultado)

#ver definicion de tablas
#cursor.execute('show create table Usuario')

#insertar datos
#sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
#values = ('correo@matias.cl', 'tomas', 45)
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)

#actualizar datos
#sql = 'update usuario set email = %s  where id = %s'
#values = ('matias@gmail.cl', 5)
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)

#eliminar datos
#sql = 'delete from usuario where id = %s'
#values = (5, )
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)
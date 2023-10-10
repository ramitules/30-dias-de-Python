import sqlite3 as sql

conn = sql.connect('test.db')
cursor = conn.cursor()

#Transacciones para agrupar operaciones y confirmar, o revertir si hay un error
try:
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Usuario1', 30))
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Usuario2', 22))

    conn.commit()
    
except sql.Error as error:
    conn.rollback()
    print(f"ERROR: {error!r}")

#Trabajar en modo Solo Lectura utilizando URIs
con_r = sql.connect('file:test.db?mode=ro', uri=True)

#Consulta de datos 2
#Primero, seleccionar lo que nos interesa, en este caso todos los usuarios
cursor.execute('SELECT * FROM usuarios')

#Luego, almacenar los datos en una lista
usuarios = cursor.fetchall()

#Por ultimo, trabajar con esa lista
for usuario in usuarios:
    print(usuario)
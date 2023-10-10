import sqlite3 as sql

#Conectarse a base de datos. Si no existe la crea
conn = sql.connect('test.db')

#Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

#Crear tabla "usuarios" con ID unico, nombre y edad
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )''')

#Insertar usuarios
cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Ramiro', 26))

#Insertar varios usuarios
usuarios = [('Gaston', 25), ('Romualdo', 99)]
cursor.executemany('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', usuarios)

#Actualizar datos
cursor.execute('UPDATE usuarios SET edad = ? WHERE nombre = ?', (30, 'Romualdo'))

#Eliminar datos
cursor.execute('DELETE FROM usuarios WHERE nombre = ?', ('Gaston',))

#Consulta de datos
for fila in conn.execute('SELECT * FROM usuarios'):
    print(fila)

#Confirmar cambios
conn.commit()

#Deshacer cambios
conn.rollback()

#Se puede utilizar contexto para hacer commit o rollback automaticamente
with conn:
    conn.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Romualdo', 30))

#Cerrar sesion
conn.close()
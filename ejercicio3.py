import sqlite3

conexion = sqlite3.connect('escuela.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    curso TEXT)''')

alumnos = [
    ('Lucio', 'Matemáticas'),
    ('Rodrigo', 'Historia'),
    ('Juan', 'Ciencias')
]

cursor.executemany("INSERT INTO alumnos (nombre, curso) VALUES (?, ?)", alumnos)

conexion.commit()

conexion.close()

print("Base de datos creada y poblada exitosamente.")
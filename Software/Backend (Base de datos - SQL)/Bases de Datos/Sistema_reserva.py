import sqlite3
conexion = sqlite3.connect("Balines_mojados.db")
cursor = conexion.cursor()
import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('Balines_mojados.db')

# Crear un cursor usando el método cursor() del objeto de conexión
cursor = conn.cursor()

create_canchas_table_sql = '''
CREATE TABLE IF NOT EXISTS canchas (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_sucursal INTEGER NOT NULL,
    Año INTEGER NOT NULL,
    Mes INTEGER NOT NULL,
    Dia INTEGER NOT NULL,
    Hora INTEGER NOT NULL,
    Minuto INTEGER NOT NULL
)
'''

create_cliente_table_sql = '''
CREATE TABLE IF NOT EXISTS cliente (
    Dni INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefono INTEGER NOT NULL
)
'''

create_personal_table_sql = '''
CREATE TABLE IF NOT EXISTS personal (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_sucursal INTEGER NOT NULL,
    Clave_acceso TEXT NOT NULL,
    Dni INTEGER NOT NULL,
    Nombre TEXT NOT NULL,
    Apellido TEXT NOT NULL
)
'''

create_reservas_table_sql = '''
CREATE TABLE IF NOT EXISTS reservas (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_personal INTEGER NOT NULL,
    Id_cancha INTEGER NOT NULL,
    Id_sucursal INTEGER NOT NULL,
    Dni_cliente INTEGER NOT NULL
)
'''

create_sucursales_table_sql = '''
CREATE TABLE IF NOT EXISTS sucursales (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_cancha INTEGER NOT NULL,
    Barrio TEXT NOT NULL,
    Calle_altura TEXT NOT NULL
)
'''
cursor.execute(create_canchas_table_sql)
cursor.execute(create_cliente_table_sql)
cursor.execute(create_personal_table_sql)
cursor.execute(create_reservas_table_sql)
cursor.execute(create_sucursales_table_sql)

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

import sqlite3

conn = sqlite3.connect('Balines_mojados.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS sucursales(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               barrio TEXT(30) NOT NULL,
               calle TEXT(30) NOT NULL,
               altura TEXT(4) NOT NULL,
               estado TEXT(20) NOT NULL)""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS canchas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               id_sucursal INTEGER(3) NOT NULL,
               tamaño TEXT(10) NOT NULL,
               tipo TEXT(10) NOT NULL,
               obstaculos TEXT(20) NOT NULL,
               min_jugadores int(2) NOT NULL,
               max_jugadores int(2) NOT NULL,
               terreno TEXT(20) NOT NULL,
               medidas TEXT(20) NOT NULL,
               estado TEXT(20) NOT NULL,
               FOREIGN KEY (id_sucursal) REFERENCES sucursales(id))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS reservas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dni_personal INTEGER(3) NOT NULL,
                id_cancha INTEGER(3) NOT NULL,
                id_sucursal INTEGER(3) NOT NULL,
                dni_cliente INTEGER(8) NOT NULL,
                fecha TEXT(4) NOT NULL,
                hora_inicio INTEGER(2) NOT NULL,
                hora_final INTEGER(2) NOT NULL,
                estado TEXT(20) NOT NULL,
                FOREIGN KEY (dni_personal) REFERENCES personal(dni),
                FOREIGN KEY (id_cancha) REFERENCES canchas(id),
                FOREIGN KEY (id_sucursal) REFERENCES sucursales(id),
                FOREIGN KEY (dni_cliente) REFERENCES clientes(dni))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS personal(
               dni INTEGER(8) PRIMARY KEY NOT NULL,
               id_sucursal INTEGER(3) NOT NULL,
               clave TEXT(15) NOT NULL,
               nombre TEXT(30) NOT NULL,
               apellido TEXT(30) NOT NULL,
               trabajo TEXT(30) NOT NULL,
               FOREIGN KEY (id_sucursal) REFERENCES sucursales(id))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
                dni INTEGER PRIMARY KEY,
                nombre TEXT(40),
                apellido TEXT(40),
                edad INTEGER(2),
                email TEXT(50),
                telefono INT(13))""")
conn.commit()
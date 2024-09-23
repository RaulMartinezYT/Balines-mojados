import sqlite3

conn = sqlite3.connect('Balines_mojados.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS sucursales(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               barrio TEXT(30) NOT NULL,
               calle TEXT(30) NOT NULL,
               altura INT(4) NOT NULL,
               estado TEXT(20) NOT NULL)""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS canchas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               id_sucursal INTEGER NOT NULL,
               tamaño TEXT(10) NOT NULL,
               tipo TEXT(10) NOT NULL,
               obstaculos TEXT(20) NOT NULL,
               min_jugadores INTEGER NOT NULL,
               max_jugadores INTEGER NOT NULL,
               terreno TEXT(20) NOT NULL,
               medidas TEXT(20) NOT NULL,
               estado TEXT(20) NOT NULL,
               FOREIGN KEY (id_sucursal) REFERENCES sucursales(id))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS reservas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dni_personal INTEGER NOT NULL,
                id_cancha INTEGER NOT NULL,
                dni_cliente INTEGER NOT NULL,
                fecha TEXT(10) NOT NULL,
                hora_inicio TEXT(5) NOT NULL,
                hora_final TEXT(5) NOT NULL,
                estado TEXT(20) NOT NULL,
                FOREIGN KEY (dni_personal) REFERENCES personal(dni),
                FOREIGN KEY (id_cancha) REFERENCES canchas(id),
                FOREIGN KEY (dni_cliente) REFERENCES clientes(dni))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS pagos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               id_reserva INTEGER NOT NULL,
               monto DECIMAL(10, 2) NOT NULL,
               metodo TEXT(30) NOT NULL,
               fecha_creacion TEXT(10) NOT NULL,
               estado TEXT(10) NOT NULL,
               FOREIGN KEY (id_reserva) REFERENCES reservas(id))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS personal(
               dni INTEGER PRIMARY KEY NOT NULL,
               id_sucursal INTEGER NOT NULL,
               clave TEXT(15) NOT NULL,
               nombre TEXT(30) NOT NULL,
               apellido TEXT(30) NOT NULL,
               trabajo TEXT(30) NOT NULL,
               FOREIGN KEY (id_sucursal) REFERENCES sucursales(id))""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
                dni INTEGER PRIMARY KEY,
                nombre TEXT(30),
                apellido TEXT(30),
                edad INTEGER,
                email TEXT(50),
                telefono INT(13))""")
conn.commit()
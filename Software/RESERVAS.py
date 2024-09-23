import sqlite3

conn = sqlite3.connect("Balines_mojados.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

def obtener_datos():
    pregunta         = input("Es un cliente nuevo:  Y/N\n")
    if pregunta == "Y" or pregunta == "y":
        dni_personal     = int(input("Dni de personal: "))
        dni_cliente      = int(input("Dni cliente: "))
        nombre_cliente   = str(input("Nombre cliente: "))
        apellido_cliente = str(input("Apellido cliente: "))
        edad_cliente     = str(input("Edad cliente: "))
        email_cliente    = str(input("Email cliente: "))
        telefono_cliente = str(input("Telefono cliente: "))
        id_cancha        = int(input("Id de cancha: "))
        fecha            = str(input("Fecha reserva: "))
        hora_inicio      = str(input("Hora de inicio: "))
        hora_final       = str(input("Hora de final: "))
        estado           = str(input("Estado de la reserva: "))
        consulta1        = "INSERT INTO clientes (dni, nombre, apellido, edad, email, telefono) VALUES (?, ?, ?, ?, ?, ?)"
        datos1           = (dni_cliente, nombre_cliente, apellido_cliente, edad_cliente, email_cliente, telefono_cliente)
        cursor.execute(consulta1, datos1)
        conn.commit()
        consulta2 = "INSERT INTO reservas (dni_personal, dni_cliente, id_cancha, fecha, hora_inicio, hora_final, estado) VALUES (?, ?, ?, ?, ?, ?, ?)"
        datos2 = (dni_personal, dni_cliente, id_cancha, fecha, hora_inicio, hora_final, estado)
        cursor.execute(consulta2, datos2)
        conn.commit()

    if pregunta == "N" or pregunta == "n":
        dni_personal     = int(input("Dni de personal: "))
        dni_cliente      = int(input("Dni cliente: "))
        id_cancha        = int(input("Id de cancha: "))
        fecha            = str(input("Fecha reserva: "))
        hora_inicio      = str(input("Hora de inicio: "))
        hora_final       = str(input("Hora de final: "))
        estado           = str(input("Estado de la reserva: "))
        consulta         = "INSERT INTO reservas (dni_personal, dni_cliente, id_cancha, fecha, hora_inicio, hora_final, estado) VALUES (?, ?, ?, ?, ?, ?, ?)"
        datos            = (dni_personal, dni_cliente, id_cancha, fecha, hora_inicio, hora_final, estado)
        cursor.execute(consulta, datos)
        conn.commit()

obtener_datos()

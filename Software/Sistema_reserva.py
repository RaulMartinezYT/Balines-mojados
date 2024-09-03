import sqlite3

def limpiar_str(a):
    a = a.lower()
    a = a.replace(" ", "_")
    a = a.replace("-", "_")
    return a

def crear_base_datos():
    conn = sqlite3.connect('Balines_mojados.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS sucursales (id INTEGER PRIMARY KEY AUTOINCREMENT, id_cancha INTEGER(3) NOT NULL, barrio TEXT(30) NOT NULL, calle TEXT(30) NOT NULL,altura INT(4) NOT NULL)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS personal (id INTEGER PRIMARY KEY AUTOINCREMENT, id_sucursal INTEGER(3) NOT NULL, clave_acceso TEXT(15) NOT NULL, dni INTEGER(8) NOT NULL, nombre TEXT(30) NOT NULL, apellido TEXT(30) NOT NULL, trabajo TEXT(30) NOT NULL)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS canchas (id INTEGER PRIMARY KEY AUTOINCREMENT, id_sucursal INTEGER(3) NOT NULL, año INTEGER(4) NOT NULL, mes INTEGER(2) NOT NULL, dia INTEGER(2) NOT NULL, hora INTEGER(2) NOT NULL, minuto INTEGER(2) NOT NULL)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS reservas ( id INTEGER PRIMARY KEY AUTOINCREMENT, id_personal INTEGER(3) NOT NULL, id_cancha INTEGER(3) NOT NULL, id_sucursal INTEGER(3) NOT NULL, dni_cliente INTEGER(8) NOT NULL)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS clientes ( dni INTEGER PRIMARY KEY, edad INTEGER(2), nombre TEXT(30), apellido TEXT(30))")
    conn.commit()

def datos_existentes(dni, edad, nombre, apellido):
    conn = sqlite3.connect('Balines_mojados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM clientes WHERE dni = ?", (dni,))
    if cursor.fetchone():
        print("Persona ya existente")
    else:
        subir_datos_cliente(dni, edad, nombre, apellido)
        print("Persona guardada con exito")

def subir_datos_cliente(dni, edad, nombre, apellido):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    consulta = "INSERT INTO clientes (dni, edad, nombre, apellido) VALUES (?, ?, ?, ?)"
    datos = (dni, edad, nombre, apellido)
    cursor.execute(consulta, datos)
    conn.commit()
    conn.close()

def tomar_datos_cliente():
    Dni = str(input("Dni del reservador: "))
    print(Dni)
    
    if len(Dni) == 8:
        try:
            Dni = int(Dni)

        except ValueError:
            print("Numeros unicamente")
            return 100 # Letra dentro de los numeros
    else:
        if len(Dni) < 8:
            print("DNI Incompleto")
            return 101

        if len(Dni) > 8:
            print("DNI Inexistente")
            return 102



    Edad = str(input("Edad del reservador: "))
    if len(Edad) == 2:
        try:
            Edad = int(Edad)

        except ValueError:
            print("Numeros unicamente")
            return 103 # Letra dentro de los numeros
    else:
        if len(Edad) <= 1 or len(Edad) >= 3:
            print("Edad inapropiada")
            return 104


    Nombre = str(input("Nombre del reservador: "))
    if len(Nombre) <= 30 and len(Nombre) >= 3:
        pass

    else:
        if len(Nombre) >= 31:
            print("Nombre demasiado largo")
            return 105
        if len(Nombre) <= 2:
            print("Apellido demasiado corto")
            return 106

    Apellido = str(input("Apellido del reservador: "))

    if len(Apellido) <= 30 and len(Apellido) >= 3:
        pass

    else:
        if len(Apellido) >= 31:
            print("Nombre demasiado largo")
            return 105
        if len(Apellido) <= 2:
            print("Apellido demasiado corto")
            return 106

    datos_existentes(Dni, Edad, Nombre, Apellido)

crear_base_datos()
tomar_datos_cliente()

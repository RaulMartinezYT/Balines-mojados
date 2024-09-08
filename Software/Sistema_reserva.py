import sqlite3

def datos_existentes(dni, edad, nombre, apellido, email, telefono):
    conn = sqlite3.connect('Balines_mojados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM clientes WHERE dni = ?", (dni,))
    
    if cursor.fetchone():
        print("Persona ya existente")
        
    else:
        subir_datos_cliente(dni, edad, nombre, apellido, email, telefono)
        print("Persona guardada con exito")


def subir_datos_cliente(dni, edad, nombre, apellido, email, telefono):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    consulta = "INSERT INTO clientes (dni, edad, nombre, apellido, email, telefono) VALUES (?, ?, ?, ?, ?, ?)"
    datos = (dni, edad, nombre, apellido, email, telefono)
    cursor.execute(consulta, datos)
    conn.commit()
    conn.close()

def tomar_datos_cliente():

    # Dni de la persona que va a realizar la reserva
    try:
        dni = abs(int(input("Dni del reservador: ")))
        dni = str(dni)

        if len(dni) < 8 :
            print("Dni incompleto")
            return 100
        
        if len(dni) > 8:
            print("Dni inexistente")
            return 101
        
        dni = int(dni)

    except ValueError:
        print("Unicamente numeros")
        return 100


    # Edad de la persona que realizará la reserva
    try:
        edad = abs(int(input("Edad del reservador: ")))
        edad = str(edad)
        
        if len(edad) < 1 or len(edad) > 2:
            print("Edad inexistente")
            return 100
        
        if len(edad) == 2 or len(edad) == 1:
            edad = int(edad)

            if edad >= 16 and edad < 18:
                print("Necesita un mayor responsable para jugar")
                return 101

            if edad < 16 or edad >= 80:
                print("Edad inapropiada para jugar")
                return 102
    
    except ValueError:
        print("Unicamente numeros")
        return 103


    # Nombre de la persona que realizará la reserva
    nombre = str(input("Nombre del reservador: "))
    nombre = nombre.replace(" ", "")
    
    if nombre.isalpha():
        print("Es solo letras")
        print(nombre)

        if len(nombre) < 3:
            print("El nombre es muy corto")
            return 102
        
        if len(nombre) > 30:
            print("El nombre es muy largo")
            return 123
        
    else:
        print("Es algo mas que letras solas")
        print(nombre)
        return 120


    # Apellido de la persona que realizará la reserva
    apellido = str(input("Apellido del reservador: "))
    apellido = apellido.replace(" ", "")

    if apellido.isalpha():
        print("Es solo letras")

        if len(apellido) < 3:
            print("El apellido es muy corto")
            return 102
        
        if len(apellido) > 30:
            print("El apellido es muy largo")
            return 123
        
    else:
        print("Es algo mas que letras solas")
        return 120
    
    while True:
        email = str(input("Mail del reservador:\n"))
        email_confirmacion = str(input("Confirme el mail:\n"))

        if email == email_confirmacion:
            break
        else:
            print("Email incorrecto, volve a intentarlo!\n")

    
    try:
        telefono = abs(int(input("Telefono del reservador: +54 9 ")))
        telefono = str(telefono)
        
        if len(telefono) < 10 or len(telefono) > 10:
            print("Telefono inexistente")
            return 100
        else:
            telefono = int(telefono)
    
    except ValueError:
        print("Unicamente numeros")
        return 103

    datos_existentes(dni, edad, nombre, apellido, email, telefono)

tomar_datos_cliente()
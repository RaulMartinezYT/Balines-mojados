import sqlite3

conn = sqlite3.connect('Balines_mojados.db')
cursor = conn.cursor()

def tomar_datos_personal():
    while True:
        # Dni del personal a añadir
        try:
            dni = abs(int(input("Dni del personal: ")))
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
        
        sucursal = input("Id de sucursal:\n")

        # Clave del personal a añadir
        clave = str(input("Clave del personal: "))

        if len(clave) < 8:
            print("Clave muy corta, 8 caracteres minimo")
            return 100
        else:
            if len(clave) > 15:
                print("Clave muy larga, 15 caracteres maximo")
            else:
                while True:
                    confirmacion = input("Ingrese nuevamente la clave para su confirmación:\n")
                    if confirmacion == clave:
                        print("Clave confirmada\n")
                        break
                    else:
                        print("Vuelve a intentarlo\n")

        # Nombre del personal a añadir
        nombre = str(input("Nombre del personal: "))
        nombre = nombre.lower()
        nombre = nombre.lstrip()
        
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
        
        apellido = str(input("Apellido del personal: "))
        apellido = apellido.lower()
        apellido = apellido.lstrip()
        
        if apellido.isalpha():
            print("Es solo letras")
            print(apellido)

            if len(apellido) < 3:
                print("El apellido es muy corto")
                return 102
            
            if len(apellido) > 30:
                print("El apellido es muy largo")
                return 123
            
        else:
            print("Es algo mas que letras solas")
            print(apellido)
            return 120
        
        trabajo = int(input("¿En que area desempeña su labor?\n1.Recepcionista\n2.Referí\n3.Equipamiento\n4.Mantenimiento\n5.Seguridad\nTu eleccion es: "))
        match trabajo:
            case 1:
                trabajo = "recepcionista"
            case 2:
                trabajo = "referi"
            case 3:
                trabajo = "equipamiento"
            case 4:
                trabajo = "mantenimiento"
            case 5:
                trabajo = "seguridad"
        
        correcto = str(input(f"¿Los datos son correctos?\nDni del personal: {dni}\nLa sucursal del personal es: {sucursal}\nLa clave del personal es: {clave}\nEl nombre del personal es: {nombre}\nEl apellido del personal es: {apellido}\nEl trabajo que desempeña es: {trabajo}\n¿Son estos datos correctos? Si/No\n"))
        correcto = correcto.lower()

        if correcto == "s" or correcto == "si":
            consulta = "INSERT INTO personal (dni, id_sucursal, clave_acceso, nombre, apellido, trabajo) VALUES (?, ?, ?, ?, ?, ?)"
            datos = (dni, sucursal, clave, nombre, apellido, trabajo)
            cursor.execute(consulta, datos)
            conn.commit()
            print("Persona añadida correctamente")
            break
        else:
            print("Te vuelvo a solicitar los datos del personal: \n")

accion = int(input("¿Que accion deseas realizar?\n1.Agregar datos\n"))

match accion:
    case 1:
        accion2 = int(input("¿Que accion deseas realizar?\n1.Agregar personal\n2.Agregar cancha\n3.Agregar sucursal\n"))
        match accion2:
            case 1:
                tomar_datos_personal()
            case 2:
                print("Todavia no hay nada")
            case 3:
                print("Todavia no hay nada")
import sqlite3, os

def limpiar_nombre(a):
    a = a.lower()
    a = a.strip()+".db"
    return a

def seleccion():
    seleccion = int(input("1. Crear Base de Datos\n2. Eliminar Base de Datos\n3. Usar una base de datos\n4. Modificar Base de Datos\n"))
    if seleccion == 1:
        nombre_db = str(input("Nombre de la base de datos a crear:\n"))
        nombre_db = limpiar_nombre(nombre_db)
        conn = sqlite3.connect(f"subcarpeta/{nombre_db}")
        conn.commit()
        conn.close()
    else:
        if seleccion == 2:
            nombre_db = input("Nombre de la base de datos a eliminar:\n")
            nombre_db = limpiar_nombre(nombre_db)
            os.remove(f"subcarpeta/{nombre_db}")

seleccion()
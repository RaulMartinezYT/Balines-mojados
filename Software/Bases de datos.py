import sqlite3, os

#  Esta funcion recibe un parametro que va a ser el nombre de la base de datos y devolverá el nombre "limpio" para prevenir errores de tipografia.
# El parametro es un str al entrar y salir, se lo escribe a minuscula, se le remplazan los "-" con "_" y los espacios en blanco por "_".

def limpiar_nombre(a):
    a = a.lower()
    a = a.strip()+".db"
    a = a.replace(" ", "_")
    a = a.replace("-", "_")
    return a

# Este metodo se utiliza para la creacion de bases de datos, no es necesario pasarle ningun parametro.
# Le solicitamos al usuario el nombre de la base de datos a crear, una vez lo tenemos lo "limpiamos", una vez terminado le asignamos el nombre limpio al archivo .db creado, nos conectamos a esa base de datos

def crear_db():
    nombre_db = str(input("Nombre de la base de datos a crear:\n"))
    nombre_db = limpiar_nombre(nombre_db)
    conn = sqlite3.connect(f"{nombre_db}")
    conn.commit()
    conn.close()

def eliminar_db():
    nombre_db = input("Nombre de la base de datos a eliminar:\n")
    nombre_db = limpiar_nombre(nombre_db)
    os.remove(f"{nombre_db}")

def usar_db():
    nombre_db = input("Nombre de la base de datos a usar:\n")
    nombre_db = limpiar_nombre(nombre_db)
    try:
        if open(nombre_db):
            print("archivo encontrado")
        
        else:
            print("archivo no encontrado")

    except FileNotFoundError:
        print(f"Error archivo no encontrado")

def seleccion():
    seleccion = int(input("1. Crear Base de Datos\n2. Eliminar Base de Datos\n3. Usar una base de datos\n4. Modificar Base de Datos\n"))
    if seleccion == 1:
        crear_db()
    if seleccion == 2:
        eliminar_db()
    if seleccion == 3:
        usar_db()

while True:
    seleccion()
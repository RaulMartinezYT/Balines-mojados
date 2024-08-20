import sqlite3, os
from datetime import datetime

# Esta funcion recibe un parametro que va a ser el nombre de la base de datos y devolverá el nombre "limpio" para prevenir errores de tipografia.
# El parametro es un str al entrar y salir, se lo escribe a minuscula, se le remplazan los "-" con "_" y los espacios en blanco por "_".
def limpiar_str(a):
    a = a.lower()
    a = a.strip() + ".db"
    a = a.replace(" ", "_")
    a = a.replace("-", "_")
    return a

# Este metodo se utiliza para la creacion de bases de datos, es necesario pasarle de parametro el nombre de la base de datos.
# Le solicitamos al usuario el nombre de la base de datos a crear, una vez lo tenemos lo "limpiamos", una vez limpiado el nombre, chequeamos que exista ese archivo.
# Si el archivo existe se lo haremos saber al usuario y queda en el si lo remplaza (se eliminará el archivo existente y se creará el nuevo)
# Si el archivo no existe se crea y listo
def crear_db(a):
    try:
        if open(f"db/{a}"):
            seleccion = str(input("La base de datos ya existe.\n¿Desea remplazarla? y/n\n"))
            limpiar_str(seleccion)
            if seleccion != "y" and seleccion != "n":
                print("Seleccion incorrecta")
            else:
                if seleccion == "y":
                    os.remove(f"db/{a}")
                    with open(f"db/{a}", 'w+') as file:
                        file.write( str(datetime.now()) )
                else:
                    print("No se remplazo la base de datos")



    except FileNotFoundError:
        try:
            with open(f"db/{a}", 'w+') as file:
                file.write( str(datetime.now()) )

        except Exception as e:
            print(f'No fue posible crear el archivo {e}')
    

# Este metodo se encarga de eliminar archivos
def eliminar_db():
    nombre_db = input("Nombre de la base de datos a eliminar:\n")
    nombre_db = limpiar_str(nombre_db)
    try:
        os.remove(f"db/{nombre_db}")

    except FileNotFoundError:
        print("El archivo no existe")
    

def usar_db():
    nombre_db = input("Nombre de la base de datos a usar:\n")
    nombre_db = limpiar_str(nombre_db)
    try:
        if open(f"db/{nombre_db}"):
            print("archivo encontrado")
        
        else:
            print("archivo no encontrado")

    except FileNotFoundError:
        print(f"Error archivo no encontrado")

# Funcion principal del programa, esta funcion se encarga de saber que quiere realizar el usuario, en este caso el empleado que está utilizando el programa
def seleccion():
    seleccion = int(input("1. Crear Base de Datos\n2. Eliminar Base de Datos\n3. Usar una base de datos\n4. Modificar Base de Datos\n"))
    
#    if seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion != 4:
#        print("Opcion incorrecta")
#        seleccion()

    if seleccion == 1:
        nombre_db = str(input("Nombre de la base de datos a crear:\n"))
        nombre_db = limpiar_str(nombre_db)
        crear_db(nombre_db)
    
    if seleccion == 2:
        eliminar_db()
    
    if seleccion == 3:
        usar_db()

    if seleccion == 4:
        print("accion 4")

# Main:
while True:
    seleccion()
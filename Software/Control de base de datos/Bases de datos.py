import sqlite3, os,time

# Esta funcion recibe un parametro que va a ser el nombre de la base de datos y devolverá el nombre "limpio" para prevenir errores de tipografia.
# El parametro es un str al entrar y salir, se lo escribe a minuscula, se le remplazan los "-" con "_" y los espacios en blanco por "_".
def limpiar_str(a):
    a = a.lower()
    a = a.strip() + ".db"
    a = a.replace(" ", "_")
    a = a.replace("-", "_")
    return a

# Este metodo se utiliza para la creacion de bases de datos, es necesario pasarle de parametro el nombre de la base de datos.
# Chequeamos que exista ese archivo.
# Si el archivo existe se lo haremos saber al usuario y queda en el si lo remplaza (se eliminará el archivo existente y se creará el nuevo).
# Si el archivo no existe se crea y listo.
def crear_db(a):
    try:
        if open(f"db/{a}"):
            seleccion = str(input("La base de datos ya existe.\n+======================+\n| ¿Deseas remplazarla? |\n+=======+=======+======+\n        | Y / N |\n        +=======+\n"))
            limpiar_str(seleccion)
            if seleccion != "y" and seleccion != "n":
                print("+========================+\n| Seleccion incorrecta |\n+========================+\n")
            else:
                if seleccion == "y": 
                    os.remove(f"db/{a}")
                    with open(f"db/{a}", 'w+') as file:
                        file.close()
                    print("+====================+\n| Archivo remplazado |\n+====================+\n")

                else:
                    print("+=================================+\n| No se remplazo la base de datos |\n+=================================+\n")

    except FileNotFoundError:
        try:
            with open(f"db/{a}", 'w+') as file:
                file.close()
                print("+================+\n| Archivo creado |\n+================+\n")

        except Exception as e:
            print(f'[ No fue posible crear el archivo ( {e} ) ]\n')
    

# Este metodo se recibe el nombre de la base de datos deseada para ser eliminada.
def eliminar_db(a):
    try:
        os.remove(f"db/{a}")

    except FileNotFoundError:
        print("\n+=======================+\n| Archivo no encontrado |\n+=======================+\n")
    
# 
def conectar_db(a):
    try:
        if open(f"db/{a}"):
            print("+====================+\n| archivo encontrado |\n+====================+\n")
            conexion = sqlite3.connect(f"db/{a}")

    except FileNotFoundError:
        print("\n| Archivo no encontrado |\n  ")

# Funcion principal del programa, esta funcion se encarga de saber que quiere realizar el usuario, en este caso el empleado que está utilizando el programa
def seleccion():
    seleccion = int(input("+============================+\n| 1. Crear Base de Datos     |\n+============================+\n| 2. Modificar Base de Datos |\n+============================+\n| 3. Eliminar Base de Datos  |\n+============================+\n"))
    
    if seleccion != 1 and seleccion != 2 and seleccion != 3:
        print("+===================+\n| Opcion incorrecta |\n+===================+\n")

    if seleccion == 1:
        nombre_db = str(input("+=====================================+\n| Nombre de la base de datos a crear: |\n+=====================================+\n"))-
        nombre_db = limpiar_str(nombre_db)
        crear_db(nombre_db)
    
    if seleccion == 2:
        nombre_db = input("Nombre de la base de datos a usar:\n")
        nombre_db = limpiar_str(nombre_db)
        conectar_db(nombre_db)
    
    if seleccion == 3:
        nombre_db = input("Nombre de la base de datos a eliminar:\n")
        nombre_db = limpiar_str(nombre_db)
        eliminar_db(nombre_db)

# Main:
while True:
    seleccion()
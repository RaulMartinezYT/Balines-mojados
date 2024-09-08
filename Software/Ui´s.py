import os, datetime, sqlite3, tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import timedelta

# Ventana emergente de alerta.
def alerta(titulo_ventana, descripcion):
    messagebox.showwarning(titulo_ventana, descripcion)

# Ventana emergente de informacion.
def informacion(titulo_ventana, descripcion):
    messagebox.showinfo(titulo_ventana, descripcion)

# Ventana emergente de error.
def error(titulo_ventana, descripcion):
    messagebox.showerror(titulo_ventana, descripcion)

# Ventana emergente con una pregunta a responder con si o no, retorna True o False dependiendo la seleccion.
def pregunta_si_no(titulo_ventana, pregunta):
    respuesta = messagebox.askyesno(titulo_ventana, pregunta)
    if respuesta:
        return True
    else:
        return False

# Ventana emergente con una pregunta a responder con si o no, retorna True o False dependiendo la seleccion.
def reintentar_si_no(titulo_ventana, pregunta):
    respuesta = messagebox.askretrycancel(titulo_ventana, pregunta)
    if respuesta:
        return True
    else:
        return False


# Funcion para la creacion de la ventana de inicio de sesion.
# Recibe como atributos colores para la ventana, no es obligado pasarlos ya que tiene valores por defecto:
#
# Fondo_principal:  Color principal de fondo.
# Fondo_secundario: Color secundario de fondo, se utiliza para diferenciar secciones.
# Letras: Color de las letras.
# Marcos: Color de las lineas o marcos de secciones de la ventana.
# Boton_activo: Color que toma un boton al ser presionado.
def ventana_iniciar_sesion(fondo_principal = "#0F1035", fondo_secundario = "#365486", letras = "#7FC7D9", marcos = "#ffffff", fondo_boton_activo = "#ffffff", h1 = 60, h2 = 50, h3 = 40 , h4 =30, h5 = 20, h6 = 10):

    # Conectamos el software con la base de datos.
    conn = sqlite3.connect('Balines_mojados.db')

    # Declaramos el nombre del cursor, el cual se encarga de realizar las consultas a la base de datos.
    cursor = conn.cursor()
    
    # Funcion del boton de inicio de sesion, al ser presionado el boton realiza las siguientes acciones:
    def boton_presionado():

        # Recibe y guarda los datos en variables separadas, DNI y la clave.
        dni = Dni_entry.get()
        clave = Clave_entry.get()
        
        # Verifica si el campo de DNI se encuentra vacio a la hora de haber presionado el boton.
        # Si se encuentra vacia se abre una ventana emergente de ERROR la cual le informa al usuario que se encuentra vacio.
        if dni == "":
            error("Error DNI", "El campo de DNI se encuentra vacio.")
            confirmacion_dni = False

        # Si no se encuentra vacia:
        else:
            # Remplaza posibles puntos los remplaza por nada.
            dni.replace(".","")

            # Intenata lo siguiente:
            try:
                # Intenta pasar el str a int.
                dni = int(dni)
                
                # Saca el valor absoluto del numero (sacandole asi cualquier signo).
                dni = abs(dni)

                # Vuelve a pasar el valor a str para poder usar el metodo .len() y asi poder calcular el largo de la cadena de caracteres.
                dni = str(dni)
                
                # Si el largo del DNI es igual a 8 se confirma que es un DNI.
                if len(dni) == 8:
                    confirmacion_dni = True

                # Si el tamaño del DNI no es de 8 digitos.
                else:
                    confirmacion_dni = False

                    # Si el tamaño del DNI es menor a 8 digitos, se le informa que al personal que el DNI esta incompleto.
                    if len(dni) < 8:
                        error("Error DNI", "El DNI ingresado está incompleto.")

                    # Si el DNI es mayor a 8 digitos se le informa al personal que el DNI es mas largo de lo que deveria.
                    else:
                        error("Error DNI", "El DNI ingresado es demasiado largo.")

            # Si no se puede realizar el unico motivo que queda es que se trata a cerca de una ecepcion de tipo "ValueError".
            # Esta exepcion (en este caso ocurre) se ejecuta ya que no se pudo pasar el valor string a entero, ya que no eran unicamente numeros.
            # Si llegamos a esto se le hará saber el o la empleado/a que el DNI ingresado no es un DNI. 
            except ValueError:
                error("Error DNI", "El DNI ingresasdo no es un DNI.")
        
        # Verifica si el campo de la clave se encuentra vacio a la hora de haber presionado el boton.
        # Si se encuentra vacia se abre una ventana emergente de ERROR la cual le informa al usuario que se encuentra vacio.
        if clave == "":
            error("Alerta", "El campo de la clave se encuentra vacio.")
            confirmacion_dni = False

        # Si no se encuentra vacia:
        # No se confirma la clave
        else:
            confirmacion_clave = True

        # Si se confirma el dni y la clave (osea que pasaron todos los filtros anteriormente mencionado) pasaria lo siguiente:
        if confirmacion_dni == True and confirmacion_clave == True:
            
            # Se define la consulta a realizar para el login:
            consulta = f"SELECT * FROM personal WHERE dni = ? AND clave_acceso = ?;"

            # Se define los datos para pasarle a la consulta.
            datos = (dni, clave)

            # Una vez lo tenemos todo preparado realizamos la consulta con los datos incluidos.
            cursor.execute(consulta, datos)

            # Al realizar la consulta se obtiene una respuesta con la siguiente linea, esa respuesta se utiliza para confirmar el inicio de sesion.
            inicio_sesion = cursor.fetchall()

            # Crea la consulta para averiguar cual es el Id de la sucursal en la que trabaja el empleado.
            consulta_id = "SELECT id_sucursal FROM personal WHERE dni = ?;"
            
            # Datos necesarios para la consulta.
            datos_id = (dni,)

            # Ejecuta la consulta con la consulta y los valores de la consulta.
            cursor.execute(consulta_id, datos_id)

            # Creamos una variable en la que se va a guardar el resultado de la consulta, osea la respuesta de la consulta.
            a = cursor.fetchone()

            # Detecta si hay valor en la variable y si es asi:
            if a:                    
                # Guarda la reserva de la consulta en una variable la cual se pasa a la siguiente ventana.
                # Y extraemos el valor de la tupla.
                id_sucursal_personal = a[0]

            # Si la peticion (chequea si el DNI y la clave son iguales a las que estan guardadas en la base de datos) se confirma el personal y el inicio de sesion, permitiendo asi el ingreso al software.
            if inicio_sesion:
                informacion("Inicio de sesion", "Inicio de sesion completa.")
                ventana.destroy()
                ventana_reservas(dni, id_sucursal_personal, fondo_principal, letras, marcos, h1, h2, h3, h4, h5, h6)
            else:
                informacion("Inicio de sesion", "Error al intentar iniciar sesion.")

    # Creacion de la ventana.
    ventana = tk.Tk()
    
    # Guarda los valores de la pantalla en dos variables:
    # Ancho_pantall: Es el ancho de la pantalla.
    # Alto_pantalla: Es el alto de la pantalla.
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    

    # Esta linea de codigo se encarga de transformar los valores de la pantalla (Ancho y Alto de pantalla) a enteros (Numeros sin decimal) los cuales se utilizan para definir el tamaño de la ventana.
    # Al tener el ancho y el alto en enteros pasan por una cuenta matematica para que siempre mantengan la relacion 16:9.
    # Lo cual nos permite tener siempre una ventana con la misma relacion, unicamente para mantenerla responsive sin necesidad de que python lo intente y falle fatalmente.
    # Pasando a lo tecnico, agarra los valores anteriores de la pantalla (el ancho y largo, los cuales se dividen para que 9 valores de alto equivalgan a 16 de ancho, para tener siempre la misma relacion (16:9).
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)

    ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
    
    # Establecemos el minimo tamaño que podrá tener la ventana
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)

    # Especificamos las medidas iniciales de la ventana.
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")

    # Especificamos el color de fondo de pantalla.
    # Este valor es el atributo que se le pasa a la funcion que ya fue antes mencionada.
    ventana.config(background = fondo_principal)

    # Especificamos que la ventana inicie maximizada.
    ventana.state("zoomed")

    # Especificamos el nombre de la ventana.
    ventana.title("Balines Mojados")

    # Creamos lo que es un LabelFrame (Un marco decorativo):
    Marco = tk.LabelFrame(ventana,
                            border = 0,
                            bg = fondo_secundario,
                            highlightbackground = marcos,
                            highlightcolor = marcos,
                            highlightthickness = 5,
                            pady = 10)


    # Lo empaqueta con el metodo .pack() el cual se encarga de colocarlo dentro de la ventana.
    Marco.pack(pady = 20)

    # Creamos un texto de bienvenida, pero este se encuentra dentro del marco que respectivamente se encuentra dentro de la ventana y asi con cada objeto / elemento.
    Bienvenido = tk.Label(Marco,
                            background = fondo_secundario, 
                            fg = letras, 
                            font = ("Family",45),
                            text = "BIENVENIDO")

    # Lo empaquetamos y es colocado.
    Bienvenido.pack()

    # Creamos un texto para el "Dni del empleado".
    Nombre = tk.Label(Marco,
                            background = fondo_secundario,
                            fg = letras,
                            font = ("Family", 30),
                            padx = 150,
                            text = "DNI:")

    # Lo empaquetamos y es colocado.
    Nombre.pack(padx = 200, pady = (30,0))

    # Creamos un "INPUT" que en tkinter se lo conoce como "Entry" el cual nos va a ayudar a comunicar al personal con el software.
    # Este entry se encargará de recibir el nombre del personal utilizado para iniciar sesion.
    Dni_entry = tk.Entry(Marco,
                            bg = fondo_secundario,
                            fg = letras,
                            border = 0,
                            font = ("Family", 25),
                            highlightthickness = 5,
                            highlightcolor = marcos,
                            highlightbackground = marcos,
                            relief = "solid",
                            width = 25)

    # Lo empaquetamos y es colocado.
    Dni_entry.pack(pady=25)

    # Creamos un texto de "Codigo de seguridad".
    Clave = tk.Label(Marco,
                            background = fondo_secundario,
                            fg = letras,
                            font = ("Family", 30),
                            text = "Clave de seguridad:")

    # Lo empaquetamos y es colocado.
    Clave.pack(pady=(40,25))

    # Creamos otro entry el cual es para el codigo de seguridad del personal, cada uno cuenta con el suyo propio.
    Clave_entry = tk.Entry(Marco,
                            bg = fondo_secundario,
                            border = 0,
                            font = ("Family", 25),
                            fg = letras,
                            highlightthickness = 5,
                            highlightcolor = marcos,
                            highlightbackground = marcos,
                            relief = "solid",
                            show = "•",
                            width = 25)
    
    # Lo empaquetamos y es colocado.
    Clave_entry.pack(pady=25)
    
    # Creamos un LabelFrame por estetica al botón.
    Marco_boton = tk.LabelFrame(Marco,
                            bg = fondo_secundario,
                            border = 0,
                            highlightthickness = 5,
                            highlightcolor = marcos,
                            highlightbackground = marcos)
    
    # Lo empaquetamos y es colocado.
    Marco_boton.pack(pady = (40,100))

    # Creacion del boton para verificar los datos colocados.
    Aceptar = tk.Button(Marco_boton,
                            activebackground = fondo_boton_activo,
                            background = fondo_secundario,
                            border = 0,
                            command = boton_presionado,
                            fg = marcos,
                            font = ("Arial", 25),
                            highlightthickness = 5,
                            highlightcolor = "#ff0000",
                            highlightbackground = "#00ff00",
                            relief = "solid",
                            text = "Iniciar sesión",
                            width = 25)
    
    # Lo empaquetamos y es colocado.
    Aceptar.pack()
    ventana.mainloop()


def ventana_reservas(dni_personal = None, id_sucursal_personal = None, fondo_principal = "#0F1035", fondo_secundario = "#365486", letras = "#7FC7D9", marcos = "#ffffff", fondo_boton_activo = "#ffffff", h1 = 60, h2 = 50, h3 = 40 , h4 =30, h5 = 20, h6 = 10):
    
    def nombre_dia(numero_dia):
        dias_de_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        return dias_de_semana[numero_dia]

    # Funcion que no permite a nadie ingresar a la ventana de reservas sin un dni o un
    if dni_personal == None or id_sucursal_personal == None:
        error("ERROR CATASTROFICO", "No deberias haber podido ingresar aqui")
        return error
    else:
        # Conectamos el software con la base de datos.
        conn = sqlite3.connect('Balines_mojados.db')

        # Declaramos el nombre del cursor, el cual se encarga de realizar las consultas a la base de datos.
        cursor = conn.cursor()

        consulta = f"SELECT * FROM personal WHERE dni = ? AND id_sucursal = ?;"
        datos = (dni_personal, id_sucursal_personal)
        cursor.execute(consulta, datos)

        datos_correctos = cursor.fetchall()

        if datos_correctos:
                informacion("Esta bien","OK")
        else:
            informacion("Error en la base de datos", "No se encuentra en la base de datos.")
            return error
            pass
    
    # Conectamos el software con la base de datos.
    conn = sqlite3.connect('Balines_mojados.db')

    # Declaramos el nombre del cursor, el cual se encarga de realizar las consultas a la base de datos.
    cursor = conn.cursor()

    # Creacion de la ventana.
    ventana = tk.Tk()
    
    # Guarda los valores de la pantalla en dos variables:
    # Ancho_pantall: Es el ancho de la pantalla.
    # Alto_pantalla: Es el alto de la pantalla.
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    
    # Esta linea de codigo se encarga de transformar los valores de la pantalla (Ancho y Alto de pantalla) a enteros (Numeros sin decimal) los cuales se utilizan para definir el tamaño de la ventana.
    # Al tener el ancho y el alto en enteros pasan por una cuenta matematica para que siempre mantengan la relacion 16:9.
    # Lo cual nos permite tener siempre una ventana con la misma relacion, unicamente para mantenerla responsive sin necesidad de que python lo intente y falle fatalmente.
    # Pasando a lo tecnico, agarra los valores anteriores de la pantalla (el ancho y largo, los cuales se dividen para que 9 valores de alto equivalgan a 16 de ancho, para tener siempre la misma relacion (16:9).
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)

    ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
    
    # Establecemos el minimo tamaño que podrá tener la ventana
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)

    # Especificamos las medidas iniciales de la ventana.
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")

    # Especificamos el color de fondo de pantalla.
    # Este valor es el atributo que se le pasa a la funcion que ya fue antes mencionada.
    ventana.config(background = fondo_principal)

    # Especificamos el nombre de la ventana.
    ventana.title("Balines Mojados")

    # ===================================== FRAME 1 ======================================== #
    # Configurar la cuadrícula de la ventana principal para la columna 0.
    ventana.columnconfigure(0, weight = 1)

    # Configurar la cuadrícula de la ventana principal para la columna 1.
    ventana.columnconfigure(1, weight = 100)

    # Configurar la cuadrícula de la ventana principal para la fila 0.
    ventana.rowconfigure(0, weight = 1)

    # Crear el frame de los botones y lo coloca en la celda (columna 0, fila 0) de la ventana principal.
    reservas_botones = tk.Frame(ventana, bg = fondo_principal)
    reservas_botones.grid(column = 0, row = 0, sticky = "NSEW")

    reservas_botones.columnconfigure(0, weight = 1)

    # Crear el segundo frame y lo coloca en la celda (columna 1, fila 0).
    espacio_reservas_visuales = tk.Frame(ventana, bg = fondo_secundario)
    espacio_reservas_visuales.grid(column = 1, row = 0, sticky = "NSEW")


    Marco_boton_nueva_reserva = tk.LabelFrame(reservas_botones,
                            bg = fondo_secundario,
                            border = 0,
                            highlightthickness = 2,
                            highlightcolor = marcos,
                            highlightbackground = marcos)
    Marco_boton_nueva_reserva.pack(padx = 5, pady = (5, 0))

    btn_crear_reserva = tk.Button(Marco_boton_nueva_reserva,
                            text = "NUEVA\n RESERVA ",
                            font = ("Arial", 15),
                            bg = fondo_secundario,
                            fg = letras,
                            border = 0,
                            activebackground = fondo_boton_activo,
                            activeforeground = fondo_boton_activo)
    btn_crear_reserva.pack()



    Marco_boton_editar = tk.LabelFrame(reservas_botones,
                            bg = fondo_secundario,
                            border = 0,
                            highlightthickness = 2,
                            highlightcolor = marcos,
                            highlightbackground = marcos)
    Marco_boton_editar.pack(padx = 5, pady = (5, 0))

    btn_editar_reserva = tk.Button(Marco_boton_editar,
                            text = "EDITAR\n RESERVA ",
                            font = ("Arial", 15),
                            bg = fondo_secundario,
                            fg = letras,
                            border = 0,
                            activebackground = fondo_boton_activo,
                            activeforeground = fondo_boton_activo)
    btn_editar_reserva.pack()



    Marco_boton_eliminar = tk.LabelFrame(reservas_botones,
                            bg = fondo_secundario,
                            border = 0,
                            highlightthickness = 2,
                            highlightcolor = marcos,
                            highlightbackground = marcos)
    Marco_boton_eliminar.pack(padx = 5, pady = (5, 0))

    btn_eliminar_reserva = tk.Button(Marco_boton_eliminar,
                            text = "ELIMINAR\n RESERVA ",
                            font = ("Arial", 15),
                            bg = fondo_secundario,
                            fg = letras,
                            border = 0,
                            activebackground = fondo_boton_activo,
                            activeforeground = fondo_boton_activo)
    btn_eliminar_reserva.pack()



    Marco_boton_cambio_sucursal = tk.LabelFrame(reservas_botones,
                            bg = fondo_secundario,
                            border = 0,
                            highlightthickness = 2,
                            highlightcolor = marcos,
                            highlightbackground = marcos)
    Marco_boton_cambio_sucursal.pack(padx = 5, pady = (0, 5), side="bottom")

    btn_cambio_sucursal = tk.Button(Marco_boton_cambio_sucursal,
                            text = "CAMBIAR\nSUCURSAL",
                            font = ("Arial", 14),
                            bg = fondo_secundario,
                            fg = letras,
                            border = 0,
                            activebackground = fondo_boton_activo,
                            activeforeground = fondo_boton_activo)
    btn_cambio_sucursal.pack()

    # ===================================== FRAME 2 ======================================== #
    # Crear el canvas y agregarlo al frame
    canvas = tk.Canvas(espacio_reservas_visuales, background = fondo_secundario)
    canvas.pack(side='top', fill='both', expand=True)

    # Crear la scrollbar horizontal y agregarla al frame
    scrollbar = ttk.Scrollbar(espacio_reservas_visuales, orient='horizontal', command=canvas.xview)
    scrollbar.pack(side='bottom', fill='x')

    # Configurar el canvas para usar la scrollbar horizontal
    canvas.config(xscrollcommand=scrollbar.set)

    # Usar "<Configure>" para actualizar el scrollregion
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    # Crear un frame dentro del canvas
    reservas_visuales = tk.Frame(canvas, bg = fondo_secundario)

    # Crear una ventana dentro del canvas para colocar el frame2
    canvas.create_window((0, 0), window=reservas_visuales, anchor="nw")

    for columnas in range(75):
        reservas_visuales.columnconfigure(columnas, weight = 1)
        
    
    for filas in range(10):
        reservas_visuales.rowconfigure(filas, weight = 1)

    fecha_hoy = datetime.datetime.now().date()

    fecha = [
            datetime.datetime.now().date(),
            fecha_hoy + timedelta(days = 1),
            fecha_hoy + timedelta(days = 2),
            fecha_hoy + timedelta(days = 3),
            fecha_hoy + timedelta(days = 4),
            fecha_hoy + timedelta(days = 5),
            fecha_hoy + timedelta(days = 6),
            fecha_hoy + timedelta(days = 7),
            fecha_hoy + timedelta(days = 8),
            fecha_hoy + timedelta(days = 9),
            ]

    dia =   [
            nombre_dia(fecha[0].weekday()),
            nombre_dia(fecha[1].weekday()),
            nombre_dia(fecha[2].weekday()),
            nombre_dia(fecha[3].weekday()),
            nombre_dia(fecha[4].weekday()),
            nombre_dia(fecha[5].weekday()),
            nombre_dia(fecha[6].weekday()),
            nombre_dia(fecha[7].weekday()),
            nombre_dia(fecha[8].weekday()),
            nombre_dia(fecha[9].weekday()),
            ]

    tabla = [
            ["",     "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[0]}\n{fecha[0]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[1]}\n{fecha[1]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[2]}\n{fecha[2]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[3]}\n{fecha[3]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[4]}\n{fecha[4]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[5]}\n{fecha[5]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[6]}\n{fecha[6]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[7]}\n{fecha[7]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[8]}\n{fecha[8]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ],
            [f"{dia[9]}\n{fecha[9]}", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00" ]
            ]
    
    def crear_tabla(reservas_visuales, tabla):
        for i, fila in enumerate(tabla):
            for j, valor in enumerate(fila):
                if valor != "":
                    label = tk.Label(reservas_visuales, text=valor, borderwidth=0, relief="solid", padx=5, pady=5, fg= letras, background= fondo_secundario, highlightthickness = 2, highlightcolor = marcos, highlightbackground = marcos)
                    label.grid(row=i, column=j, sticky="nsew")

    # Configura el tamaño de las columnas y filas
    def configurar_grid(reservas_visuales, numero_filas, numero_columnas):
        for filas in range(numero_filas):
            reservas_visuales.grid_rowconfigure(filas, weight=1)
            for columnas in range(numero_columnas):
                reservas_visuales.grid_columnconfigure(columnas, weight=1)
    
    filas = len(tabla)
    columnas = len(tabla[0])
    configurar_grid(reservas_visuales, filas, columnas)
    crear_tabla(reservas_visuales, tabla)

    ventana.mainloop()

ventana_reservas(51398854, 1)
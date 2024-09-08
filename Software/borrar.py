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
            # informacion("Error en la base de datos", "No se encuentra en la base de datos.")
            # return error
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
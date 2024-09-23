import datetime, sqlite3, time, tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import timedelta
from tkinter import colorchooser


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

def ventana_reservas(dni_personal = None, id_sucursal_personal = None, id_cancha = None, color_principal = "#0F1035", color_secundario = "#365486", color_letras = "#7FC7D9", tipografia = "Arial", color_marcos = "#ffffff", color_boton_activo = "#ffffff", h1 = 45, h2 = 40, h3 = 35, h4 = 30, h5 = 25, h6 = 20, h7 = 15):
    
    if dni_personal == None and id_sucursal_personal == None and id_cancha == None:
        error("ERROR CATASTROFICO", "No deberias haber podido ingresar aqui.")
        return error
    elif dni_personal == None or id_sucursal_personal == None or id_cancha == None:
        error("ERROR DATOS", "Datos del personal incompleto, inicie sesion nuevamente.")

    else:
        conn = sqlite3.connect("Balines_mojados.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        consulta = f"SELECT * FROM personal WHERE dni = ? AND id_sucursal = ?;"
        datos = (dni_personal, id_sucursal_personal)
        cursor.execute(consulta, datos)
        datos_correctos = cursor.fetchall()
        conn.close()

        if datos_correctos:
                conn = sqlite3.connect("Balines_mojados.db")
                cursor = conn.cursor()
                ventana = tk.Tk()
                ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
                ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
                alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)
                ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
                ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)
                ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
                ventana.config(background = color_principal)
                ventana.title("Balines Mojados - Reservas")
        else:
            return error        
    
    # ===================================== FRAME 1 ======================================== #

    #for reserva in reservas:
    #            id_reserva             = reserva[0]
    #            dni_personal_reserva   = reserva[1]
    #          # Id_cancha_reserva      = reserva[2]
    #            dni_cliente            = reserva[3]
    #            fecha_reserva          = reserva[4]
    #            hora_inicio_reserva    = reserva[5]
    #            hora_fin_reserva       = reserva[6]
    #            estado_reserva         = reserva[7]

    ventana.grid_columnconfigure(0, weight = 1)
    ventana.grid_columnconfigure(1, weight = 1000)
    ventana.grid_rowconfigure(0, weight = 1)

    frame_botones    = tk.Frame(ventana, background = color_secundario, highlightthickness = 1, highlightbackground = color_marcos)
    frame_reservas   = tk.Frame(ventana, background = color_secundario, highlightthickness = 1, highlightbackground = color_marcos)
    
    frame_botones.grid(   column = 0, row = 0, padx = (10, 0), pady = 10, sticky = "nsew")
    frame_reservas.grid(  column = 1, row = 0, padx = 10, pady = 10, sticky = "nsew")

    Marco_nueva_reserva     = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    crear_reserva           = tk.Button(Marco_nueva_reserva, text = "NUEVA\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_detalles_reserva  = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    detalles_reserva        = tk.Button(Marco_detalles_reserva, text = "DETALLES\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_editar            = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    editar_reserva          = tk.Button(Marco_editar, text = "EDITAR\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_eliminar          = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    eliminar_reserva        = tk.Button(Marco_eliminar, text = "ELIMINAR\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_cambio_sucursal   = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    cambio_sucursal         = tk.Button(Marco_cambio_sucursal, text = "CAMBIAR\nSUCURSAL", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)

    Marco_nueva_reserva.pack(pady = (5, 0), padx = 5)
    crear_reserva.pack()
    Marco_detalles_reserva.pack(pady = (5, 0), padx = 5)
    detalles_reserva.pack()
    Marco_editar.pack(pady = (5, 0), padx = 5)
    editar_reserva.pack()
    Marco_eliminar.pack(pady = (5, 0), padx = 5)
    eliminar_reserva.pack()
    Marco_cambio_sucursal.pack(pady = (0, 5), padx = 5, side = "bottom")
    cambio_sucursal.pack()

    # ===================================== FRAME 2 ======================================== #
    def nombre_dia(numero_dia):
        dias_de_semana = ["   Lunes   ","  Martes  "," Miercoles","  Jueves  "," Viernes  ","  Sabado  "," Domingo "]
        return dias_de_semana[numero_dia]
    
    horas    = ["FECHA / HORA","08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00"]
    fechas   = []
    dias     = []
    reservas = []

    fecha_hoy = datetime.datetime.now().date()

    # Crea la fecha y el numero del dia.
    for x in range(31):
        fechas.append(fecha_hoy + timedelta(days = x))
        dias.append(nombre_dia(fechas[x].weekday()))
        fechas[x]   = str(fechas[x].strftime("%d/%m/%Y"))
        dias[x]     = str(dias[x])
    
    def obtener_reservas():
        cursor.execute("SELECT * FROM reservas WHERE id_cancha = ?;", (id_cancha,))
        reservas = cursor.fetchall()
        return reservas

    # Inserta en la tabla la fecha y el dia.
    def iniciar_tabla():
        for x in range(31):
            dia      = dias[x]
            fecha    = fechas[x]
            tabla.insert("", "end", values = (f"{dia}\n{fecha}", ""))

    def insertar_reservas():
        for reserva in reservas:
                dni_cliente            = reserva[3]
                fecha_reserva          = reserva[4]
                hora_inicio_reserva    = reserva[5]
                hora_fin_reserva       = reserva[6]
                estado_reserva         = reserva[7]
                
                conn = sqlite3.connect("Balines_mojados.db")
                cursor = conn.cursor()
                cursor.execute("PRAGMA foreign_keys = ON;")
                cursor.execute("SELECT nombre, apellido FROM clientes WHERE dni = ?;", (dni_cliente,))
                datos_cliente = cursor.fetchall()

                if datos_cliente:
                    nombre_cliente = datos_cliente[0][0]
                    apellido_cliente = datos_cliente[0][1]
                conn.close()

                try:
                    columna_inicio = horas.index(hora_inicio_reserva)
                    columna_final = horas.index(hora_fin_reserva)
                    fila = fechas.index(fecha_reserva)

                except ValueError:
                    columna_inicio = None
                    columna_final  = None
                    fila           = None

                if fila != None and columna_inicio != None and columna_final != None:
                    dia    = dias[fila]
                    datos  = [f"{dia}\n{fecha_reserva}"]
                    
                    for x in range(74):
                        if x != 0:
                            if x == columna_inicio:
                                datos.append(f"Inicio de reserva\n{nombre_cliente}\n{apellido_cliente}\n{estado_reserva}")
                            elif x == columna_final:
                                datos.append(f"Final de reserva\n{nombre_cliente}\n{apellido_cliente}\n{estado_reserva}")
                            elif ((x > columna_inicio) and (x < columna_final)):
                                datos.append("====")
                            else:
                                datos.append("")
                            item_id = tabla.get_children()[fila]
                            tabla.item(item_id, values = datos)
                    
                elif fila == None or columna_inicio == None or columna_final == None:
                    error("FALTA DATOS","TITULO")
                    pass
                
                else:
                    error("NC","TITULO")
                    pass

    # Con esta funcion al entregarle la fecha y la hora de la reserva, sacamos la fecha, la fila y la columna de la reserva la cual se utiliza para ingresarlo en la tabla.
    # La fila representa la fecha de la reserva.
    # La columna la hora inicial y final de la reserva.
    

    # ===================================== MAIN ======================================== #

    style = ttk.Style()
    style.configure("Treeview", rowheight = 70)
    
    tabla = ttk.Treeview(frame_reservas, columns = horas, show = 'headings')

    for hora in horas:
        tabla.heading(hora, text = hora, anchor = "center")
        tabla.column(hora, width = 100, anchor = "center")

    tabla.pack(fill = 'both', expand = True)
    tabla.bind("<Button-1>", lambda e: "break")

    scrollbar = ttk.Scrollbar(frame_reservas, orient = 'horizontal', command = tabla.xview)
    scrollbar.pack(side = 'bottom', fill = 'x')
    tabla.config(xscrollcommand = scrollbar.set)


    iniciar_tabla()
    reservas = obtener_reservas()
    insertar_reservas()
    
    conn.close()
    ventana.mainloop()

ventana_reservas(51398854, 1, 1)
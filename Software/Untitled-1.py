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
    
    # Chequea si los datos son correctos.
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
                
                ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)
                ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
                ventana.config(background = color_principal)
                ventana.title("Balines Mojados - Reservas")
        else:
            return error
    # ===================================== FRAME 1 ======================================== #



    # ===================================== FRAME 2 ======================================== #
    horas    = ["FECHA / HORA","08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00"]
    fechas   = []
    dias     = []
    reservas = []

    def obtener_reservas():
        conn = sqlite3.connect("Balines_mojados.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("SELECT * FROM reservas WHERE id_cancha = ?;", (id_cancha,))
        reservas = cursor.fetchall()
        return reservas
    

    def nombre_dia(numero_dia):
        dias_de_semana = ["   Lunes   ","  Martes  "," Miercoles","  Jueves  "," Viernes  ","  Sabado  "," Domingo "]
        return dias_de_semana[numero_dia]
    
    fecha_hoy = datetime.datetime.now().date()
    # Crea la fecha y el numero del dia.
    for x in range(31):
        fechas.append(fecha_hoy + timedelta(days = x))
        dias.append(nombre_dia(fechas[x].weekday()))
        fechas[x]   = str(fechas[x].strftime("%d/%m/%Y"))
        dias[x]     = str(dias[x])

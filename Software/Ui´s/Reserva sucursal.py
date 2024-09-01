import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def Reserva(fondo = "#0F1035", fondo_inicio = "#365486", letras = "#7FC7D9", marcos = "#ffffff", Boton_activo ="#ffffff"):

    def Guardar_datos():
        fecha_reserva = fecha_entrante.get()
        hora_reserva = hora_entrante.get()
        minutos_reserva = minutos_entrante.get()
        print(f"La hora de la reserva es {hora_reserva} y {minutos_reserva} del {fecha_reserva}")

    ventana = tk.Tk()
    # Determina el ancho y alto del equipo creando asi una ventana de un cuarto a relacion de estas medidas
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    # Mantiene la relacion 16:9 del softwere
    cuarto_ancho_pantalla, cuarto_alto_pantalla = int(((alto_pantalla / 1.4) * 16) / 9), int(((ancho_pantalla / 1.4) * 9) / 16)
    # Minimo tamaño de la ventana ( 1/4 del tamaño de la pantalla con una relacion 16:9)
    #ventana.minsize(cuarto_ancho_pantalla, cuarto_alto_pantalla)
    # Otorga los valores de la ventana
    ventana.geometry(f"{cuarto_ancho_pantalla}x{cuarto_alto_pantalla}")
    # Color del fondo de la ventana posible variante(#162447)
    ventana.config(background = f"{fondo}")
    ventana.title("Balines Mojados")

    horas = [
            "08","09","10",
            "11","12","13",
            "14","15","16",
            "17","18","19",
            "20","21","22",
            "23","00","01"
            ]

    minutos = ["00","15","30","45"]

    fecha_entrante = DateEntry(ventana, width=12, background='green', foreground='black', borderwidth=5)
    fecha_entrante.pack()

    hora_entrante = ttk.Combobox(ventana, values = horas)
    hora_entrante.set("Hora")
    hora_entrante.pack()

    minutos_entrante = ttk.Combobox(ventana, values = minutos)
    minutos_entrante.set("Minutos")
    minutos_entrante.pack()

    boton = tk.Button(ventana, text = "Guardar datos", command = Guardar_datos)
    boton.pack()

    ventana.mainloop()

Reserva()
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def reserva(fondo = "#0F1035", fondo_inicio = "#365486", letras = "#7FC7D9", marcos = "#ffffff", Boton_activo ="#ffffff"):
    def boton_presionado():
        print("Datos guardados")
        fecha = date_entry.get()
        hora2 = hora.get()
        print(fecha, hora2)

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

    date_entry = DateEntry(ventana, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.pack(pady=5)

    opciones = ["08:00","08:15","08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45","23:00","23:15","23:30","23:45","00:00","00:15","00:30","00:45","01:00"]
    hora = ttk.Combobox(ventana, values = opciones)
    hora.set("Hora")
    hora.pack()

    boton = tk.Button(ventana,text="Guardar datos",command=boton_presionado)
    boton.pack()

    ventana.mainloop()

reserva()
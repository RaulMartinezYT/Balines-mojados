import tkinter as tk
import os

def ui_sucursales(fondo = "#18141d", letras = "#f0f0f0", marcos = "#f0f0f0"):
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
    
    Sucursales = tk.Label(ventana, text="SUCURSALES",font=("Family",20),border=4,relief="solid",highlightthickness = 5,highlightcolor = f"{marcos}", highlightbackground = f"{marcos}",background=f"{fondo}",fg=f"{letras}")
    Sucursales.pack(pady = 5)

    Sucursal1 = tk.Frame(ventana, bg="blue", width=400, height=500)
    Sucursal1.pack(pady=5)

    botons1 = tk.Button(Sucursal1, text="Sucursal1", padx=5,pady=5)
    botons1.pack()

    Sucursal2 = tk.Frame(ventana, bg="blue", width=100, height=50)
    Sucursal2.pack(pady=5)

    Sucursal3 = tk.Frame(ventana, bg="yellow", width=100, height=50)
    Sucursal3.pack(pady=5)

    Sucursal4 = tk.Frame(ventana, bg="yellow", width=100, height=50)
    Sucursal4.pack(pady=5)

    Sucursal5 = tk.Frame(ventana, bg="yellow", width=100, height=50)
    Sucursal5.pack(pady=5)

    Sucursal6 = tk.Frame(ventana, bg="blue", width=100, height=50)
    Sucursal6.pack(pady=5)

    Sucursal7 = tk.Frame(ventana, bg="blue", width=100, height=50)
    Sucursal7.pack(pady=5)

    ventana.mainloop()

ui_sucursales()
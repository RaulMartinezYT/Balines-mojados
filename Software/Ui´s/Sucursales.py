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
    Sucursales.pack()

    Sucursal_1 = tk.LabelFrame(ventana, bg="blue")
    Sucursal_1.pack()

    boton_1 = tk.Button(Sucursal_1, text="Sucursal 1", padx=5,pady=5)
    boton_1.pack()

    Sucursal_2 = tk.LabelFrame(ventana, bg="red")
    Sucursal_2.pack()

    botom_2 = tk.Label(Sucursal_2,text="Hola")
    botom_2.pack()

    ventana.mainloop()

ui_sucursales()
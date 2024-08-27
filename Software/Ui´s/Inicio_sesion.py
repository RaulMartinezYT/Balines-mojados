import tkinter as tk
ventana = tk.Tk()

# Determina el ancho y alto del equipo creando asi una ventana de un cuarto a relacion de estas medidas
ancho_pantalla, alto_pantalla = (ventana.winfo_screenwidth()) / 1.4, ventana.winfo_screenheight() / 1.4

# Mantiene la relacion 16:9 del softwere
ancho_pantalla, alto_pantalla = (alto_pantalla * 16) / 9, (ancho_pantalla * 9) / 16

# Convierte los valores de ancho y alto a numeros enteros
ancho_pantalla, alto_pantalla = int(ancho_pantalla), int(alto_pantalla)

# Minimo tamaño de la ventana ( 1/4 del tamaño de la pantalla con una relacion 16:9)
ventana.minsize(ancho_pantalla, alto_pantalla)

# Otorga los valores de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Color del fondo de la ventana posible variante(#18141d)
ventana.config(background = "#162447")

Marco = tk.LabelFrame(ventana, fg = "#D1D1D1", pady = 10, bg = "#162447", border = 4, relief = "ridge")

Bienvenido = tk.Label(Marco, text = "BIENVENIDO", fg = "#D1D1D1", background = "#162447", font = ("Family",45))
Nombre = tk.Label(Marco, text = "Nombre de empleado", fg = "#D1D1D1", background = "#162447", font = ("Family",30))
Nombre_entrada = tk.Entry(Marco, width = 25,fg = "#D1D1D1", bg = "#162447", font = ("Family",25), border = 2, relief = "ridge")
Codigo = tk.Label(Marco, text = "Codigo de seguridad", fg = "#D1D1D1", background = "#162447", font = ("Family",30))
Codigo_entrada = tk.Entry(Marco, width = 25,fg = "#D1D1D1", bg = "#162447", font = ("Family",25), border = 2, relief = "ridge", show = "*")
Datos_incorrectos = tk.Label(Marco, text = "NOMBRE O CODIGO INCORRECTO", fg = "#D1D1D1", bg = "#162447", font = ("Family",25), border = 2, relief = "ridge")
Datos_faltantes = tk.Label(Marco, text = "INGRESE NOMBRE Y CODIGO DE SEGURIDAD", fg = "#D1D1D1", bg = "#162447", font = ("Family",25), border = 2, relief = "ridge")
Aceptar = tk.Button(Marco, text = "Iniciar sesion", fg = "#D1D1D1",width= 25, background = "#162447", font = ("Family",25), border = 2, relief = "ridge")

# Al añadir relleno (padding) tener en cuenta:
# Pady = (10,20) 10 de relleno a la izquierda y 20 a la derecha
# Padx = (10,20) 10 de relleno arriba y 20 abajo
#
# Forma para hacerle saber al usuario que esta incorrto la informacion
# a = input("Hola:\n")
# if a == "a":
#     Datos_incorrectos.pack()

Marco.pack(pady = 20)
Bienvenido.pack(padx = 200, pady = (30,0))
Nombre.pack(pady=(40,25), padx=100)
Nombre_entrada.pack(pady=25)
Codigo.pack(pady=(40,25))
Codigo_entrada.pack(pady=25)
Aceptar.pack(pady = (40,100))
ventana.mainloop()
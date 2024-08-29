import tkinter as tk

def ui_iniciar_sesion(fondo = "#0F1035", fondo_inicio = "#365486", letras = "#7FC7D9", marcos = "#ffffff", Boton_activo ="#ffffff"):

    def boton_presionado():
        print(f"Presionado")

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

    # Crea e inicializa los elementos de la UI:
    Marco = tk.LabelFrame(ventana,
                            bg = f"{fondo_inicio}",
                            highlightthickness = 5,
                            highlightcolor = f"{marcos}",
                            highlightbackground = f"{marcos}",
                            pady = 10,
                            border=0)

    Marco.pack(pady = 20)

    Bienvenido = tk.Label(Marco,
                            background = f"{fondo_inicio}", 
                            fg = f"{letras}", 
                            font = ("Family",45),
                            text = "BIENVENIDO")

    Bienvenido.pack()

    Nombre = tk.Label(Marco,
                            background = f"{fondo_inicio}",
                            fg = f"{letras}",
                            font = ("Family", 30),
                            text = "Nombre de empleado")

    Nombre.pack(padx = 200, pady = (30,0))

    Nombre_entrada = tk.Entry(Marco,
                            bg = f"{fondo_inicio}",
                            border=0,
                            highlightthickness = 5,
                            highlightcolor = f"{marcos}",
                            highlightbackground = f"{marcos}",
                            font = ("Family", 25),
                            relief = "solid",
                            width = 25)

    Nombre_entrada.pack(pady=25)

    Codigo = tk.Label(Marco,
                            background = f"{fondo_inicio}",
                            fg = f"{letras}",
                            font = ("Family", 30),
                            text = "Codigo de seguridad")

    Codigo.pack(pady=(40,25))

    Codigo_entrada = tk.Entry(Marco,
                            bg = f"{fondo_inicio}",
                            border=0,
                            highlightthickness = 5,
                            highlightcolor = f"{marcos}",
                            highlightbackground = f"{marcos}",
                            font = ("Family", 25),
                            relief = "solid",
                            show = "•",
                            width = 25)

    Codigo_entrada.pack(pady=25)

    Datos_incorrectos = tk.Label(Marco,
                            background = f"{fondo_inicio}",
                            border = 2,
                            fg = f"{letras}",
                            font = ("Family", 10),
                            relief = "solid",
                            text = "NOMBRE O CODIGO INCORRECTO")

    Datos_faltantes = tk.Label(Marco,
                            background = f"{fondo_inicio}",
                            border = 2,
                            fg = f"{letras}",
                            font = ("Family", 10),
                            relief = "solid",
                            text = "INGRESE NOMBRE Y CODIGO DE SEGURIDAD")
    
    Marco_boton = tk.LabelFrame(Marco,
                            bg = f"{fondo_inicio}",
                            highlightthickness = 5,
                            highlightcolor = f"{marcos}",
                            highlightbackground = f"{marcos}",
                            border=0)
    
    Marco_boton.pack(pady = (40,100))

    Aceptar = tk.Button(
                            Marco_boton,
                            border=0,
                            background=fondo_inicio,
                            command=boton_presionado,
                            activebackground=Boton_activo,
                            highlightthickness=5,
                            highlightcolor="#ff0000",
                            highlightbackground="#00ff00",
                            fg=marcos,
                            font=("Arial", 25),
                            relief="solid",
                            text="Iniciar sesión",
                            width=25)

    Aceptar.pack()

    # Al añadir relleno (padding) tener en cuenta:
    # Pady = (10,20) 10 de relleno a la izquierda y 20 a la derecha
    # Padx = (10,20) 10 de relleno arriba y 20 abajo

    # Forma para hacerle saber al usuario que esta incorrto la informacion
    # a = input("Hola:\n")
    # if a == "a":
    # Datos_incorrectos.pack()

    ventana.mainloop()

ui_iniciar_sesion()
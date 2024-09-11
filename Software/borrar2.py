import tkinter as tk

ventana = tk.Tk()

# Función para mostrar el frame de la opción 1
def mostrar_frame(frame):
    # Ocultar todos los frames antes de mostrar el seleccionado
    for fr in [frame_btn1, frame_btn2, frame_btn3, frame_btn4]:
        fr.pack_forget()
    frame.pack(fill="both", expand=True)

# Función para ocultar los indicadores
def ocultar_indicadores():
    btn1_indicador.config(bg="#aaaaaa")
    btn2_indicador.config(bg="#aaaaaa")
    btn3_indicador.config(bg="#aaaaaa")
    btn4_indicador.config(bg="#aaaaaa")

# Función para cambiar el indicador y mostrar el frame correspondiente
def indicador(label, frame):
    ocultar_indicadores()
    label.config(bg="blue")  # Cambia el color del indicador seleccionado
    mostrar_frame(frame)  # Muestra el frame correspondiente

# Crear el frame de las opciones de la izquierda
opciones = tk.Frame(ventana, bg="#aaaaaa")

# Botón para la opción 1
btn1 = tk.Button(opciones, text="OPCION 1", bg="#aaaaaa", relief="flat", fg="blue", font=("Bold", 10),
                 command=lambda: indicador(btn1_indicador, frame_btn1))
btn1.place(x=10, y=50)

# Indicador para el botón 1
btn1_indicador = tk.Label(opciones, background="#aaaaaa")
btn1_indicador.place(x=3, y=50, height=38)

# Botón para la opción 2
btn2 = tk.Button(opciones, text="OPCION 2", bg="#aaaaaa", relief="flat", fg="blue", font=("Bold", 10),
                 command=lambda: indicador(btn2_indicador, frame_btn2))
btn2.place(x=10, y=100)

# Indicador para el botón 2
btn2_indicador = tk.Label(opciones, background="#aaaaaa")
btn2_indicador.place(x=3, y=100, height=38)

# Botón para la opción 3
btn3 = tk.Button(opciones, text="OPCION 3", bg="#aaaaaa", relief="flat", fg="blue", font=("Bold", 10),
                 command=lambda: indicador(btn3_indicador, frame_btn3))
btn3.place(x=10, y=150)

# Indicador para el botón 3
btn3_indicador = tk.Label(opciones, background="#aaaaaa")
btn3_indicador.place(x=3, y=150, height=38)

# Botón para la opción 4
btn4 = tk.Button(opciones, text="OPCION 4", bg="#aaaaaa", relief="flat", fg="blue", font=("Bold", 10),
                 command=lambda: indicador(btn4_indicador, frame_btn4))
btn4.place(x=10, y=200)

# Indicador para el botón 4
btn4_indicador = tk.Label(opciones, background="#aaaaaa")
btn4_indicador.place(x=3, y=200, height=38)

# Colocar el frame de opciones a la izquierda
opciones.pack(side=tk.LEFT)
opciones.pack_propagate(False)
opciones.configure(width=100, height=500)

# Crear el frame principal que cambiará su contenido
frame_original = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
frame_original.pack(side=tk.LEFT, fill="both", expand=True)
frame_original.pack_propagate(False)
frame_original.configure(height=500, width=500)

# Definir los frames para cada opción
frame_btn1 = tk.Frame(frame_original, bg="lightblue")
frame_btn2 = tk.Frame(frame_original, bg="lightgreen")
frame_btn3 = tk.Frame(frame_original, bg="lightyellow")
frame_btn4 = tk.Frame(frame_original, bg="lightpink")

# Añadir contenido a los frames (ejemplo: solo un Label en cada uno)
tk.Label(frame_btn1, text="Contenido Opción 1", bg="lightblue", font=("Arial", 18)).pack(expand=True)
tk.Label(frame_btn2, text="Contenido Opción 2", bg="lightgreen", font=("Arial", 18)).pack(expand=True)
tk.Label(frame_btn3, text="Contenido Opción 3", bg="lightyellow", font=("Arial", 18)).pack(expand=True)
tk.Label(frame_btn4, text="Contenido Opción 4", bg="lightpink", font=("Arial", 18)).pack(expand=True)

# Mostrar inicialmente el frame de la opción 1
mostrar_frame(frame_btn1)

# Iniciar la ventana principal
ventana.mainloop()

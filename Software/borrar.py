import tkinter as tk

def mostrar_frame(content_func):
    # Limpiar el frame principal
    for widget in frame_contenido.winfo_children():
        widget.destroy()
    
    # Ejecutar la función que agregará el contenido al frame
    content_func()

def mostrar_contenido_opcion1():
    label = tk.Label(frame_contenido, text="Contenido de la Opción 1", font=("Arial", 18))
    label.pack(pady=20)
    entry = tk.Entry(frame_contenido)
    entry.pack(pady=10)
    button = tk.Button(frame_contenido, text="Guardar")
    button.pack(pady=10)

def mostrar_contenido_opcion2():
    label = tk.Label(frame_contenido, text="Contenido de la Opción 2", font=("Arial", 18))
    label.pack(pady=20)
    checkbox = tk.Checkbutton(frame_contenido, text="Aceptar términos")
    checkbox.pack(pady=10)

def mostrar_contenido_opcion3():
    label = tk.Label(frame_contenido, text="Contenido de la Opción 3", font=("Arial", 18))
    label.pack(pady=20)
    listbox = tk.Listbox(frame_contenido)
    for item in ["Elemento 1", "Elemento 2", "Elemento 3"]:
        listbox.insert(tk.END, item)
    listbox.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("600x400")

# Crear el frame de las opciones de la izquierda
opciones = tk.Frame(ventana, bg="#aaaaaa")
opciones.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Botones para las opciones
btn1 = tk.Button(opciones, text="Opción 1", command=lambda: mostrar_frame(mostrar_contenido_opcion1))
btn1.pack(pady=10)

btn2 = tk.Button(opciones, text="Opción 2", command=lambda: mostrar_frame(mostrar_contenido_opcion2))
btn2.pack(pady=10)

btn3 = tk.Button(opciones, text="Opción 3", command=lambda: mostrar_frame(mostrar_contenido_opcion3))
btn3.pack(pady=10)

# Crear el frame contenedor de contenido
frame_contenido = tk.Frame(ventana, highlightbackground="black", highlightthickness=2)
frame_contenido.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

# Mostrar inicialmente la opción 1
mostrar_frame(mostrar_contenido_opcion1)

# Iniciar la ventana principal
ventana.mainloop()

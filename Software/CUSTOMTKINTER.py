import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Imagen con Descripción")

# Cargar la imagen
ruta_imagen = "Canchas_imagenes/cancha_1.jpg"  # Cambia esto por la ruta de tu imagen
imagen = Image.open(ruta_imagen)
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack(pady=10)

# Crear un label para la descripción
descripcion = "Esta es una descripción de la imagen."
label_descripcion = tk.Label(ventana, text=descripcion, font=("Arial", 14))
label_descripcion.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()

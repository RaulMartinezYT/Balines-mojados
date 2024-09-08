import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con Imagen")

# Cargar la imagen desde la subcarpeta 'imagenes'
ruta_imagen = "imagenes/imagen.png"
imagen = Image.open(ruta_imagen)

# Convertir la imagen a un formato que Tkinter pueda usar
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen
etiqueta_imagen = tk.Label(root, image=imagen_tk)
etiqueta_imagen.pack()

# Iniciar el bucle principal
root.mainloop()

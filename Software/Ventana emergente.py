import time
from tkinter import messagebox

titulo_ventana = input("Nombre de ventana: ")
descripcion = input("Descripcion: ")

messagebox.showinfo(titulo_ventana, descripcion)
messagebox.showwarning(titulo_ventana, descripcion)
messagebox.showerror(titulo_ventana, descripcion)

# Devuelve "YES" or "NO"
respuesta = messagebox.askquestion(titulo_ventana, descripcion)
if respuesta == 'yes':
    print("El usuario eligió sí.")
else:
    print("El usuario eligió no.")

# Devuelve true or false
respuesta = messagebox.askyesno(titulo_ventana, "¿Estás seguro?")
if respuesta:
    print("El usuario eligió sí.")
else:
    print("El usuario eligió no.")

respuesta = messagebox.askretrycancel(titulo_ventana, "El proceso falló. ¿Reintentar?")
if respuesta:
    print("El usuario eligió reintentar.")
else:
    print("El usuario eligió cancelar.")

time.sleep(5)
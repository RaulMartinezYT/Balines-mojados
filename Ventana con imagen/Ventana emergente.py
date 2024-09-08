import tkinter as tk

def mostrar_ventana_emergencia():
    # Crear una nueva ventana de nivel superior
    ventana_emergencia = tk.Toplevel()
    ventana_emergencia.title("Ventana de Emergencia")
    
    # Definir el tamaño de la ventana
    ancho_ventana = 300
    alto_ventana = 150
    
    # Obtener el tamaño de la pantalla
    pantalla_ancho = ventana_emergencia.winfo_screenwidth()
    pantalla_alto = ventana_emergencia.winfo_screenheight()
    
    # Calcular la posición X e Y para centrar la ventana
    x = (pantalla_ancho - ancho_ventana) // 2
    y = (pantalla_alto - alto_ventana) // 2
    
    # Establecer la geometría de la ventana
    ventana_emergencia.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
    # Agregar un mensaje a la ventana de emergencia
    mensaje = tk.Label(ventana_emergencia, text="¡Alerta! Esta es una ventana de emergencia.", padx=20, pady=20)
    mensaje.pack()

    # Agregar un botón para cerrar la ventana de emergencia
    boton_cerrar = tk.Button(ventana_emergencia, text="Cerrar", command=ventana_emergencia.destroy)
    boton_cerrar.pack()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")

# Agregar un botón en la ventana principal para mostrar la ventana de emergencia
boton_emergencia = tk.Button(ventana_principal, text="Mostrar Ventana de Emergencia", command=mostrar_ventana_emergencia)
boton_emergencia.pack(pady=20)

# Iniciar el bucle principal de Tkinter
ventana_principal.mainloop()

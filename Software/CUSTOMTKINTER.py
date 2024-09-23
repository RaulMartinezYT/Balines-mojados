import customtkinter as ctk

# Inicializar la aplicación
ctk.set_appearance_mode("System")  # Modo de apariencia
ctk.set_default_color_theme("blue")  # Tema de color

root = ctk.CTk()  # Crear la ventana principal
root.title("Ejemplo de Tabla en CustomTkinter")

# Crear encabezados de la tabla
headers = ["Nombre", "Edad", "Ciudad"]
for col, header in enumerate(headers):
    label = ctk.CTkLabel(root, text=header)
    label.grid(row=0, column=col, padx=10, pady=10)

# Datos de ejemplo
data = [
    ("Juan", 25, "Madrid"),
    ("Ana", 30, "Barcelona"),
    ("Luis", 22, "Valencia"),
]

# Insertar datos en la tabla
for row, values in enumerate(data, start=1):
    for col, value in enumerate(values):
        label = ctk.CTkLabel(root, text=value)
        label.grid(row=row, column=col, padx=10, pady=5)

# Ejecutar el bucle principal
root.mainloop()

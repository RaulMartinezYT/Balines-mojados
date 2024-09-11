import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

def crear_reservas_visuales(ventana):
    # Crear un Frame para las reservas visuales
    reservas_frame = tk.Frame(ventana, bg='lightgray')
    reservas_frame.pack(fill='both', expand=True)
    
    # Configurar la cuadrícula
    num_filas = 32  # Por ejemplo, 30 días + 2 filas adicionales para encabezados
    num_columnas = 20  # Por ejemplo, 16 intervalos de 15 minutos + 4 columnas para encabezados
    
    for i in range(num_filas):
        reservas_frame.grid_rowconfigure(i, weight=1)
        
    for j in range(num_columnas):
        reservas_frame.grid_columnconfigure(j, weight=1)
    
    # Encabezado de horarios
    horas = [""] + ["08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", 
                    "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", 
                    "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", 
                    "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", 
                    "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", 
                    "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", 
                    "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", 
                    "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", 
                    "02:00"]
    
    # Agregar encabezados de horario
    for j, hora in enumerate(horas):
        label = tk.Label(reservas_frame, text=hora, bg='lightblue', relief='solid')
        label.grid(row=0, column=j, sticky='nsew')

    # Agregar encabezados de fecha (para los días del mes)
    fecha_inicio = datetime.now().replace(day=1)  # Suponiendo que queremos el primer día del mes
    for i in range(1, num_filas):  # Empezar en 1 para dejar la primera fila para los horarios
        fecha = fecha_inicio + timedelta(days=i - 1)
        label = tk.Label(reservas_frame, text=fecha.strftime("%d/%m/%Y"), bg='lightgreen', relief='solid')
        label.grid(row=i, column=0, sticky='nsew')
        
    # Agregar celdas de reserva (vacías para el ejemplo)
    for i in range(1, num_filas):
        for j in range(1, num_columnas):
            cell = tk.Label(reservas_frame, text="", bg='white', relief='solid')
            cell.grid(row=i, column=j, sticky='nsew')
    
    return reservas_frame

ventana = tk.Tk()
ventana.geometry("1200x800")  # Ajusta el tamaño de la ventana según tus necesidades
reservas_frame = crear_reservas_visuales(ventana)
ventana.mainloop()

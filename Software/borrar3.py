import tkinter as tk

def create_grid(frame, rows, columns, values):
    inner_frame = tk.Frame(frame, padx=5, pady=5)
    inner_frame.pack(fill=tk.BOTH, expand=True)
    
    for row in range(rows):
        inner_frame.grid_rowconfigure(row, weight=1)
    for column in range(columns):
        inner_frame.grid_columnconfigure(column, weight=1)
    
    index = 0
    for row in range(rows):
        for column in range(columns):
            if index < len(values):
                text = values[index]
                index += 1
            else:
                text = ""
            label = tk.Label(inner_frame, text=text, borderwidth=1, relief="solid")
            label.grid(row=row, column=column, sticky="nsew")

def main():
    root = tk.Tk()
    root.title("Ventana Responsiva")

    # Configurar el tamaño de la ventana para que sea ajustable
    root.geometry("800x600")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Lista de valores para la cuadrícula
    values = [f"Item {i+1}" for i in range(370)]  # Cambia esta lista con tus valores deseados

    # Crear una cuadrícula de 10 filas y 37 columnas en el frame
    create_grid(frame, 10, 37, values)

    root.mainloop()

if __name__ == "__main__":
    main()

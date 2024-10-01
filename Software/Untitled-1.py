import customtkinter as ctk
from tkinter import colorchooser

class AplicacionDibujo:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Dibujo")
        self.root.geometry("800x600")

        # Configuración del lienzo
        self.lienzo = ctk.CTkCanvas(root, bg="white")
        self.lienzo.pack(fill="both", expand=True)

        # Variables para el dibujo
        self.dibujando = False
        self.x_inicial = None
        self.y_inicial = None
        self.color = "black"
        self.grosor = 2

        # Eventos del mouse
        self.lienzo.bind("<Button-1>", self.iniciar_dibujo)
        self.lienzo.bind("<B1-Motion>", self.dibujar)
        self.lienzo.bind("<ButtonRelease-1>", self.finalizar_dibujo)

        # Frame para los controles
        self.frame_controles = ctk.CTkFrame(root)
        self.frame_controles.pack(pady=10)

        # Botón para limpiar el lienzo
        self.boton_limpiar = ctk.CTkButton(self.frame_controles, text="Limpiar", command=self.limpiar_lienzo)
        self.boton_limpiar.pack(side="left", padx=5)

        # Botón para seleccionar color
        self.boton_color = ctk.CTkButton(self.frame_controles, text="Seleccionar Color", command=self.seleccionar_color)
        self.boton_color.pack(side="left", padx=5)

        # Selector de grosor
        self.grosor_var = ctk.StringVar(value="2")
        self.selector_grosor = ctk.CTkOptionMenu(self.frame_controles, self.grosor_var, "1", "2", "3", "4", "5", command=self.cambiar_grosor)
        self.selector_grosor.pack(side="left", padx=5)

    def iniciar_dibujo(self, event):
        self.dibujando = True
        self.x_inicial = event.x
        self.y_inicial = event.y

    def dibujar(self, event):
        if self.dibujando:
            self.lienzo.create_line(self.x_inicial, self.y_inicial, event.x, event.y, fill=self.color, width=self.grosor)
            self.x_inicial = event.x
            self.y_inicial = event.y

    def finalizar_dibujo(self, event):
        self.dibujando = False

    def limpiar_lienzo(self):
        self.lienzo.delete("all")

    def seleccionar_color(self):
        color_seleccionado = colorchooser.askcolor()[1]
        if color_seleccionado:
            self.color = color_seleccionado

    def cambiar_grosor(self, nuevo_grosor):
        try:
            self.grosor = int(nuevo_grosor)  # Asegúrate de convertir a entero
        except ValueError:
            self.grosor = 2  # Valor por defecto en caso de error

# Crear la ventana principal
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modo oscuro
    ctk.set_default_color_theme("blue")  # Tema azul

    ventana = ctk.CTk()
    app = AplicacionDibujo(ventana)
    ventana.mainloop()

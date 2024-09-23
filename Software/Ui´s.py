import datetime, sqlite3, time, tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import timedelta
from tkinter import colorchooser

############################
 #   VENTANAS EMERGENTES    #
  ############################
# Ventana emergente de alerta.
def alerta(titulo_ventana, descripcion):
    messagebox.showwarning(titulo_ventana, descripcion)

# Ventana emergente de informacion.
def informacion(titulo_ventana, descripcion):
    messagebox.showinfo(titulo_ventana, descripcion)

# Ventana emergente de error.
def error(titulo_ventana, descripcion):
    messagebox.showerror(titulo_ventana, descripcion)

# Ventana emergente con una pregunta a responder con si o no, retorna True o False dependiendo la seleccion.
def pregunta_si_no(titulo_ventana, pregunta):
    respuesta = messagebox.askyesno(titulo_ventana, pregunta)
    if respuesta:
        return True
    else:
        return False

# Ventana emergente con una pregunta a responder con si o no, retorna True o False dependiendo la seleccion.
def reintentar_si_no(titulo_ventana, pregunta):
    respuesta = messagebox.askretrycancel(titulo_ventana, pregunta)
    if respuesta:
        return True
    else:
        return False

#####################################
 #   EXTRACCION DE DATOS DE LA DB    #
  #####################################
def existe_dni(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM personal WHERE dni = ?", (dni,))
    entrada = cursor.fetchone()
    conn.close()
    if entrada[0] > 0:
        return True
    else:
        return False

def id_sucursal_a_barrio_sucursal(id_sucursal):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT barrio FROM sucursales WHERE id = ?;"
    datos = (id_sucursal,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    nombre_sucursal = resultado[0]
    conn.close()
    return nombre_sucursal

def barrio_sucursal_a_id_sucursal(barrio_sucursal):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT id FROM sucursales WHERE barrio = ?;"
    datos = (barrio_sucursal,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        id_sucursal = resultado[0]
        conn.close()
        return id_sucursal
    else:
        conn.close()
    
def dni_a_id_sucursal(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT id_sucursal FROM personal WHERE dni = ?;"
    datos = (dni,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        id_sucursal = resultado[0]
        conn.close()
        return id_sucursal
    else:
        conn.close()

def dni_a_clave(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT clave FROM personal WHERE dni = ?;"
    datos = (dni,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        clave = resultado[0]
        conn.close()
        return clave
    else:
        conn.close()

def dni_a_nombre(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT nombre FROM personal WHERE dni = ?;"
    datos = (dni,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        nombre = resultado[0]
        conn.close()
        return nombre
    else:
        conn.close()

def dni_a_apellido(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT apellido FROM personal WHERE dni = ?;"
    datos = (dni,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        apellido = resultado[0]
        conn.close()
        return apellido
    else:
        conn.close()

def dni_a_trabajo(dni):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    peticion = "SELECT trabajo FROM personal WHERE dni = ?;"
    datos = (dni,)
    cursor.execute(peticion, datos)
    resultado = cursor.fetchone()
    if resultado is not None:
        trabajo = resultado[0]
        conn.close()
        return trabajo
    else:
        conn.close()

def cantidad_sucursales():
    conn     = sqlite3.connect("Balines_mojados.db")
    cursor   = conn.cursor()
    cursor.execute("SELECT COUNT(id) FROM sucursales;")
    resultado = cursor.fetchone()
    cantidad = resultado[0]
    return cantidad

###############
 #   LISTAS    #
  ###############

# Devuelve una lista con el siguiente formato: fila["Barrio", "Calle"], fila["Barrio", "Calle"].
def lista_barrios_sucursales():
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT barrio, calle FROM sucursales;")
    resultados = cursor.fetchall()
    lista_barrios = ["~~~ Sucursal a seleccionar ~~~"] + [[fila[0], fila[1]] for fila in resultados]
    conn.close()
    return lista_barrios

# Devuelve una lista con el siguiente formato: fila["Nombre", "Apellido", NUMERO DE DNI], fila["Nombre", "Apellido", NUMERO DE DNI].
def lista_dni_personal():
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, apellido, dni FROM personal;")
    resultados = cursor.fetchall()
    lista_barrios = [[fila[0], fila[1], fila[2]] for fila in resultados]
    conn.close()
    return lista_barrios

#######################################
 #   ESTADO DE LA SUCURSAL / CANCHA    #
  #######################################
def id_sucursal_a_estado(id):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    consulta = "SELECT estado FROM sucursales WHERE id = ?;"
    datos = (id,)
    cursor.execute(consulta, datos)
    resultado = cursor.fetchall()
    estado = resultado[0]
    conn.close()
    return estado
        
def id_cancha_a_estado(id):
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    consulta = "SELECT estado FROM canchas WHERE id = ?;"
    datos = (id,)
    cursor.execute(consulta, datos)
    resultado = cursor.fetchall()
    estado = resultado[0]
    conn.close()
    return estado



def ventana_iniciar_sesion(color_principal = "#0F1035", color_secundario = "#365486", color_letras = "#7FC7D9", tipografia = "Arial", color_marcos = "#ffffff", color_boton_activo = "#ffffff", h1 = 45, h2 = 40, h3 = 35, h4 = 30, h5 = 25, h6 = 20, h7 = 15): 
    def cerrar_ventana(ventana_emergente):
        ventana_emergente.destroy()  # Cierra la ventana emergente
        ventana.deiconify()  # Muestra nuevamente la ventana principal
        
    def ventana_personalizacion():
        def color():
            color = colorchooser.askcolor(title="Selecciona un color")
            if color[1]:  # Verificar si se ha seleccionado un color
                ventana_personalizar.config(bg = color[1])

        # Deshabilitar la ventana principal
        ventana.withdraw()  # Oculta la ventana principal

        ventana_personalizar = tk.Toplevel(ventana)

        ancho_pantalla_personalizar, alto_pantalla_personalizar = ventana_personalizar.winfo_screenwidth(), ventana_personalizar.winfo_screenheight()
        
        ancho_ventana_inicial_personalizar = int(((alto_pantalla_personalizar / 2) * 16) / 9)
        alto_ventana_inicial_personalizar =  int(((ancho_pantalla_personalizar / 2) * 9) / 16)
        
        ventana_personalizar.minsize(ancho_ventana_inicial_personalizar, alto_ventana_inicial_personalizar)
        
        ventana_personalizar.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
        
        ventana_personalizar.config(background = color_principal)
        
        ventana_personalizar.title("Balines Mojados - Personalizacion")




        ventana_personalizar.grid_columnconfigure()
        ventana_personalizar.grid_rowconfigure()

        # Crear un botón para cerrar la ventana emergente
        boton_cerrar = tk.Button(ventana_personalizar, text="Cancelar", command = lambda: cerrar_ventana(ventana_personalizar))
        boton_cerrar.pack(pady=20)

        

        boton_color = tk.Button(ventana_personalizar, text="Seleccionar Color", command = color)
        boton_color.pack(pady=10)
        ventana_personalizar.mainloop()

    # Conectamos el software con la base de datos.
    conn = sqlite3.connect("Balines_mojados.db")

    # Declaramos el nombre del cursor, el cual se encarga de realizar las consultas a la base de datos.
    cursor = conn.cursor()

    # Funcion del boton de inicio de sesion, al ser presionado el boton realiza las siguientes acciones:
    def boton_iniciar_sesion():

        # Recibe y guarda los datos en variables separadas, DNI y la clave.
        dni = dni_entry.get()
        clave = clave_entry.get()
        
        # Verifica si el campo de DNI se encuentra vacio a la hora de haber presionado el boton.
        # Si se encuentra vacia se abre una ventana emergente de ERROR la cual le informa al usuario que se encuentra vacio.
        if dni == "":
            error("Error DNI", "El campo de DNI se encuentra vacio.")
            confirmacion_dni = False

        # Si no se encuentra vacia:
        else:
            # Remplaza posibles puntos los remplaza por nada.
            dni.replace(".","")

            # Intenata lo siguiente:
            try:
                # Intenta pasar el str a int.
                dni = int(dni)
                
                # Saca el valor absoluto del numero (sacandole asi cualquier signo).
                dni = abs(dni)

                # Vuelve a pasar el valor a str para poder usar el metodo .len() y asi poder calcular el largo de la cadena de caracteres.
                dni = str(dni)
                
                # Si el largo del DNI es igual a 8 se confirma que es un DNI.
                if len(dni) == 8:
                    confirmacion_dni = True

                # Si el tamaño del DNI no es de 8 digitos.
                else:
                    confirmacion_dni = False

                    # Si el tamaño del DNI es menor a 8 digitos, se le informa que al personal que el DNI esta incompleto.
                    if len(dni) < 8:
                        error("Error DNI", "El DNI ingresado está incompleto.")

                    # Si el DNI es mayor a 8 digitos se le informa al personal que el DNI es mas largo de lo que deveria.
                    else:
                        error("Error DNI", "El DNI ingresado es demasiado largo.")

            # Si no se puede realizar el unico motivo que queda es que se trata a cerca de una ecepcion de tipo "ValueError".
            # Esta exepcion (en este caso ocurre) se ejecuta ya que no se pudo pasar el valor string a entero, ya que no eran unicamente numeros.
            # Si llegamos a esto se le hará saber el o la empleado/a que el DNI ingresado no es un DNI. 
            except ValueError:
                error("Error DNI", "El DNI ingresasdo no es un DNI.")
        
        # Verifica si el campo de la clave se encuentra vacio a la hora de haber presionado el boton.
        # Si se encuentra vacia se abre una ventana emergente de ERROR la cual le informa al usuario que se encuentra vacio.
        if clave == "":
            error("Alerta", "El campo de la clave se encuentra vacio.")
            confirmacion_dni = False

        # Si no se encuentra vacia:
        # No se confirma la clave
        else:
            confirmacion_clave = True

        # Si se confirma el dni y la clave (osea que pasaron todos los filtros anteriormente mencionado) pasaria lo siguiente:
        if confirmacion_dni == True and confirmacion_clave == True:
            
            # Se define la consulta a realizar para el login:
            consulta = f"SELECT * FROM personal WHERE dni = ? AND clave = ?;"

            # Se define los datos para pasarle a la consulta.
            datos = (dni, clave)

            # Una vez lo tenemos todo preparado realizamos la consulta con los datos incluidos.
            cursor.execute(consulta, datos)

            # Al realizar la consulta se obtiene una respuesta con la siguiente linea, esa respuesta se utiliza para confirmar el inicio de sesion.
            inicio_sesion = cursor.fetchall()

            # Crea la consulta para averiguar cual es el Id de la sucursal en la que trabaja el empleado.
            consulta_id = "SELECT id_sucursal FROM personal WHERE dni = ?;"
            
            # Datos necesarios para la consulta.
            datos_id = (dni,)

            # Ejecuta la consulta con la consulta y los valores de la consulta.
            cursor.execute(consulta_id, datos_id)

            # Creamos una variable en la que se va a guardar el resultado de la consulta, osea la respuesta de la consulta.
            respuesta = cursor.fetchone()

            # Detecta si hay valor en la variable y si es asi:
            if respuesta:                    
                # Guarda la reserva de la consulta en una variable la cual se pasa a la siguiente ventana.
                # Y extraemos el valor de la tupla.
                id_sucursal = respuesta[0]

            # Si la peticion (chequea si el DNI y la clave son iguales a las que estan guardadas en la base de datos) se confirma el personal y el inicio de sesion, permitiendo asi el ingreso al software.
            if inicio_sesion:
                nombre = dni_a_nombre(dni)
                apellido = dni_a_apellido(dni)
                consulta = "SELECT * FROM personal WHERE dni = ? AND clave = ? AND trabajo = 'Administrador';"
                datos = (dni, clave)
                cursor.execute(consulta, datos)
                respuesta_administrador = cursor.fetchall()

                if respuesta_administrador:
                    informacion("Inicio de sesion - Administrador", f"Inicio de sesion completa.\nBienvenido {nombre} {apellido}")
                    ventana.destroy()
                    time.sleep(0.5)
                    ventana_administrador(dni, id_sucursal)
                
                else:
                    informacion("Inicio de sesion - Personal", f"Inicio de sesion completa.\nBienvenido {nombre} {apellido}")
                    ventana.destroy()
                    ventana_reservas(dni, id_sucursal)
            else:
                informacion("Inicio de sesion", "Error al intentar iniciar sesion.")

    # Creacion de la ventana.
    ventana = tk.Tk()
    
    # Guarda los valores de la pantalla en dos variables:
    # Ancho_pantall: Es el ancho de la pantalla.
    # Alto_pantalla: Es el alto de la pantalla.
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    

    # Esta linea de codigo se encarga de transformar los valores de la pantalla (Ancho y Alto de pantalla) a enteros (Numeros sin decimal) los cuales se utilizan para definir el tamaño de la ventana.
    # Al tener el ancho y el alto en enteros pasan por una cuenta matematica para que siempre mantengan la relacion 16:9.
    # Lo cual nos permite tener siempre una ventana con la misma relacion, unicamente para mantenerla responsive sin necesidad de que python lo intente y falle fatalmente.
    # Pasando a lo tecnico, agarra los valores anteriores de la pantalla (el ancho y largo, los cuales se dividen para que 9 valores de alto equivalgan a 16 de ancho, para tener siempre la misma relacion (16:9).
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)

    ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
    
    # Establecemos el minimo tamaño que podrá tener la ventana
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)

    # Especificamos las medidas iniciales de la ventana.
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")

    # Especificamos el color de fondo de pantalla.
    # Este valor es el atributo que se le pasa a la funcion que ya fue antes mencionada.
    ventana.config(background = color_principal)

    # Especificamos el nombre de la ventana.
    ventana.title("Balines Mojados - Iniciar sesion")

    # Creamos lo que es un LabelFrame (Un marco decorativo):
    marco        = tk.LabelFrame(ventana, border = 0, bg = color_secundario, highlightbackground = color_marcos, highlightcolor = color_marcos, highlightthickness = 2, pady = 10)
    
    # Creamos un texto de bienvenida, pero este se encuentra dentro del marco que respectivamente se encuentra dentro de la ventana y asi con cada objeto / elemento.
    bienvenido   = tk.Label(marco, background = color_secundario,  fg = color_letras,  font = (tipografia, h1), text = "BIENVENIDO")

    # Creamos un texto para el "Dni del empleado".
    nombre       = tk.Label(marco, background = color_secundario, fg = color_letras, font = (tipografia, h4), padx = 150, text = "DNI:")

    # Creamos un "INPUT" que en tkinter se lo conoce como "Entry" el cual nos va a ayudar a comunicar al personal con el software.
    # Este entry se encargará de recibir el nombre del personal utilizado para iniciar sesion.
    dni_entry    = tk.Entry(marco, bg = color_secundario, fg = color_letras, border = 0, font = (tipografia, h5), highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos, relief = "solid", width = 25)

    # Creamos un texto de "Codigo de seguridad".
    clave        = tk.Label(marco, background = color_secundario, fg = color_letras, font = (tipografia, h4), text = "Clave de seguridad:")

    # Creamos otro entry el cual es para el codigo de seguridad del personal, cada uno cuenta con el suyo propio.
    clave_entry  = tk.Entry(marco, bg = color_secundario, border = 0, font = (tipografia, h5), fg = color_letras, highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos, relief = "solid", show = "•", width = 25)
    
    # Creamos un LabelFrame por estetica al botón.
    marco_boton  = tk.LabelFrame(marco, bg = color_secundario, border = 0, highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos)
    
    # Creacion del boton para verificar los datos colocados.
    aceptar      = tk.Button(marco_boton, activebackground = color_boton_activo, background = color_secundario, border = 0, command = boton_iniciar_sesion, fg = color_marcos, font = (tipografia, h5), highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos, relief = "solid", text = "Iniciar sesión", width = 25)
    
    marco_personalizar = tk.LabelFrame(ventana, bg = color_secundario, border = 0, highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos)
    boton_personalizar = tk.Button(marco_personalizar, activebackground = color_boton_activo, background = color_secundario, border = 0, command = ventana_personalizacion, fg = color_marcos, font = (tipografia, h7), highlightthickness = 2, highlightcolor = color_marcos, highlightbackground = color_marcos, relief = "solid", text = "Config", width = 5, height = 1)

    marco.pack(pady = 20)
    bienvenido.pack()
    nombre.pack(padx = 200, pady = (30,0))
    dni_entry.pack(pady=25)
    clave.pack(pady=(40,25))
    clave_entry.pack(pady=25)
    marco_boton.pack(pady = (40,100))
    aceptar.pack()
    marco_personalizar.pack(side = tk.BOTTOM, anchor = tk.SE, padx = 5, pady = 5)
    boton_personalizar.pack(expand = True, fill = "both")

    ventana.mainloop()

def ventana_sucursales(color_principal = "#0F1035", color_secundario = "#365486", color_letras = "#7FC7D9", tipografia = "Arial", color_marcos = "#ffffff", color_boton_activo = "#ffffff", h1 = 45, h2 = 40, h3 = 35, h4 = 30, h5 = 25, h6 = 20, h7 = 15):
    ventana = tk.Tk()
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
    ventana.config(background = color_principal)
    ventana.title("Balines Mojados - Sucursales")

    frame_sucursales = tk.Frame(ventana, padx = 5, pady = 5)
    frame_sucursales.grid()

    for x in range(4):
        frame_sucursales.grid_columnconfigure(x, weight = 1)

    for x in range(5):
        frame_sucursales.grid_rowconfigure()

    cantidad_sucursales = cantidad_sucursales()
    


def ventana_reservas(dni_personal = None, id_sucursal_personal = None, color_principal = "#0F1035", color_secundario = "#365486", color_letras = "#7FC7D9", tipografia = "Arial", color_marcos = "#ffffff", color_boton_activo = "#ffffff", h1 = 45, h2 = 40, h3 = 35, h4 = 30, h5 = 25, h6 = 20, h7 = 15):
    
    def numero_dia_a_nombre_dia(numero_dia):
        dias_de_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        return dias_de_semana[numero_dia]

    if dni_personal == None or id_sucursal_personal == None:
        error("ERROR CATASTROFICO", "No deberias haber podido ingresar aqui")
        return error
    else:
        conn = sqlite3.connect("Balines_mojados.db")

        cursor = conn.cursor()

        consulta = f"SELECT * FROM personal WHERE dni = ? AND id_sucursal = ?;"
        datos = (dni_personal, id_sucursal_personal)
        cursor.execute(consulta, datos)

        datos_correctos = cursor.fetchall()

        if datos_correctos:
                informacion("Esta bien","OK")
        else:
            # informacion("Error en la base de datos", "No se encuentra en la base de datos.")
            # return error
            pass
    
    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    ventana = tk.Tk()
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)
    ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
    ventana.config(background = color_principal)
    ventana.title("Balines Mojados - Reservas")
    # ===================================== FRAME 1 ======================================== #

    ventana.grid_columnconfigure(0, weight = 1)
    ventana.grid_columnconfigure(1, weight = 1000)
    ventana.grid_rowconfigure(0, weight = 1)

    frame_botones    = tk.Frame(ventana, background = color_secundario, highlightthickness = 1, highlightbackground = color_marcos)
    frame_reservas   = tk.Frame(ventana, background = color_secundario, highlightthickness = 1, highlightbackground = color_marcos)
    
    frame_botones.grid(   column = 0, row = 0, padx = (10, 0), pady = 10, sticky = "nsew")
    frame_reservas.grid(  column = 1, row = 0, padx = 10, pady = 10, sticky = "nsew")

    Marco_nueva_reserva     = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    crear_reserva           = tk.Button(Marco_nueva_reserva, text = "NUEVA\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_editar            = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    editar_reserva          = tk.Button(Marco_editar, text = "EDITAR\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_eliminar          = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    eliminar_reserva        = tk.Button(Marco_eliminar, text = "ELIMINAR\n RESERVA ", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)
    Marco_cambio_sucursal   = tk.LabelFrame(frame_botones, bg = color_secundario, border = 0, highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
    cambio_sucursal         = tk.Button(Marco_cambio_sucursal, text = "CAMBIAR\nSUCURSAL", font = (tipografia, h7), bg = color_secundario, fg = color_letras, border = 0, activebackground = color_boton_activo, activeforeground = color_boton_activo)

    Marco_nueva_reserva.pack( pady = (5, 0), padx = 2.5)
    crear_reserva.pack()
    Marco_editar.pack( pady = (5, 0), padx = 2.5)
    editar_reserva.pack()
    Marco_eliminar.pack( pady = (5, 0), padx = 2.5)
    eliminar_reserva.pack()
    Marco_cambio_sucursal.pack( pady = (0, 5), padx = 2.5, side="bottom")
    cambio_sucursal.pack()

    # ===================================== FRAME 2 ======================================== #
    def nombre_dia(numero_dia):
        dias_de_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        return dias_de_semana[numero_dia]
    
    horas    = ["FECHA / HORA","08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "01:00", "01:15", "01:30", "01:45", "02:00"]
    fechas   = []
    dias     = []

    fecha_hoy = datetime.datetime.now().date()

    for x in range(31):
        fechas.append(fecha_hoy + timedelta(days = x))
        dias.append(nombre_dia(fechas[x].weekday()))
        fechas[x]   = str(fechas[x])
        dias[x]     = str(dias[x])
    
    def iniciar_tabla():
        for x in range(31):
            dia      = dias[x]
            fecha    = fechas[x]
            tabla.insert("", "end", values = (f"  {dia}:\n{fecha}", ""))

    def reservas_visuales(fecha, fila, columna):
        dia    = dias[fila]
        datos  = [f"{dia}:\n{fecha}"]
        for x in range(72):
            if x == 0:
                pass
            else:
                if x != columna:
                    datos.append("")
                else:
                    datos.append("RESERVADO")
                item_id = tabla.get_children()[fila]
                tabla.item(item_id, values = datos)

    def fila_columna_reserva(fecha, hora):
        columna = horas.index(hora)
        print(f"Columna: {columna}")

        fila = fechas.index(fecha)
        print(f"Fila: {fila}")

        reservas_visuales(fecha, fila, columna)


                

    style = ttk.Style()
    style.configure("Treeview", rowheight = 70)
    
    tabla = ttk.Treeview(frame_reservas, columns = horas, show = 'headings')

    for hora in horas:
        tabla.heading(hora, text = hora, anchor = "center")
        tabla.column(hora, width = 100, anchor = "center")

    tabla.pack(fill = 'both', expand = True)
    tabla.bind("<Button-1>", lambda e: "break")

    scrollbar = ttk.Scrollbar(frame_reservas, orient = 'horizontal', command = tabla.xview)
    scrollbar.pack(side = 'bottom', fill = 'x')
    tabla.config(xscrollcommand = scrollbar.set)
    iniciar_tabla()
    fila_columna_reserva("2024-09-30", "08:00")

    ventana.mainloop()

def ventana_administrador(dni_administrador = None, id_sucursal_administrador = None, color_principal = "#0F1035", color_secundario = "#365486", color_letras = "#7FC7D9", tipografia = "Arial", color_marcos = "#ffffff", color_boton_activo = "#ffffff", h1 = 45, h2 = 40, h3 = 35, h4 = 30, h5 = 25, h6 = 20, h7 = 15):
    
    def limpiar_frame(funcion):
        for widget in frame_principal.winfo_children():
            widget.destroy()
        funcion()

    def personal_frame():
        
        def obtener_datos_añadir():
            dni               = dni_entry_añadir.get()
            sucursal_nombre   = sucursal_entry_añadir.get()
            id_sucursal       = barrio_sucursal_a_id_sucursal(sucursal_nombre)
            clave             = clave_entry_añadir.get()
            clave_confir      = clave_confir_entry_añadir.get()
            nombre            = nombre_entry_añadir.get()
            nombre            = nombre.capitalize()
            nombre            = nombre.lstrip()
            apellido          = apellido_entry_añadir.get()
            apellido          = apellido.capitalize()
            apellido          = apellido.lstrip()
            trabajo           = desempeño_entry_añadir.get()

            while True:

                if dni == "":
                        alerta("Dni incompleto", "El campo del dni se encuentra vacio.")
                        break
                
                else:

                    if existe_dni(dni):
                        alerta("Error en la base de datos", "El Dni ya se encuentra en la base de datos.")
                        return error
                    
                    else:
                        try:
                            dni = abs(int(dni))
                            dni = str(dni)

                            if len(dni) < 8 :
                                alerta("Dni incompleto", "El numero de DNI proporcionado se encuentra incompleto.")
                                return error
                                        
                            if len(dni) > 8:
                                alerta("Dni inexistente", "El numero de DNI proporcionado es demasiado largo.")
                                return error
                            
                            dni = int(dni)

                        except ValueError:
                            alerta("Unicamente numeros", "El numero de DNI proporcionado no corresponde a un DNI.")
                            return error
                        
                        if sucursal_nombre == "~~~ Sucursal a seleccionar ~~~":
                            alerta("Sucursal incompleta", "El campo del sucursal no es una sucursal.")
                            break
                        else:

                            if clave == "":
                                alerta("Clave incompleta", "El campo de la clave se encuentra vacio.")
                                break

                            else:
                                if len(clave) < 8:
                                    alerta("Clave muy corta", "La clave es muy corta, se necesita 8 caracteres como minimo.")
                                    return error
                                else:

                                    if len(clave) > 15:
                                        alerta("Clave muy larga", "La clave es muy larga, 15 caracteres como maximo.")
                                    else:

                                        if clave == clave_confir:
                                            pass
                                        else:
                                            alerta("Confirmar clave", "La clave no se pudo confirmar.")
                                            return error
                                if nombre == "":
                                    alerta("Nombre incompleto", "El campo del nombre se encuentra vacio.")
                                    break

                                else:
                                    if nombre.isalpha():

                                        if len(nombre) < 3:
                                            alerta("El nombre es muy corto", "El nombre debe contener entre 4 y 30 caracteres.")
                                            return error
                                        
                                        if len(nombre) > 30:
                                            alerta("El nombre es muy largo","El nombre debe contener entre 4 y 30 caracteres.")
                                            return error
                                        
                                    else:
                                        alerta("Nombre incorrecto",'El parametro de "Nombre", acepta unicamente color_letras.')
                                        return error
                                
                                    if apellido == "":
                                        alerta("Apellido incompleto", "El campo del apellido se encuentra vacio.")
                                        break

                                    else:
                                        if apellido.isalpha():

                                            if len(apellido) < 3:
                                                alerta("El apellido es muy corto", "El apellido debe contener entre 4 y 30 caracteres.")
                                                return error
                                            
                                            if len(apellido) > 30:
                                                alerta("El apellido es muy largo", "El apellido debe contener entre 4 y 30 caracteres.")
                                                return error

                                            
                                            if pregunta_si_no("Confirmacion de datos", f'¿Están correctos los siguientes datos?\n● Nombre: "{nombre}"\n● Apellido: "{apellido}"\n● Cargo: "{trabajo}"\n● En la sucursal: "{barrio_sucusal}"'):
                                                conn = sqlite3.connect("Balines_mojados.db")
                                                cursor = conn.cursor()

                                                consulta = "INSERT INTO personal (dni, id_sucursal, clave, nombre, apellido, trabajo) VALUES (?, ?, ?, ?, ?, ?)"
                                                barrio_sucusal = id_sucursal_a_barrio_sucursal(id_sucursal)
                                                datos = (dni, id_sucursal, clave, nombre, apellido, trabajo)
                                                
                                                dni_entry_añadir.delete(0, tk.END)
                                                sucursal_entry_añadir.current(0)
                                                clave_entry_añadir.delete(0, tk.END)
                                                clave_confir_entry_añadir.delete(0, tk.END)
                                                nombre_entry_añadir.delete(0, tk.END)
                                                apellido_entry_añadir.delete(0, tk.END)
                                                desempeño_entry_añadir.current(0)

                                                cursor.execute(consulta, datos)
                                                conn.commit()
                                                informacion("Procesado satisfactoriamente", "Personal agregado correctamente a la base de datos.")
                                                break
                                            else:
                                                informacion("Procesado cancelado satisfactoriamente","Añadicion de datos cancelada.")
                                                break

                                        else:
                                            alerta("Apellido Incorrecto", "El apellido tiene que conformarse unicamente por color_letras")
                                            break

        def obtener_datos_modificar():
            dni                = dni_entry_modificar.get()
            barrio_sucursal    = sucursal_entry_modificar.get()
            clave              = clave_entry_modificar.get()
            clave_confir       = clave_confir_entry_modificar.get()
            nombre             = nombre_entry_modificar.get()
            nombre             = nombre.capitalize()
            nombre             = nombre.lstrip()
            apellido           = apellido_entry_modificar.get()
            apellido           = apellido.capitalize()
            apellido           = apellido.lstrip()
            trabajo            = desempeño_entry_modificar.get()

            while True:
                if dni == "":
                    alerta("Dni incompleto", "El campo del dni se encuentra vacio.")
                    break
                else:
                    try:
                        dni = abs(int(dni))
                        dni = str(dni)

                        if len(dni) < 8 :
                            alerta("Dni incompleto", "El numero de DNI proporcionado se encuentra incompleto.")
                            break
                                    
                        if len(dni) > 8:
                            alerta("Dni inexistente", "El numero de DNI proporcionado es demasiado largo.")
                            break
                        
                        dni = int(dni)

                    except ValueError:
                        alerta("Unicamente numeros", "El numero de DNI proporcionado no corresponde a un DNI.")
                        break
                    
                    if existe_dni(dni) == False:
                            alerta("Error base de datos", "El Dni no se encuentra en la base de datos.")
                            break
                        
                    else:
                    
                        if barrio_sucursal == "~~~ Sucursal a seleccionar ~~~":
                            alerta("Sucursal incompleta", "El campo del sucursal no es una sucursal.")
                            break
                        else:
                        
                            if clave == "":
                                alerta("Clave incompleta", "El campo de la clave se encuentra vacio.")
                                break
                            
                            else:
                                if len(clave) < 8:
                                    alerta("Clave muy corta", "La clave es muy corta, se necesita 8 caracteres como minimo.")
                                    break
                                else:
                                
                                    if len(clave) > 15:
                                        alerta("Clave muy larga", "La clave es muy larga, 15 caracteres como maximo.")
                                    else:
                                    
                                        if clave == clave_confir:
                                            pass
                                        else:
                                            alerta("Confirmar clave", "La clave no se pudo confirmar.")
                                            break
                                
                                if nombre == "":
                                    alerta("Nombre incompleto", "El campo del nombre se encuentra vacio.")
                                    break
                                
                                else:
                                    if nombre.isalpha():
                                    
                                        if len(nombre) < 3:
                                            alerta("El nombre es muy corto", "El nombre debe contener entre 4 y 30 caracteres.")
                                            break
                                        
                                        if len(nombre) > 30:
                                            alerta("El nombre es muy largo","El nombre debe contener entre 4 y 30 caracteres.")
                                            break
                                        
                                    else:
                                        alerta("Nombre incorrecto",'El parametro de "Nombre", acepta unicamente color_letras.')
                                        break
                                
                                    if apellido == "":
                                        alerta("Apellido incompleto", "El campo del apellido se encuentra vacio.")
                                        break
                                    
                                    else:
                                        if apellido.isalpha():
                                        
                                            if len(apellido) < 3:
                                                alerta("El apellido es muy corto", "El apellido debe contener entre 4 y 30 caracteres.")
                                                break
                                            
                                            if len(apellido) > 30:
                                                alerta("El apellido es muy largo", "El apellido debe contener entre 4 y 30 caracteres.")
                                                break
                                            
                                        else:
                                            alerta("Apellido Incorrecto", "El apellido tiene que conformarse unicamente por color_letras")
                                            break

                                        if trabajo == "~~~ Desempeño a seleccionar ~~~":
                                            alerta("Desempeño laboral incompleta", "El campo del desempeño laboral no es un desempeño laboral.")
                                            break
                                        
                                        else:
                                            conn = sqlite3.connect("Balines_mojados.db")
                                            cursor = conn.cursor()

                                            barrio_sucursal_original    = dni_a_id_sucursal(dni)
                                            barrio_sucursal_original    = id_sucursal_a_barrio_sucursal(barrio_sucursal_original)
                                            clave_original              = dni_a_clave(dni)
                                            nombre_original             = dni_a_nombre(dni)
                                            nombre_original             = nombre_original.capitalize()
                                            nombre_original             = nombre_original.lstrip()
                                            apellido_original           = dni_a_apellido(dni)
                                            apellido_original           = apellido_original.capitalize()
                                            apellido_original           = apellido_original.lstrip()
                                            trabajo_original            = dni_a_trabajo(dni)
                                            
                                            if clave != "" and clave != None:

                                                if clave != clave_original:

                                                    if pregunta_si_no("Confirmar cambio", f'¿Estás seguro de cambiar la clave del empleado {nombre_original} {apellido_original} con DNI ({dni}), de "{clave_original}" a "{clave}"?'):
                                                        consulta = "UPDATE personal SET clave = ? WHERE dni = ?;"
                                                        datos = (clave, dni)

                                                        if cursor.execute(consulta, datos):
                                                            informacion("Procesado satisfactoriamente","Actualizacion de datos completada con exito.")
                                                            conn.commit()
                                                        else:
                                                            informacion("Error inesperado", "No se pudo actualizar los datos del personal.")
                                                    else:
                                                        informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                                                else:
                                                    pass

                                            if nombre != "" and nombre != None:
                                                

                                                if nombre != nombre_original:
                                                    
                                                    if pregunta_si_no("Confirmar cambio", f'¿Estás seguro de cambiar el nombre del empleado con DNI ({dni}) de {nombre_original} {apellido_original} a {nombre} {apellido}?'):
                                                        consulta = "UPDATE personal SET nombre = ? WHERE dni = ?;"
                                                        datos = (nombre, dni)

                                                        if cursor.execute(consulta, datos):
                                                            informacion("Procesado satisfactoriamente","Actualizacion de datos completada con exito.")
                                                            conn.commit()
                                                        else:
                                                            informacion("Error inesperado", "No se pudo actualizar los datos del personal.")
                                                    else:
                                                        informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                                                else:
                                                    pass

                                            if apellido != "" and apellido != None:
                                                apellido_original = dni_a_apellido(dni)

                                                if apellido != apellido_original:

                                                    if pregunta_si_no("Confirmar cambio", f'¿Estás seguro de cambiar el apellido de {nombre_original} {apellido_original} con DNI ({dni}) a {nombre} {apellido}?'):
                                                        consulta = "UPDATE personal SET apellido = ? WHERE dni = ?;"
                                                        datos = (apellido, dni)

                                                        if cursor.execute(consulta, datos):
                                                            informacion("Procesado satisfactoriamente","Actualizacion de datos completada con exito.")
                                                            conn.commit()
                                                        else:
                                                            informacion("Error inesperado", "No se pudo actualizar los datos del personal.")
                                                    else:
                                                        informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                                                else:
                                                    pass

                                            if trabajo != "" and trabajo != None:

                                                if trabajo != trabajo_original:

                                                    if pregunta_si_no("Confirmar cambio", f'¿Estas seguro de cambiar el desempeño laboral del empleado {nombre_original} {apellido_original} con dni ({dni}), de "{trabajo_original}" a "{trabajo}"?'):
                                                        consulta = "UPDATE personal SET trabajo = ? WHERE dni = ?;"
                                                        datos = (trabajo, dni)

                                                        if cursor.execute(consulta, datos):
                                                            informacion("Procesado satisfactoriamente","Actualizacion de datos completada con exito.")
                                                            conn.commit()
                                                        else:
                                                            informacion("Error inesperado", "No se pudo actualizar los datos del personal.")
                                                    else:
                                                        informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                                                else:
                                                    pass
                                            if (clave_original == clave) and (nombre_original == nombre) and (apellido_original == apellido) and (trabajo_original == trabajo):
                                                informacion("Base de datos no actualizada","Ningun dato fue remplazado, los datos ingresados son los mismos que se encuentran en la base de datos.")

                                            dni_entry_modificar.delete(0, tk.END)
                                            sucursal_entry_modificar.current(0)
                                            clave_entry_modificar.delete(0, tk.END)
                                            clave_confir_entry_modificar.delete(0, tk.END)
                                            nombre_entry_modificar.delete(0, tk.END)
                                            apellido_entry_modificar.delete(0, tk.END)
                                            desempeño_entry_modificar.current(0)
                                            conn.commit()
                                            break                        

        def obtener_datos_eliminar():
                dni = dni_entry_eliminar.get()
                
                try:
                    
                    dni = str(dni)

                    if len(dni) < 8 :
                        alerta("Dni incompleto", "El numero de DNI proporcionado se encuentra incompleto.")
                        return error
                    
                    if len(dni) > 8:
                        alerta("Dni inexistente", "El numero de DNI proporcionado es demasiado largo.")
                        return error
                    
                    dni = int(dni)

                except ValueError:
                    alerta("Unicamente numeros", "El numero de DNI proporcionado no corresponde a un DNI.")
                    return error
                
                if existe_dni(dni):
                    nombre = dni_a_nombre(dni)
                    apellido = dni_a_apellido(dni)
                    sucursal = dni_a_id_sucursal(dni)
                    sucursal = id_sucursal_a_barrio_sucursal(sucursal)

                    if pregunta_si_no("Eliminar personal", f'¿Estás seguro de eliminar de la base de datos a "{nombre} {apellido}" con DNI: "{dni}", que trabaja en la sucursal de: "{sucursal}"?'):
                        if pregunta_si_no("Eliminar personal","¿Estas realmente seguro?\n(Este cambio es irreversible)"):
                            conn = sqlite3.connect("Balines_mojados.db")
                            cursor = conn.cursor()

                            consulta = "DELETE FROM personal WHERE dni = ?;"
                            datos = (dni,)
                            cursor.execute(consulta, datos)

                            informacion("Procesado satisfactoriamente","Actualizacion de datos completada con exito.")
                            dni_entry_eliminar.delete(0, tk.END)
                            conn.commit()
                        else:
                            informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                    else:
                        informacion("Procesado cancelado satisfactoriamente","Actualizacion de datos cancelada.")
                else:
                    alerta("Error base de datos", "El Dni no se encuentra en la base de datos.")
                    return error

        # Lista de los barrios de las sucursales:
        sucursales = lista_barrios_sucursales()

        # Lista del desempeño del personal:
        desempeño = ["~~~ Desempeño a seleccionar ~~~","Recepcionista", "Referi", "Equipamiento","Seguridad", "Administrador"]

        # Lista de dni personal:
        todos_dni_personal = lista_dni_personal()

        # Configuracion del grid del frame principal.
        for x in range(3):
            frame_principal.grid_columnconfigure(x, weight = 1)
        frame_principal.grid_rowconfigure(0, weight = 1)

        # Declaracion de los frames.
        frame_añadir      = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_modificar   = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_eliminar    = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)

        # Posicionamiento de los frames.
        frame_añadir.grid(     column = 0, row = 0, sticky = "nsew", pady = (5,0), padx = (0,5))
        frame_modificar.grid(  column = 1, row = 0, sticky = "nsew", pady = (5,0), padx = (0,5))
        frame_eliminar.grid(   column = 2, row = 0, sticky = "nsew", pady = (5,0))

        # Configuracion del grid de los frames.
        for x in range(15):
            frame_añadir.grid_rowconfigure(x, weight = 1)
        frame_añadir.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_modificar.grid_rowconfigure(x, weight = 1)
        frame_modificar.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_eliminar.grid_rowconfigure(x, weight = 1)
        frame_eliminar.grid_columnconfigure(0, weight = 1)

        

          ##################################################
         #    DECLARACION DE ELEMENTOS AÑADIR PERSONAL    #
        ##################################################
        encabezado_añadir          = tk.Label(       frame_añadir, text = "AÑADIR PERSONAL", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
                
        dni_texto_añadir           = tk.Label(       frame_añadir, text = "Dni del personal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        dni_entry_añadir           = tk.Entry(       frame_añadir, font = (tipografia, h7))
         
        sucursal_texto_añadir      = tk.Label(       frame_añadir, text = "Sucursal en la que desempeñará su trabajo:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_añadir      = ttk.Combobox(   frame_añadir, values = sucursales, state = "readonly", font = (tipografia, h7))
        sucursal_entry_añadir.current(0)
        
        clave_texto_añadir         = tk.Label(       frame_añadir, text = "Clave del personal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        clave_entry_añadir         = tk.Entry(       frame_añadir, font = (tipografia, h7))
        
        clave_confir_texto_añadir  = tk.Label(       frame_añadir, text = "Repita la clave:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        clave_confir_entry_añadir  = tk.Entry(       frame_añadir, font = (tipografia, h7))
                 
        nombre_texto_añadir        = tk.Label(       frame_añadir, text = "Nombre del empleado:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        nombre_entry_añadir        = tk.Entry(       frame_añadir, font = (tipografia, h7))
               
        apellido_texto_añadir      = tk.Label(       frame_añadir, text = "Apellido del empleado:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        apellido_entry_añadir      = tk.Entry(       frame_añadir, font = (tipografia, h7))
        
        desempeño_texto_añadir     = tk.Label(       frame_añadir, text = "Desempeño laboral:", foreground = color_letras,  bg = color_secundario, font = (tipografia, h7))
        desempeño_entry_añadir     = ttk.Combobox(   frame_añadir, values = desempeño, state = "readonly", font = (tipografia, h7))
        desempeño_entry_añadir.current(0)

        btn_añadir =                  tk.Button(frame_añadir, text = "Añadir personal", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_añadir)

          ######################################################
         #    POSICIONAMIENTO DE ELEMENTOS AÑADIR PERSONAL    #
        ######################################################
        encabezado_añadir.grid(            column = 0, row = 0,  sticky = "nsew", padx = 5, pady = 5)

        dni_texto_añadir.grid(             column = 0, row = 1,  sticky = "nsew")
        dni_entry_añadir.grid(             column = 0, row = 2,  sticky = "ew",   padx = 15)

        sucursal_texto_añadir.grid(        column = 0, row = 3,  sticky = "nsew")
        sucursal_entry_añadir.grid(        column = 0, row = 4,  sticky = "ew",   padx = 15)

        clave_texto_añadir.grid(           column = 0, row = 5,  sticky = "nsew")
        clave_entry_añadir.grid(           column = 0, row = 6,  sticky = "ew",   padx = 15)
        clave_confir_texto_añadir.grid(    column = 0, row = 7,  sticky = "nsew")
        clave_confir_entry_añadir.grid(    column = 0, row = 8,  sticky = "ew",   padx = 15)

        nombre_texto_añadir.grid(          column = 0, row = 9,  sticky = "nsew")
        nombre_entry_añadir.grid(          column = 0, row = 10, sticky = "ew",   padx = 15)

        apellido_texto_añadir.grid(        column = 0, row = 11, sticky = "nsew")
        apellido_entry_añadir.grid(        column = 0, row = 12, sticky = "ew",   padx = 15)

        desempeño_texto_añadir.grid(       column = 0, row = 13, sticky = "nsew")
        desempeño_entry_añadir.grid(       column = 0, row = 14, sticky = "ew",   padx = 15)
        
        btn_añadir.grid(                   column = 0, row = 15, sticky = "nsew", padx = 5, pady = 5)

          #####################################################
         #    DECLARACION DE ELEMENTOS MODIFICAR PERSONAL    #
        #####################################################
        encabezado_modificar              = tk.Label(       frame_modificar, text = "MODIFICAR DATOS DE PERSONAL",    border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        
        dni_texto_modificar               = tk.Label(       frame_modificar, text = "Dni del personal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        dni_entry_modificar               = ttk.Combobox(   frame_modificar, values = todos_dni_personal, font = (tipografia, h7))
        
        sucursal_texto_modificar          = tk.Label(       frame_modificar, text = "Sucursal en la que desempeña su trabajo:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_modificar          = ttk.Combobox(   frame_modificar, values = sucursales, state = "readonly", font = (tipografia, h7))
        sucursal_entry_modificar.current(0)
        
        clave_texto_modificar             = tk.Label(       frame_modificar, text = "Clave del personal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        clave_entry_modificar             = tk.Entry(       frame_modificar, font = (tipografia, h7))
        
        clave_confir_texto_modificar      = tk.Label(       frame_modificar, text = "Repita la clave:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        clave_confir_entry_modificar      = tk.Entry(       frame_modificar, font = (tipografia, h7))
        
        nombre_texto_modificar            = tk.Label(       frame_modificar, text = "Nombre del empleado:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        nombre_entry_modificar            = tk.Entry(       frame_modificar, font = (tipografia, h7))
        
        apellido_texto_modificar          = tk.Label(       frame_modificar, text = "Apellido del empleado:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        apellido_entry_modificar          = tk.Entry(       frame_modificar, font = (tipografia, h7))
        
        desempeño_texto_modificar         = tk.Label(       frame_modificar, text = "Desempeño laboral:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        desempeño_entry_modificar         = ttk.Combobox(   frame_modificar, values = desempeño, state = "readonly", font = (tipografia, h7))
        desempeño_entry_modificar.current(0)
        
        btn_modificar                     = tk.Button(      frame_modificar, text = "Guardar datos del personal", foreground = color_letras, bg = color_secundario, font = (tipografia, h7),relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_modificar)

          #########################################################
         #    POSICIONAMIENTO DE ELEMENTOS MODIFICAR PERSONAL    #
        #########################################################
        encabezado_modificar.grid(         column = 0, row = 0,  sticky = "nsew", padx = 5, pady = 5)
        
        dni_texto_modificar.grid(          column = 0, row = 1,  sticky = "nsew")
        dni_entry_modificar.grid(          column = 0, row = 2,  sticky = "ew", padx = 15)
        
        sucursal_texto_modificar.grid(     column = 0, row = 3,  sticky = "nsew")
        sucursal_entry_modificar.grid(     column = 0, row = 4,  sticky = "ew", padx = 15)
        
        clave_texto_modificar.grid(        column = 0, row = 5,  sticky = "nsew")
        clave_entry_modificar.grid(        column = 0, row = 6,  sticky = "ew", padx = 15)
        
        clave_confir_texto_modificar.grid( column = 0, row = 7,  sticky = "nsew")
        clave_confir_entry_modificar.grid( column = 0, row = 8,  sticky = "ew", padx = 15)
        
        nombre_texto_modificar.grid(       column = 0, row = 9,  sticky = "nsew")
        nombre_entry_modificar.grid(       column = 0, row = 10, sticky = "ew", padx = 15)
        
        apellido_texto_modificar.grid(     column = 0, row = 11, sticky = "nsew")
        apellido_entry_modificar.grid(     column = 0, row = 12, sticky = "ew", padx = 15)
        
        desempeño_texto_modificar.grid(    column = 0, row = 13, sticky = "nsew")
        desempeño_entry_modificar.grid(    column = 0, row = 14, sticky = "ew", padx = 15)
        
        btn_modificar.grid(                column = 0, row = 15, sticky = "nsew", padx = 5, pady = 5)

          ####################################################
         #    DECLARACION DE ELEMENTOS ELIMINAR PERSONAL    #
        ####################################################
        encabezado_eliminar           = tk.Label(    frame_eliminar, text = "ELIMINAR PERSONAL", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        dni_texto_eliminar            = tk.Label(    frame_eliminar, text = "Dni del personal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        dni_entry_eliminar            = tk.Entry(    frame_eliminar, font = (tipografia, h7))
        btn_eliminar                  = tk.Button(   frame_eliminar, text = "Eliminar personal", foreground = color_letras, bg = color_secundario, font = (tipografia, h7),relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_eliminar)
        
          #########################################################
         #    POSICIONAMIENTO DE ELEMENTOS ELIMINARS PERSONAL    #
        #########################################################
        encabezado_eliminar.pack(    side = "top",     fill = "x", padx = 5, pady = 5)
        dni_texto_eliminar.pack(     side = "top",     fill = "x", padx = 5, pady = 5)
        dni_entry_eliminar.pack(     side = "top",     fill = "x", padx = 15, pady = 5)
        btn_eliminar.pack(           side = "bottom",  fill = "x", padx = 5, pady = 5)

    def sucursales_frame():

        def obtener_datos_añadir():
            barrio_añadir      = barrio_entry_añadir.get()
            calle_añadir       = calle_entry_añadir.get()
            altura_añadir      = altura_entry_añadir.get()
            estado_añadir      = estado_entry_añadir.get()

            while True:

                if barrio_añadir == "":
                    alerta("Barrio incompleto", "El campo del barrio de la sucursal se encuentra vacio.")
                    break
                
                else:
                    barrio_añadir2 = barrio_añadir.replace(" ", "")
                    if barrio_añadir2.isalpha():
                        barrio_añadir.replace(" ", "_")

                        if len(barrio_añadir) < 3:
                            alerta("El barrio es muy corto", "El barrio de la sucursal es muy corto como para ser un barrio.")
                            return error
                                        
                        if len(barrio_añadir) > 30:
                            alerta("El barrio es muy largo", "El barrio de la sucursal es muy largo, como maximo 30 color_letras")
                            return error
                    else:
                        alerta("El barrio es incorrecto", "El barrio de la sucursal debe conformarse unicamente por color_letras.")
                        break
                    
                    if calle_añadir == "":
                        alerta("Calle incompleta", "El campo de la calle de la sucursal se encuentra vacio.")
                        break

                    else:
                        calle_añadir2 = calle_añadir.replace(" ", "")
                        if calle_añadir2.isalpha():
                            calle_añadir.replace(" ", "_")

                            if len(calle_añadir) < 3:
                                alerta("La calle es muy corta", "La calle de la sucursal es muy corta como para ser una calle.")
                                return error
                                        
                            if len(calle_añadir) > 30:
                                alerta("La calle es muy larga", "La calle de la sucursal es muy larga, como maximo 30 color_letras")
                                return error
                            
                        else:
                            alerta("La calle es incorrecta", "La calle de la sucursal debe conformarse unicamente por color_letras.")
                            break

                        if altura_añadir == "":
                            alerta("La altura esta incompleta", "La altura de la calle de la sucursal se encuentra vacia.")
                            break

                        else:
                            if altura_añadir.isnumeric():
                                if len(altura_añadir) < 1:
                                    alerta("La altura es muy corta", "La altura de la calle es muy corta.")
                                    return error
                                            
                                if len(altura_añadir) > 4:
                                    alerta("La altura es muy larga", "La altura de la calle de la sucursal es muy grande.")
                                    return error
                            
                            else:
                                alerta("La altura es incorrecta", "La altura de la calle de la sucursal debe conformarse unicamente por 4 numeros.")
                                break

                            if estado_añadir == "~~~ Estados a seleccionar ~~~":
                                alerta("Estado incompleto", "El campo del estado de la sucursal se encuentra vacio.")
                                break
                            
                            else:
                                
                                if pregunta_si_no("Confirmacion de datos", f'¿Están correctos los siguientes datos de la sucursal?\n● Barrio: "{barrio_añadir}"\n● Calle: "{calle_añadir}"\n● Altura: "{altura_añadir}"\n● Estado: "{estado_añadir}"'):
                                    conn = sqlite3.connect("Balines_mojados.db")
                                    cursor = conn.cursor()
                                    consulta = "INSERT INTO sucursales (barrio, calle, altura, estado) VALUES (?, ?, ?, ?);"
                                    datos = (barrio_añadir, calle_añadir, altura_añadir, estado_añadir)
                                    cursor.execute(consulta, datos)
                                    barrio_entry_añadir.delete(0, tk.END)
                                    calle_entry_añadir.delete(0, tk.END)
                                    altura_entry_añadir.delete(0, tk.END)
                                    estado_entry_añadir.current(0)
                                    conn.commit()
                                    informacion("Procesado satisfactoriamente","Eliminacion de datos completada.")
                                    break
                                else:
                                    informacion("Procesado cancelado satisfactoriamente","Eliminacion de datos cancelada.")
                                    break

        def obtener_datos_modificar():
            barrio_modificar      = sucursal_entry_modificar.get()
            calle_modificar       = calle_entry_modificar.get()
            altura_modificar      = altura_entry_modificar.get()
            estado_modificar      = estado_entry_modificar.get()

            while True:
                if barrio_modificar == "~~~ Sucursal a seleccionar ~~~":
                    alerta("Barrio incompleto", "El campo del barrio de la sucursal se encuentra vacio.")
                    break
                else:
                    if calle_modificar == "":
                        alerta("Calle incompleta", "El campo de la calle de la sucursal se encuentra vacio.")
                        break

                    else:
                        calle_modificar2 = calle_modificar.replace(" ", "")
                        if calle_modificar2.isalpha():
                            calle_modificar.replace(" ", "_")

                            if len(calle_modificar) < 3:
                                alerta("La calle es muy corta", "La calle de la sucursal es muy corta como para ser una calle.")
                                return error
                                        
                            if len(calle_modificar) > 30:
                                alerta("La calle es muy larga", "La calle de la sucursal es muy larga, como maximo 30 color_letras")
                                return error
                            
                        else:
                            alerta("La calle es incorrecta", "La calle de la sucursal debe conformarse unicamente por color_letras.")
                            break

                        if altura_modificar == "":
                            alerta("La altura esta incompleta", "La altura de la calle de la sucursal se encuentra vacia.")
                            break

                        else:
                            if altura_modificar.isnumeric():
                                if len(altura_modificar) < 1:
                                    alerta("La altura es muy corta", "La altura de la calle es muy corta.")
                                    return error
                                            
                                if len(altura_modificar) > 4:
                                    alerta("La altura es muy larga", "La altura de la calle de la sucursal es muy grande.")
                                    return error
                            
                            else:
                                alerta("La altura es incorrecta", "La altura de la calle de la sucursal debe conformarse unicamente por 4 numeros.")
                                break

                            if estado_modificar == "~~~ Estados a seleccionar ~~~":
                                alerta("Estado incompleto", "El campo del estado de la sucursal se encuentra vacio.")
                                break
                            
                            else:
                                
                                if pregunta_si_no("Confirmacion de datos", f'¿Están correctos los siguientes datos de la sucursal?\n● Calle: "{calle_modificar}"\n● Altura: "{altura_modificar}"\n● Estado: "{estado_modificar}"'):
                                    conn = sqlite3.connect("Balines_mojados.db")
                                    cursor = conn.cursor()
                                    
                                    consulta = "UPDATE sucursales SET calle = ?, altura = ?, estado = ? WHERE barrio = ?;"
                                    datos = ( calle_modificar, altura_modificar, estado_modificar, barrio_modificar)
                                    cursor.execute(consulta, datos)
                                    
                                    sucursal_entry_modificar.current(0)
                                    calle_entry_modificar.delete(0, tk.END)
                                    altura_entry_modificar.delete(0, tk.END)
                                    estado_entry_modificar.current(0)
                                    conn.commit()
                                    
                                    informacion("Procesado satisfactoriamente","Añadicion de datos completada.")
                                    break
                                else:
                                    informacion("Procesado cancelado satisfactoriamente","Añadicion de datos cancelada.")
                                    break
        
        def obtener_datos_eliminar():
            barrio_eliminar = sucursal_entry_eliminar.get()

            while True:

                if barrio_eliminar == "":
                    alerta("Barrio incompleto", "El campo del barrio de la sucursal se encuentra vacio.")
                    break
                
                else:
                    barrio_eliminar2 = barrio_eliminar.replace(" ", "")
                    if barrio_eliminar2.isalpha():
                        barrio_eliminar.replace(" ", "_")

                        if len(barrio_eliminar) < 3:
                            alerta("El barrio es muy corto", "El barrio de la sucursal es muy corto como para ser un barrio.")
                            return error
                                        
                        if len(barrio_eliminar) > 30:
                            alerta("El barrio es muy largo", "El barrio de la sucursal es muy largo, como maximo 30 color_letras")
                            return error

                        if pregunta_si_no("Confirmacion de eliminacion", f'¿Estas seguro de eliminar la sucursal?'):
                                conn = sqlite3.connect("Balines_mojados.db")
                                cursor = conn.cursor()

                                peticion_calle = "SELECT calle FROM sucursales WHERE barrio = ?;"
                                datos_calle = (barrio_eliminar,)
                                cursor.execute(peticion_calle,)
                                calle = cursor.fetchone()
                                
                                peticion_altura = "SELECT altura FROM sucursales WHERE barrio = ?;"
                                datos_altura = (barrio_eliminar,)
                                cursor.execute(peticion_altura, datos_altura)
                                altura = cursor.fetchone()

                                calle_eliminar = calle[0]
                                altura_eliminar = altura[0]
                                consulta = 'UPDATE sucursales SET estado = "eliminada" WHERE barrio = ?;'
                                datos = (barrio_eliminar,)
                                cursor.execute(consulta, datos)
                                conn.commit()
                                
                                informacion("Procesado satisfactoriamente","Añadicion de datos completada.")
                                
                                cursor.execute("SELECT dni FROM personal WHERE barrio = ?, calle = ?;")
                                datos = (barrio_sucursal,)
                                cursor.execute(peticion, datos)
                                dni_personal_sucursal_eliminar = cursor.fetchall()
                                conn.close()
                                
                                break
                        

                    else:
                        alerta("El barrio es incorrecto", "El barrio de la sucursal debe conformarse unicamente por color_letras.")
                        break


        estados = ["~~~ Estados a seleccionar ~~~", "Activa", "Inactiva", "Suspendida",  "Renovaciones"]

        sucursales = lista_barrios_sucursales()

        for x in range(3):
            frame_principal.grid_columnconfigure(x, weight = 1)
        frame_principal.grid_rowconfigure(0, weight = 1)
        
        frame_añadir      = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_modificar   = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_eliminar    = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)

        frame_añadir.grid(     column = 0, row = 0, sticky = "nsew", pady = (5, 0), padx = (0, 5))
        frame_modificar.grid(  column = 1, row = 0, sticky = "nsew", pady = (5, 0), padx = (0, 5))
        frame_eliminar.grid(   column = 2, row = 0, sticky = "nsew", pady = (5, 0))

        for x in range(15):
            frame_añadir.grid_rowconfigure(x, weight = 1)
        frame_añadir.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_modificar.grid_rowconfigure(x, weight = 1)
        frame_modificar.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_eliminar.grid_rowconfigure(x, weight = 1)
        frame_eliminar.grid_columnconfigure(0, weight = 1)

          ####################################################
         #    DECLARACION DE ELEMENTOS AÑADIR SUCURSALES    #
        ####################################################
        
        encabezado_añadir          = tk.Label(      frame_añadir, text = "AÑADIR SUCURSAL", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
            
        barrio_texto_añadir        = tk.Label(      frame_añadir, text = "Barrio de la sucursal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        barrio_entry_añadir        = tk.Entry(      frame_añadir, font = (tipografia, h7))
            
        calle_texto_añadir         = tk.Label(      frame_añadir, text = "Calle de la sucursal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        calle_entry_añadir         = tk.Entry(      frame_añadir, font = (tipografia, h7))
            
        altura_texto_añadir        = tk.Label(      frame_añadir, text = "Numero de la calle:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        altura_entry_añadir        = tk.Entry(      frame_añadir, font = (tipografia, h7))
        
        estado_texto_añadir        = tk.Label(      frame_añadir, text = "Estado de la sucursal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        
        estado_entry_añadir       = ttk.Combobox(   frame_añadir, values = estados, state = "readonly", font = (tipografia, h7))
        estado_entry_añadir.current(0)

        btn_añadir                 = tk.Button(     frame_añadir, text = "AÑADIR SUCURSAL", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_añadir)
        
          ###################################################
         #    COLOCACION DE ELEMENTOS AÑADIR SUCURSALES    #
        ###################################################
        encabezado_añadir.grid(      column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)

        barrio_texto_añadir.grid(    column = 0, row = 1, sticky = "nsew")
        barrio_entry_añadir.grid(    column = 0, row = 2, sticky = "ew", padx = 15)
    
        calle_texto_añadir.grid(     column = 0, row = 3, sticky = "nsew")
        calle_entry_añadir.grid(     column = 0, row = 4, sticky = "ew", padx = 15)
    
        altura_texto_añadir.grid(    column = 0, row = 5, sticky = "nsew")
        altura_entry_añadir.grid(    column = 0, row = 6, sticky = "ew", padx = 15)

        estado_texto_añadir.grid(    column = 0, row = 7, sticky = "nsew")
        estado_entry_añadir.grid(    column = 0, row = 8, sticky = "ew", padx = 15)

        btn_añadir.grid(             column = 0, row = 15, sticky = "nsew", padx = 5, pady = 5)
        
        
          #######################################################
         #    DECLARACION DE ELEMENTOS MODIFICAR SUCURSALES    #
        #######################################################
        encabezado_modificar       = tk.Label(frame_modificar, text = "MODIFICAR SUCURSAL", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        
        sucursal_texto_modificar   = tk.Label(frame_modificar, text = "Sucursal a modificar:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_modificar   = ttk.Combobox(frame_modificar, values = sucursales, state = "readonly", font = (tipografia, h7))
        sucursal_entry_modificar.current(0)
        
        calle_texto_modificar      = tk.Label(frame_modificar, text = "Calle de la sucursal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        calle_entry_modificar      = tk.Entry(frame_modificar, font = (tipografia, h7))
        
        altura_texto_modificar     = tk.Label(frame_modificar, text = "Altura de la calle:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        altura_entry_modificar     = tk.Entry(frame_modificar, font = (tipografia, h7))

        estado_texto_modificar = tk.Label(frame_modificar, text = "Estado de la sucursal:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        estado_entry_modificar = ttk.Combobox(frame_modificar, values = estados, state = "readonly", font = (tipografia, h7))
        estado_entry_modificar.current(0)
        
        btn_modificar               = tk.Button(frame_modificar, text = "GUARDAR DATOS DE LA SUCURSAL", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_modificar)
        

          #####################################################
         #    COLOCACION DE ELEMENTOS ELIMINAR SUCURSALES    #
        #####################################################
        encabezado_modificar.grid(        column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)
        
        sucursal_texto_modificar.grid(    column = 0, row = 1, sticky = "nsew")
        sucursal_entry_modificar.grid(    column = 0, row = 2, sticky = "ew", padx = 15)
        
        calle_texto_modificar.grid(       column = 0, row = 3, sticky = "nsew")
        calle_entry_modificar.grid(       column = 0, row = 4, sticky = "ew", padx = 15)
        
        altura_texto_modificar.grid(      column = 0, row = 5, sticky = "nsew")
        altura_entry_modificar.grid(      column = 0, row = 6, sticky = "ew", padx = 15)

        estado_texto_modificar.grid(      column = 0, row = 7, sticky = "nsew")
        estado_entry_modificar.grid(      column = 0, row = 8, sticky = "ew", padx = 15)
        
        btn_modificar.grid(               column = 0, row = 15, sticky = "nsew", padx = 5, pady = 5)

          #######################################################
         #    DECLARACION DE ELEMENTOS ELIMINAR SUCURSALES    #
        #######################################################
        encabezado_eliminar              = tk.Label(frame_eliminar, text = "ELIMINAR SUCURSAL", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        sucursal_texto_eliminar          = tk.Label(frame_eliminar, text = "Sucursal a eliminar:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_eliminar          = ttk.Combobox(frame_eliminar, values = sucursales, state = "readonly", font = (tipografia, h7))
        sucursal_entry_eliminar.current(0)
        btn_eliminar                     = tk.Button(frame_eliminar, text = "ELIMINAR SUCURSAL", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_eliminar)
        

          #####################################################
         #    COLOCACION DE ELEMENTOS ELIMINAR SUCURSALES    #
        #####################################################
        encabezado_eliminar.grid(         column = 0, row = 0, sticky = "nsew")
        sucursal_texto_eliminar.grid(     column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)
        sucursal_entry_eliminar.grid(     column = 0, row = 2, sticky = "ew", padx = 15)
        btn_eliminar.grid(                column = 0, row = 15, sticky = "nsew", padx = 5, pady = 5)

    def canchas_frame():

        def obtener_datos_añadir():
            sucursal_añadir      = sucursal_entry_añadir.get()
            tamaño_añadir        = tamaño_entry_añadir.get()
            tipo_añadir          = tipo_entry_añadir.get()
            obstaculos_añadir    = obstaculos_entry_añadir.get()
            min_jug_añadir       = min_jug_entry_añadir.get()
            max_jug_añadir       = max_jug_entry_añadir.get()
            terreno_añadir       = terreno_entry_añadir.get()
            ancho_añadir         = ancho_entry_añadir.get()
            largo_añadir         = largo_entry_añadir.get()
            medidas_añadir       = f"{ancho_añadir}x{largo_añadir}"
            estado_añadir        = estado_entry_añadir.get()

            while True:
                if sucursal_añadir == "~~~ Sucursal a seleccionar ~~~":
                    alerta("Sucursal incompleta", "El campo de la sucursal se encuentra vacio.")
                    break

                else:
                    if tamaño_añadir == "~~~ Tamaño a seleccionar ~~~":
                        alerta("Tamaño incompleto", "El campo del tamaño se encuentra vacio.")
                        break

                    else:
                        if tipo_añadir == "~~~ Tipo a seleccionar ~~~":
                            alerta("Tipo incompleto", "El campo del tipo se encuentra vacio.")
                            break

                        else:
                            if obstaculos_añadir == "~~~ Obstaculos a seleccionar ~~~":
                                alerta("Obstaculos incompleto", "El campo de obstaculos se encuentra vacio.")
                                break
                            
                            else:
                                if min_jug_añadir > max_jug_añadir:
                                    alerta("Jugadores incorrectos", "El campo de minimos jugadores debe ser mayor a el maximo jugadores.")
                                    break
                                else:
                                    if terreno_añadir == "~~~ Terreno a seleccionar ~~~":
                                        alerta("Terreno incompleto", "El campo de terreno se encuentra vacio.")
                                        break
                                    
                                    else:
                                        if pregunta_si_no("Confirmacion de datos", f'¿Están correctos los siguientes datos?\n● Sucursal: "{sucursal_añadir}"\n● Tamaño: "{tamaño_añadir}"\n● Tipo de cancha: "{tipo_añadir}"\n● Obstaculos: "{obstaculos_añadir}"\n● Estado: {estado_añadir}'):
                                            conn = sqlite3.connect("Balines_mojados.db")
                                            cursor = conn.cursor()

                                            consulta = "INSERT INTO canchas (id_sucursal, tamaño, tipo, obstaculos, min_jugadores, max_jugadores, terreno, medidas, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
                                            id_sucursal_añadir = barrio_sucursal_a_id_sucursal(sucursal_añadir)
                                            datos = (id_sucursal_añadir, tamaño_añadir, tipo_añadir, obstaculos_añadir, min_jug_añadir, max_jug_añadir, terreno_añadir, medidas_añadir, estado_añadir)

                                            cursor.execute(consulta, datos)
                                            conn.commit()
                                            informacion("Procesado satisfactoriamente", "Cancha agregada correctamente a la base de datos.")
                                            break
                                        else:
                                            informacion("Procesado cancelado satisfactoriamente","Añadicion de datos cancelada.")
                                            break
                                    
        def obtener_datos_modificar():
            sucursal_modificar      = sucursal_entry_modificar.get()
            tamaño_modificar       = tamaño_entry_modificar.get()
            tipo_modificar         = tipo_entry_modificar.get()
            obstaculos_modificar   = obstaculos_entry_modificar.get()
            min_jug_modificar      = min_jug_entry_modificar.get()
            max_jug_modificar      = max_jug_entry_modificar.get()
            terreno_modificar      = terreno_entry_modificar.get()
            ancho_modificar        = ancho_entry_modificar.get()
            largo_modificar        = largo_entry_modificar.get()
            medidas_modificar      = f"{ancho_modificar}x{largo_modificar}"
            estado_modificar       = estado_entry_modificar.get()

            while True:
                if sucursal_modificar == "~~~ Sucursal a seleccionar ~~~":
                    alerta("Sucursal incompleta", "El campo de la sucursal se encuentra vacio.")
                    break

                else:
                    if tamaño_modificar == "~~~ Tamaño a seleccionar ~~~":
                        alerta("Tamaño incompleto", "El campo del tamaño se encuentra vacio.")
                        break

                    else:
                        if tipo_modificar == "~~~ Tipo a seleccionar ~~~":
                            alerta("Tipo incompleto", "El campo del tipo se encuentra vacio.")
                            break

                        else:
                            if obstaculos_modificar == "~~~ Obstaculos a seleccionar ~~~":
                                alerta("Obstaculos incompleto", "El campo de obstaculos se encuentra vacio.")
                                break
                            
                            else:
                                if min_jug_modificar > max_jug_modificar:
                                    alerta("Jugadores incorrectos", "El campo de minimos jugadores debe ser mayor a el maximo jugadores.")
                                    break
                                else:
                                    if terreno_modificar == "~~~ Terreno a seleccionar ~~~":
                                        alerta("Terreno incompleto", "El campo de terreno se encuentra vacio.")
                                        break
                                    
                                    else:
                                        if pregunta_si_no("Confirmacion de datos", f'¿Están correctos los siguientes datos?\n● Sucursal: "{sucursal_modificar}"\n● Tamaño: "{tamaño_modificar}"\n● Tipo de cancha: "{tipo_modificar}"\n● Obstaculos: "{obstaculos_modificar}"\n● Estado: {estado_modificar}'):
                                            conn = sqlite3.connect("Balines_mojados.db")
                                            cursor = conn.cursor()

                                            consulta = "INSERT INTO canchas (id_sucursal, tamaño, tipo, obstaculos, min_jugadores, max_jugadores, terreno, medidas, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
                                            id_sucursal_modificar = barrio_sucursal_a_id_sucursal(sucursal_modificar)
                                            datos = (id_sucursal_modificar, tamaño_modificar, tipo_modificar, obstaculos_modificar, min_jug_modificar, max_jug_modificar, terreno_modificar, medidas_modificar, estado_modificar)

                                            cursor.execute(consulta, datos)
                                            conn.commit()
                                            informacion("Procesado satisfactoriamente", "Cancha agregada correctamente a la base de datos.")
                                            break
                                        else:
                                            informacion("Procesado cancelado satisfactoriamente","Añadicion de datos cancelada.")
                                            break


        sucursales        = lista_barrios_sucursales()
        tamaño_cancha     = ["~~~ Tamaño a seleccionar ~~~", "Grande", "Mediana", "Chica"]
        tipo_cancha       = ["~~~ Tipo a seleccionar ~~~", "Speedball", "Recball", "Woodsball"]
        obstaculos        = ["~~~ Obstaculos a seleccionar ~~~", "Artificiales", "Naturales"]
        terreno           = ["~~~ Terreno a seleccionar ~~~", "Tierra", "Pasto sintetico", "Cemento", "Polvo de ladrillo"]
        estados           = ["~~~ Estados a seleccionar ~~~", "Activa", "Inactiva", "Suspendida",  "Renovaciones"]

        
        for x in range(3):
            frame_principal.grid_columnconfigure(x, weight = 1)
        frame_principal.grid_rowconfigure(0, weight = 1)

        frame_añadir      = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_modificar   = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_eliminar    = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        
        frame_añadir.grid(     column = 0, row = 0, sticky = "nsew", pady = (5,0), padx = (0, 5))
        frame_modificar.grid(  column = 1, row = 0, sticky = "nsew", pady = (5,0), padx = (0, 5))
        frame_eliminar.grid(   column = 2, row = 0, sticky = "nsew", pady = (5,0))

        for x in range(15):
            frame_añadir.grid_rowconfigure(x, weight = 1)
        frame_añadir.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_modificar.grid_rowconfigure(x, weight = 1)
        frame_modificar.grid_columnconfigure(0, weight = 1)

        for x in range(15):
            frame_eliminar.grid_rowconfigure(x, weight = 1)
        frame_eliminar.grid_columnconfigure(0, weight = 1)


          #################################################
         #    DECLARACION DE ELEMENTOS AÑADIR CANCHAS    #
        #################################################
        encabezado_añadir             = tk.Label(frame_añadir, text = "AÑADIR CANCHA", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        
        sucursal_texto_añadir         = tk.Label(frame_añadir, text = "Sucursal de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_añadir         = ttk.Combobox(frame_añadir, values = sucursales, state = "readonly", font = (tipografia, h7), justify = "center")
        sucursal_entry_añadir.current(0)
        

        tamaño_texto_añadir           = tk.Label(frame_añadir, text = "Tamaño de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        tamaño_entry_añadir           = ttk.Combobox(frame_añadir, values = tamaño_cancha, state = "readonly", font = (tipografia, h7), justify = "center")
        tamaño_entry_añadir.current(0)
        
        tipo_texto_añadir             = tk.Label(frame_añadir, text = "Tipo de cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        tipo_entry_añadir             = ttk.Combobox(frame_añadir, values = tipo_cancha, state = "readonly", font = (tipografia, h7), justify = "center")
        tipo_entry_añadir.current(0)

        obstaculos_texto_añadir       = tk.Label(frame_añadir, text = "Obstaculos de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        obstaculos_entry_añadir       = ttk.Combobox(frame_añadir, values = obstaculos, state = "readonly", font = (tipografia, h7), justify = "center")
        obstaculos_entry_añadir.current(0)

        frame_jugadores               = tk.Frame(frame_añadir, bg = color_secundario)
        min_jug_texto_añadir          = tk.Label(frame_jugadores, text = "Minimo numero de jugadores:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        min_jug_entry_añadir          = tk.Spinbox(frame_jugadores, from_= 2, to = 20, format="%2.0f", increment = 2, font = (tipografia, h7), state="readonly", justify = "center")

        max_jug_texto_añadir          = tk.Label(frame_jugadores, text = "Maximos numero de jugadores:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        max_jug_entry_añadir          = tk.Spinbox(frame_jugadores, from_= 4, to = 40, format="%2.0f", increment = 2, font = (tipografia, h7), state="readonly", justify = "center")

        terreno_texto_añadir          = tk.Label(frame_añadir, text = "Terreno de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        terreno_entry_añadir          = ttk.Combobox(frame_añadir, values = terreno, state = "readonly", font = (tipografia, h7), justify = "center")
        terreno_entry_añadir.current(0)

        medidas_texto_añadir          = tk.Label(frame_añadir, text = "Medidas de la cancha (en metros):", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        
        frame_medidas_añadir          = tk.Frame(frame_añadir, bg = color_secundario)
        
        ancho_texto_añadir            = tk.Label(frame_medidas_añadir, text = "Ancho:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        ancho_entry_añadir            = tk.Spinbox(frame_medidas_añadir, from_=10, to=130, format="%3.0f", increment = 5, font = (tipografia, h7), state="readonly", justify = "center")
        
        largo_texto_añadir            = tk.Label(frame_medidas_añadir, text = "Largo:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        largo_entry_añadir            = tk.Spinbox(frame_medidas_añadir, from_=10, to=130, format="%3.0f", increment = 5, font = (tipografia, h7), state="readonly", justify = "center")

        estado_texto_añadir           = tk.Label(frame_añadir, text = "Estado de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        estado_entry_añadir           = ttk.Combobox(frame_añadir, values = estados, state = "readonly", font = (tipografia, h7), justify = "center")
        estado_entry_añadir.current(0)

        btn_añadir    = tk.Button(frame_añadir, text = "AÑADIR CANCHA", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_añadir)
        
        for x in range(2):
            frame_medidas_añadir.grid_rowconfigure(x, weight = 1)
            frame_medidas_añadir.grid_columnconfigure(x, weight = 1)
        
        for x in range(2):
            frame_jugadores.grid_rowconfigure(x, weight = 1)
            frame_jugadores.grid_columnconfigure(x, weight = 1)

          ################################################
         #    COLOCACION DE ELEMENTOS AÑADIR CANCHAS    #
        ################################################
        encabezado_añadir.grid(        column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)
        
        sucursal_texto_añadir.grid(    column = 0, row = 1, sticky = "nsew")
        sucursal_entry_añadir.grid(    column = 0, row = 2, sticky = "ew", padx = 15)
        
        tamaño_texto_añadir.grid(      column = 0, row = 3, sticky = "nsew")
        tamaño_entry_añadir.grid(      column = 0, row = 4, sticky = "ew", padx = 15)
        
        tipo_texto_añadir.grid(        column = 0, row = 5, sticky = "nsew")
        tipo_entry_añadir.grid(        column = 0, row = 6, sticky = "ew", padx = 15)
        
        obstaculos_texto_añadir.grid(  column = 0, row = 7, sticky = "nsew")
        obstaculos_entry_añadir.grid(  column = 0, row = 8, sticky = "ew", padx = 15)
        
        frame_jugadores.grid(     column = 0, row = 9, sticky = "nsew")

        min_jug_texto_añadir.grid(     column = 0, row = 0, sticky = "nsew")
        min_jug_entry_añadir.grid(     column = 0, row = 1, sticky = "ew", padx = 15)
        
        max_jug_texto_añadir.grid(     column = 1, row = 0, sticky = "nsew")
        max_jug_entry_añadir.grid(     column = 1, row = 1, sticky = "ew", padx = 15)
             
        terreno_texto_añadir.grid(     column = 0, row = 10, sticky = "nsew")
        terreno_entry_añadir.grid(     column = 0, row = 11, sticky = "ew", padx = 15)
             
        medidas_texto_añadir.grid(     column = 0, row = 12, sticky = "ew", padx = 15)
        frame_medidas_añadir.grid(     column = 0, row = 13, sticky = "nsew", padx = 15)

        ancho_texto_añadir.grid(       column = 0, row = 0, sticky = "nsew")
        ancho_entry_añadir.grid(       column = 0, row = 1, sticky = "ew", padx = (0,5))
  
        largo_texto_añadir.grid(       column = 1, row = 0, sticky = "nsew")
        largo_entry_añadir.grid(       column = 1, row = 1, sticky = "ew", padx = (5,0))

        estado_texto_añadir.grid(      column = 0, row = 14, sticky = "nsew", padx = (5,0))
        estado_entry_añadir.grid(      column = 0, row = 15, sticky = "ew", padx = (5,0))
        
        btn_añadir.grid(               column = 0, row = 17, sticky = "nsew", padx = 5, pady = 5)

          ####################################################
         #    DECLARACION DE ELEMENTOS modificar CANCHAS    #
        ####################################################
        encabezado_modificar             = tk.Label(frame_modificar, text = "MODIFICAR CANCHA", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        
        sucursal_texto_modificar         = tk.Label(frame_modificar, text = "Sucursal de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        sucursal_entry_modificar         = ttk.Combobox(frame_modificar, values = sucursales, state = "readonly", font = (tipografia, h7), justify = "center")
        sucursal_entry_modificar.current(0)
        

        tamaño_texto_modificar           = tk.Label(frame_modificar, text = "Tamaño de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        tamaño_entry_modificar           = ttk.Combobox(frame_modificar, values = tamaño_cancha, state = "readonly", font = (tipografia, h7), justify = "center")
        tamaño_entry_modificar.current(0)
        
        tipo_texto_modificar             = tk.Label(frame_modificar, text = "Tipo de cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        tipo_entry_modificar             = ttk.Combobox(frame_modificar, values = tipo_cancha, state = "readonly", font = (tipografia, h7), justify = "center")
        tipo_entry_modificar.current(0)

        obstaculos_texto_modificar       = tk.Label(frame_modificar, text = "Obstaculos de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        obstaculos_entry_modificar       = ttk.Combobox(frame_modificar, values = obstaculos, state = "readonly", font = (tipografia, h7), justify = "center")
        obstaculos_entry_modificar.current(0)

        frame_jugadores               = tk.Frame(frame_modificar, bg = color_secundario)
        min_jug_texto_modificar          = tk.Label(frame_jugadores, text = "Minimo numero de jugadores:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        min_jug_entry_modificar          = tk.Spinbox(frame_jugadores, from_= 2, to = 20, format="%2.0f", increment = 2, font = (tipografia, h7), state="readonly", justify = "center")

        max_jug_texto_modificar          = tk.Label(frame_jugadores, text = "Maximos numero de jugadores:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        max_jug_entry_modificar          = tk.Spinbox(frame_jugadores, from_= 4, to = 40, format="%2.0f", increment = 2, font = (tipografia, h7), state="readonly", justify = "center")

        terreno_texto_modificar          = tk.Label(frame_modificar, text = "Terreno de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        terreno_entry_modificar          = ttk.Combobox(frame_modificar, values = terreno, state = "readonly", font = (tipografia, h7), justify = "center")
        terreno_entry_modificar.current(0)

        medidas_texto_modificar          = tk.Label(frame_modificar, text = "Medidas de la cancha (en metros):", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        
        frame_medidas_modificar          = tk.Frame(frame_modificar, bg = color_secundario)
        
        ancho_texto_modificar            = tk.Label(frame_medidas_modificar, text = "Ancho:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        ancho_entry_modificar            = tk.Spinbox(frame_medidas_modificar, from_=10, to=130, format="%3.0f", increment = 5, font = (tipografia, h7), state="readonly", justify = "center")
        
        largo_texto_modificar            = tk.Label(frame_medidas_modificar, text = "Largo:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        largo_entry_modificar            = tk.Spinbox(frame_medidas_modificar, from_=10, to=130, format="%3.0f", increment = 5, font = (tipografia, h7), state="readonly", justify = "center")

        estado_texto_modificar           = tk.Label(frame_modificar, text = "Estado de la cancha:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        estado_entry_modificar           = ttk.Combobox(frame_modificar, values = estados, state = "readonly", font = (tipografia, h7), justify = "center")
        estado_entry_modificar.current(0)

        btn_modificar    = tk.Button(frame_modificar, text = "GUARDAR DATOS", foreground = color_letras, bg = color_secundario, font = (tipografia, h7), relief = "ridge", activebackground = color_boton_activo, border = 2, command = obtener_datos_añadir)
        
        for x in range(2):
            frame_medidas_modificar.grid_rowconfigure(x, weight = 1)
            frame_medidas_modificar.grid_columnconfigure(x, weight = 1)
        
        for x in range(2):
            frame_jugadores.grid_rowconfigure(x, weight = 1)
            frame_jugadores.grid_columnconfigure(x, weight = 1)

          ###################################################
         #    COLOCACION DE ELEMENTOS MODIFICAR CANCHAS    #
        ###################################################
        encabezado_modificar.grid(        column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)
        
        sucursal_texto_modificar.grid(    column = 0, row = 1, sticky = "nsew")
        sucursal_entry_modificar.grid(    column = 0, row = 2, sticky = "ew", padx = 15)
        
        tamaño_texto_modificar.grid(      column = 0, row = 3, sticky = "nsew")
        tamaño_entry_modificar.grid(      column = 0, row = 4, sticky = "ew", padx = 15)
        
        tipo_texto_modificar.grid(        column = 0, row = 5, sticky = "nsew")
        tipo_entry_modificar.grid(        column = 0, row = 6, sticky = "ew", padx = 15)
        
        obstaculos_texto_modificar.grid(  column = 0, row = 7, sticky = "nsew")
        obstaculos_entry_modificar.grid(  column = 0, row = 8, sticky = "ew", padx = 15)
        
        frame_jugadores.grid(     column = 0, row = 9, sticky = "nsew")

        min_jug_texto_modificar.grid(     column = 0, row = 0, sticky = "nsew")
        min_jug_entry_modificar.grid(     column = 0, row = 1, sticky = "ew", padx = 15)
        
        max_jug_texto_modificar.grid(     column = 1, row = 0, sticky = "nsew")
        max_jug_entry_modificar.grid(     column = 1, row = 1, sticky = "ew", padx = 15)
             
        terreno_texto_modificar.grid(     column = 0, row = 10, sticky = "nsew")
        terreno_entry_modificar.grid(     column = 0, row = 11, sticky = "ew", padx = 15)
             
        medidas_texto_modificar.grid(     column = 0, row = 12, sticky = "ew", padx = 15)
        frame_medidas_modificar.grid(     column = 0, row = 13, sticky = "nsew", padx = 15)

        ancho_texto_modificar.grid(       column = 0, row = 0, sticky = "nsew")
        ancho_entry_modificar.grid(       column = 0, row = 1, sticky = "ew", padx = (0,5))
  
        largo_texto_modificar.grid(       column = 1, row = 0, sticky = "nsew")
        largo_entry_modificar.grid(       column = 1, row = 1, sticky = "ew", padx = (5,0))

        estado_texto_modificar.grid(      column = 0, row = 14, sticky = "nsew", padx = (5,0))
        estado_entry_modificar.grid(      column = 0, row = 15, sticky = "ew", padx = (5,0))
        
        btn_modificar.grid(               column = 0, row = 17, sticky = "nsew", padx = 5, pady = 5)       
        

    def reservas_frame():
        desempeño = ["~~~ Desempeño a seleccionar ~~~", "Recepcionista", "Referi", "Equipamiento","Seguridad", "Administrador"]
        
        for x in range(3):
            frame_principal.grid_columnconfigure(x, weight = 1)
        frame_principal.grid_rowconfigure(0, weight = 1)

        frame_añadir      = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_modificar   = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)
        frame_eliminar    = tk.Frame(frame_principal, background = color_secundario, highlightcolor = color_marcos, highlightthickness = 1)

        frame_añadir.grid(     column = 0, row = 0, sticky = "nsew", pady = (5, 0), padx = (0, 5))
        frame_modificar.grid(  column = 1, row = 0, sticky = "nsew", pady = (5, 0), padx = (0, 5))
        frame_eliminar.grid(   column = 2, row = 0, sticky = "nsew", pady = (5, 0))

        añadir_texto               = tk.Label(frame_añadir, text="AÑADIR RESERVA", border = 1, foreground = color_letras, bg = color_secundario, font = (tipografia, h7), highlightthickness = 1, highlightcolor = color_marcos, highlightbackground = color_marcos)
        dni_reservador_texto       = tk.Label(frame_añadir, text="Dni del reservador:", foreground = color_letras, bg = color_secundario, font = (tipografia, h7))
        fecha                      = DateEntry(frame_añadir, width=12, background = color_secundario, foreground = color_principal, borderwidth=2)
        spinbox_hora               = tk.Spinbox(frame_añadir, from_=8, to=23, format="%02.0f", state='normal')
        spinbox_minuto             = tk.Spinbox(frame_añadir, from_=8, to=23, format="%02.0f", state='normal')
        dni_reservador             = tk.Entry(frame_añadir, foreground = color_letras, bg = color_secundario, font = (tipografia, h7))

        añadir_texto.grid(column = 0, row = 0, sticky = "nsew", padx = 5, pady = 5)
        dni_reservador_texto.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady = 5)
        fecha.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady = 5)
        spinbox_hora.grid(column = 0, row = 3, sticky = "nsew", padx = 5, pady = 5)
        spinbox_minuto.grid(column = 0, row = 4, sticky = "nsew", padx = 5, pady = 5)
        dni_reservador.grid(column = 0, row = 5, sticky = "ew", padx = 5, pady = 5)
        

    conn = sqlite3.connect("Balines_mojados.db")
    cursor = conn.cursor()
    ventana = tk.Tk()
    ancho_pantalla, alto_pantalla = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
    ancho_ventana_inicial = int(((alto_pantalla / 1.4) * 16) / 9)
    alto_ventana_inicial =  int(((ancho_pantalla / 1.4) * 9) / 16)
    ancho_ventana, alto_ventana = ventana.winfo_width(), ventana.winfo_height()
    ventana.minsize(ancho_ventana_inicial, alto_ventana_inicial)
    ventana.geometry(f"{ancho_ventana_inicial}x{alto_ventana_inicial}")
    ventana.title("Balines Mojados - Administrador")
    ventana.grid_rowconfigure(0, weight = 1)
    ventana.grid_rowconfigure(1, weight = 30)
    ventana.grid_columnconfigure(0, weight = 1)

    frame_10_porciento = tk.Frame(ventana, background = color_principal)
    frame_10_porciento.grid(row = 0, column = 0, sticky = "nsew")

    frame_10_porciento.grid_columnconfigure(0, weight = 1)
    frame_10_porciento.grid_rowconfigure(0, weight = 1)

    frame_btn = tk.Frame(frame_10_porciento, border = 1, bg = color_marcos)
    frame_btn.grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = (10,0))

    frame_btn.grid_columnconfigure(0, weight = 1)
    frame_btn.grid_columnconfigure(1, weight = 1)
    frame_btn.grid_columnconfigure(2, weight = 1)
    frame_btn.grid_columnconfigure(3, weight = 1)

    frame_btn.grid_rowconfigure(0, weight = 1)
    
    frame_90_porciento = tk.Frame(ventana, background = color_principal)
    frame_90_porciento.grid(row = 1, column = 0, sticky = "nsew")

    frame_90_porciento.grid_columnconfigure(0, weight = 1)
    frame_90_porciento.grid_rowconfigure(0, weight = 1)

    frame_principal = tk.Frame(frame_90_porciento, background = color_principal)
    frame_principal.grid(column = 0, row = 0, sticky = "nsew", padx = 10, pady = (0,10))

    btn_personal = tk.Button(frame_btn, border = 0, text = "PERSONAL", font = (tipografia, h7), activebackground = color_boton_activo, activeforeground = color_letras, fg = color_letras, background = color_secundario, command=lambda: limpiar_frame(personal_frame))
    btn_personal.grid(column = 0, row = 0, sticky = "nsew")



    btn_sucursales = tk.Button(frame_btn, border = 0, text = "SUCURSALES", font = (tipografia, h7), activebackground = color_boton_activo, activeforeground = color_letras, fg = color_letras, background = color_secundario, command=lambda: limpiar_frame(sucursales_frame))
    btn_sucursales.grid(column = 1, row = 0, sticky = "nsew")



    btn_canchas = tk.Button(frame_btn, border = 0, text = "CANCHAS", font = (tipografia, h7), activebackground = color_boton_activo, activeforeground = color_letras, fg = color_letras, background = color_secundario, command=lambda: limpiar_frame(canchas_frame))
    btn_canchas.grid(column = 2, row = 0, sticky="nsew")



    btn_reservas = tk.Button(frame_btn, border = 0, text = "RESERVAS", font = (tipografia, h7), activebackground = color_boton_activo, activeforeground = color_letras, fg = color_letras, background = color_secundario, command=lambda: limpiar_frame(reservas_frame))
    btn_reservas.grid(column = 3, row = 0, sticky ="nsew")

    ventana.mainloop()

ventana_iniciar_sesion()
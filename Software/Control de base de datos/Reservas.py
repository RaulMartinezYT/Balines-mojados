import datetime

reservas = []

# Chequea si el local está abierto a esa hora
def local_abierto(hora):
    if (hora >= "08" and hora <= "23") or (hora >= "00" and hora <= "02"):
        return True

# Solicita la fecha de la reserva
def Obtener_fecha_reserva():
    año = str(input("Año de la reserva: "))
    mes = str(input("Mes de la reserva: "))
    dia = str(input("Dia de la reserva: "))
    hora = str(input("Hora de la reserva: "))
    minuto = str(input("Minuto de la reserva: "))
    Verificar_fecha(año, mes, dia, hora, minuto)

def Verificar_fecha(año, mes, dia, hora, minuto):
    Año_actual = datetime.datetime.now().strftime("%Y")
    Mes_actual = datetime.datetime.now().strftime("%m")
    Dia_actual = datetime.datetime.now().strftime("%d")
    Hora_actual = datetime.datetime.now().strftime("%H")
    Minuto_actual = datetime.datetime.now().strftime("%M")

    print(f"{Año_actual} \n {Mes_actual} \n {Dia_actual} \n {Hora_actual} \n {Minuto_actual}")

def Verificar_reservas():

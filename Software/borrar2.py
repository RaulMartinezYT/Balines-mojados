import datetime
from datetime import timedelta

def nombre_dia(numero_dia):
    dias_de_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    return dias_de_semana[numero_dia]

fecha_hoy = datetime.datetime.now().date()

fecha = [
        datetime.datetime.now().date(),
        fecha_hoy + timedelta(days = 1),
        fecha_hoy + timedelta(days = 2),
        fecha_hoy + timedelta(days = 3),
        fecha_hoy + timedelta(days = 4),
        fecha_hoy + timedelta(days = 5),
        fecha_hoy + timedelta(days = 6),
        fecha_hoy + timedelta(days = 7),
        fecha_hoy + timedelta(days = 8),
        fecha_hoy + timedelta(days = 9),
        ]
dia = [
    nombre_dia(fecha_hoy.weekday()),
    nombre_dia(fecha[1].weekday()),
    nombre_dia(fecha[2].weekday()),
    nombre_dia(fecha[3].weekday()),
    nombre_dia(fecha[4].weekday()),
    nombre_dia(fecha[5].weekday()),
    nombre_dia(fecha[6].weekday()),
    nombre_dia(fecha[7].weekday()),
    nombre_dia(fecha[8].weekday()),
    nombre_dia(fecha[9].weekday()),
    ]

print(f"""
        Dia actual: {dia[0]}
        fecha actual: {fecha[0].strftime("%d-%m-%Y")}\n
        Dia: {dia[1]}
        fecha: {fecha[1].strftime("%d-%m-%Y")}\n
        Dia: {dia[2]}
        fecha: {fecha[2].strftime("%d-%m-%Y")}\n
        Dia: {dia[3]}
        fecha: {fecha[3].strftime("%d-%m-%Y")}\n
        Dia: {dia[4]}
        fecha: {fecha[4].strftime("%d-%m-%Y")}\n
        Dia: {dia[5]}
        fecha: {fecha[5].strftime("%d-%m-%Y")}\n
        Dia: {dia[6]}
        fecha: {fecha[6].strftime("%d-%m-%Y")}\n
        Dia: {dia[7]}
        fecha: {fecha[7].strftime("%d-%m-%Y")}\n
        Dia: {dia[8]}
        fecha: {fecha[8].strftime("%d-%m-%Y")}\n
        Dia: {dia[9]}
        fecha: {fecha[9].strftime("%d-%m-%Y")}\n""")
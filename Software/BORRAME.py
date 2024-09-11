import sqlite3
def obtener_lista_barrios():
    conn = sqlite3.connect('Balines_mojados.db')
    cursor = conn.cursor()
    
    # Consulta para obtener todos los barrios de la tabla sucursales
    cursor.execute("SELECT barrio FROM sucursales;")
    
    # fetchall() devuelve todas las filas como una lista de tuplas
    resultados = cursor.fetchall()
    
    # Convertir los resultados a una lista plana (quitamos las tuplas)
    lista_barrios = [fila[0] for fila in resultados]
    
    conn.close()  # Cierra la conexión
    return lista_barrios

print(obtener_lista_barrios())

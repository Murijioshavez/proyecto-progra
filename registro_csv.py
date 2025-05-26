import csv

def leer_csv(archivo):
    with open('actividades.csv', newline='') as archivo:
        reader = csv.DictReader(archivo)
        lista_de_filas = list(reader)
        return lista_de_filas

def guardar_en_csv(nombre_archivo, datos, encabezados):
    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writerow(datos)
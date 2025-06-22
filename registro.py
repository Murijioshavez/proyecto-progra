import json

colores = {'Torneos Internos':"#7BBDFF", 'Deporte y Cultura': "#11FF99",'Capítulos estudiantiles':"#E1A4FF",
           "Grupos estudiantiles": "#65FFE2", "Bienestar": "#F7E16D", "Mentoría": "#8EFFA2", "Clubs estudiantiles": "#FEBAFF",
           "Actividades recreativas": "#E3A2FF"}

def leer_json(archivo):
    with open('actividades.json', encoding='utf-8') as archivo:
        data = json.load(archivo)
        return data
        

def guardar_en_json(nombre_archivo, datos_nuevos):
    with open(nombre_archivo, 'r',encoding='utf-8') as archivo:
        datos_archivo = json.load(archivo)
        datos_archivo.append(datos_nuevos)
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos_archivo, archivo, indent=4)
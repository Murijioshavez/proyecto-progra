"""Compatibilidad histórica: las operaciones de datos viven en activity_store."""
from activity_store import ActivityStore

colores = {
    "Torneos Internos": "#7BBDFF",
    "Deporte y Cultura": "#11FF99",
    "Capítulos estudiantiles": "#E1A4FF",
    "Grupos estudiantiles": "#65FFE2",
    "Bienestar": "#F7E16D",
    "Mentoría": "#8EFFA2",
    "Clubs estudiantiles": "#FEBAFF",
    "Actividades recreativas": "#E3A2FF",
}

def leer_json(archivo="actividades.json"):
    return ActivityStore(archivo).list_all()


def guardar_en_json(nombre_archivo, datos_nuevos):
    return ActivityStore(nombre_archivo).append(datos_nuevos)

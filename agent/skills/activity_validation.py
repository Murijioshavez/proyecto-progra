"""Skill: validación determinista de campos necesarios para el calendario."""
from datetime import datetime

from registro import colores


def validate_activity(activity):
    errors = []
    if activity.get("categoria") not in colores:
        errors.append("categoría desconocida")
    if not activity.get("descripcion"):
        errors.append("el título de la actividad es obligatorio")
    if not activity.get("duracion"):
        errors.append("falta duración")
    try:
        datetime.strptime(activity.get("fecha", ""), "%Y/%m/%d")
    except (TypeError, ValueError):
        errors.append("fecha inválida; use YYYY-MM-DD")
    return errors

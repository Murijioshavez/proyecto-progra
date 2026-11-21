"""Skill: normaliza y completa campos derivados sin inventar datos esenciales."""
from registro import colores


def complete_activity(draft):
    activity = {key: value.strip() if isinstance(value, str) else value for key, value in draft.items()}
    category = activity.get("categoria", "")
    if category not in colores:
        normalized = category.casefold()
        category = next((name for name in colores if name.casefold() == normalized), category)
        if category not in colores:
            category = "Actividades recreativas"
    activity["categoria"] = category
    activity["color"] = colores[category]
    activity["descripcion"] = activity.get("descripcion", "")
    activity["duracion"] = activity.get("duracion") or "Por definir"
    activity["comentario"] = activity.get("comentario") or (
        f"Actividad de la categoría {category}: {activity['descripcion']}."
        if activity["descripcion"] else "Descripción generada automáticamente pendiente de título."
    )
    activity["fecha"] = (activity.get("fecha") or "").replace("-", "/")
    return activity

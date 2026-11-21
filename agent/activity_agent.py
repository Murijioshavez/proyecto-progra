"""Orquestador de skills: itera una ficha hasta que las reglas la aceptan."""
from datetime import date

from agent.agent_config import AGENT_NAME, AGENT_ROLE, DEFAULT_MAX_ITERATIONS, DEFAULT_DURATION
from agent.skills.activity_completion import complete_activity
from agent.skills.activity_validation import validate_activity


class ActivityAgent:
    name = AGENT_NAME
    role = AGENT_ROLE

    def __init__(self, max_iterations=DEFAULT_MAX_ITERATIONS):
        if max_iterations < 1:
            raise ValueError("max_iterations debe ser al menos 1")
        self.max_iterations = max_iterations

    def prepare(self, draft):
        """Completa campos omitidos por reglas transparentes y valida por iteración."""
        activity = dict(draft)
        if not activity.get("fecha"):
            activity["fecha"] = date.today().isoformat()
        if not activity.get("duracion"):
            activity["duracion"] = DEFAULT_DURATION
        errors = []
        for _ in range(self.max_iterations):
            previous = activity.copy()
            activity = complete_activity(activity)
            errors = validate_activity(activity)
            if not errors:
                return activity
            # Una nueva vuelta solo aporta valor cuando una skill transformó la ficha.
            # Así el agente itera hasta converger en vez de repetir a ciegas.
            if activity == previous:
                break
        raise ValueError("No se pudo preparar la actividad: " + "; ".join(errors))


__all__ = ["ActivityAgent"]

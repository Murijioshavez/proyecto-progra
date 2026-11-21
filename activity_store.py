"""Persistencia JSON aislada de Flask y de las reglas del agente."""
import json
from pathlib import Path
from threading import RLock


class ActivityStore:
    def __init__(self, path):
        self.path = Path(path)
        self._lock = RLock()

    def list_all(self):
        with self._lock:
            if not self.path.exists() or not self.path.stat().st_size:
                return []
            with self.path.open(encoding="utf-8") as stream:
                data = json.load(stream)
            if not isinstance(data, list):
                raise ValueError("El archivo de actividades debe contener una lista JSON")
            return data

    def append(self, activity):
        with self._lock:
            activities = self.list_all()
            activities.append(activity)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            temporary = self.path.with_suffix(self.path.suffix + ".tmp")
            with temporary.open("w", encoding="utf-8") as stream:
                json.dump(activities, stream, ensure_ascii=False, indent=2)
            temporary.replace(self.path)
            return activity

"""Aplicación web: las rutas coordinan presentación, agente y persistencia."""
from datetime import date
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

from activity_store import ActivityStore
from agent.activity_agent import ActivityAgent
from registro import colores

BASE_DIR = Path(__file__).resolve().parent
store = ActivityStore(BASE_DIR / "actividades.json")
agent = ActivityAgent(max_iterations=3)
app = Flask(__name__)


"""
ANTES — implementación original acoplada (conservada como referencia):

@app.route("/publicar", methods=["GET", "POST"])
def publicar():
    if request.method == "POST":
        categoria = request.form["categoria"]
        descripcion = request.form["descripcion"]
        duracion = request.form["duracion"]
        comentario = request.form["comentario"]
        fecha = request.form["fecha"]
        color = colores[categoria]
        guardar_en_json("actividades.json", {
            "categoria": categoria,
            "descripcion": descripcion,
            "duracion": duracion,
            "comentario": comentario,
            "fecha": fecha.replace("-", "/"),
            "color": color,
        })
        return redirect("/actividades")
    return render_template("actividades.html")

Problemas: la ruta aplicaba las reglas, transformaba datos y persistía directamente;
no completaba valores opcionales ni gestionaba errores de validación/archivo.

DESPUÉS — el flujo operativo está implementado a continuación:
1. `agent.prepare(...)` aplica skills iterativas de completado y validación.
2. `store.append(...)` persiste el resultado con reemplazo atómico.
3. Cada responsabilidad vive en su módulo (`agent/skills/`, `activity_store.py`).
"""


@app.route("/")
def home():
    return render_template("index.html", colores=colores)


@app.route("/nueva")
def nueva():
    return render_template("nueva.html", today=date.today().isoformat(), colores=colores)


@app.route("/actividades")
def actividades():
    try:
        return render_template("actividades.html", actividades=store.list_all())
    except (OSError, ValueError) as error:
        app.logger.exception("No se pudieron cargar las actividades")
        return render_template("error.html", mensaje=str(error)), 500


@app.route("/publicar", methods=["GET", "POST"])
def publicar():
    if request.method == "GET":
        return redirect(url_for("nueva"))
    try:
        activity = agent.prepare(request.form.to_dict())
    except ValueError as error:
        return render_template("error.html", mensaje=str(error)), 400
    try:
        store.append(activity)
    except (OSError, ValueError) as error:
        app.logger.exception("No se pudo guardar la actividad")
        return render_template("error.html", mensaje="No se pudo guardar la actividad."), 500
    return redirect(url_for("actividades"))


if __name__ == "__main__":
    app.run(debug=False)

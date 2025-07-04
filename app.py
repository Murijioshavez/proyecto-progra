import os
from flask import Flask, render_template, request, redirect
from registro import leer_json, guardar_en_json, colores
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d ")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", colores = colores)
@app.route('/nueva')
def nueva():
    return render_template("nueva.html", today= formatted_date, colores = colores)

@app.route('/actividades')
def actividades():
    try:
        actividades = leer_json('actividades.json')
        return render_template("actividades.html", actividades=actividades)
    except Exception as e:
        print(f"Error al cargar actividades: {e}")
        return "Hubo un error cargando las actividades", 500

@app.route("/publicar", methods=["GET", "POST"])
def publicar():
    if request.method == "POST":
        categoria = request.form["categoria"]
        print(categoria)
        descripcion = request.form["descripcion"]
        duracion = request.form["duracion"]
        comentario = request.form["comentario"]
        fecha = request.form["fecha"]
        color = colores[categoria]
        

        guardar_en_json('actividades.json',{'categoria': categoria,'descripcion': descripcion,'duracion': duracion,'comentario': comentario, 'fecha': fecha.replace('-', '/'), 'color': color} )

        return redirect("/actividades")  

    return render_template("actividades.html")  
if __name__ == "__main__":
    app.run(debug=True)
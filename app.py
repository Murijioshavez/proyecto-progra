from flask import Flask, render_template, request, redirect
from registro import leer_json, guardar_en_json, colores, cocurriculares
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d ")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", colores = colores)
@app.route('/nueva')
def nueva():
    return render_template("nueva.html", today= formatted_date, cocurriculares = cocurriculares)

@app.route('/actividades')
def actividades():
     actividades = leer_json('/actividades.json')
     return render_template("actividades.html", actividades=actividades)

@app.route("/publicar", methods=["GET", "POST"])
def publicar():
    if request.method == "POST":
        categoria = request.form["categoria"]
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

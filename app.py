from flask import Flask, render_template, request, redirect
from registro_csv import leer_csv, guardar_en_csv
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d ")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route('/nueva')
def nueva():
    return render_template("nueva.html", today= formatted_date)

@app.route('/actividades')
def actividades():
    actividades = leer_csv('/actividades.csv')
    return render_template("actividades.html", actividades=actividades[::-1])

@app.route("/publicar", methods=["GET", "POST"])
def publicar():
    if request.method == "POST":
        categoria = request.form["categoria"]
        descripcion = request.form["descripcion"]
        duracion = request.form["duracion"]
        comentario = request.form["comentario"]
        fecha = request.form["fecha"]
        

        guardar_en_csv('actividades.csv',{'categoria': categoria,'descripcion': descripcion,'duracion': duracion,'comentario': comentario, 'fecha': fecha}, ['categoria','descripcion','duracion','comentario', 'fecha'] )

        return redirect("/actividades")  

    return render_template("actividades.html")  
if __name__ == "__main__":
    app.run(debug=True)

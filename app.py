from flask import Flask, render_template, request, redirect
from registro_csv import leer_csv, guardar_en_csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route('/nueva')
def nueva():
    return render_template("nueva.html")

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

        guardar_en_csv('actividades.csv',{'categoria': categoria,'descripcion': descripcion,'duracion': duracion,'comentario': comentario}, ['categoria','descripcion','duracion','comentario'] )

        return redirect("/actividades")  

    return render_template("actividades.html")  
if __name__ == "__main__":
    app.run(debug=True)

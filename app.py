from flask import Flask, render_template, request
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
    return render_template("actividades.html", actividades=actividades)


if __name__ == "__main__":
    app.run(debug=True)

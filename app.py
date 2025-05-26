from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", nombre= 'Mau')
@app.route('/nueva')
def nueva():
    return render_template("nueva.html")

@app.route('/actividades')
def actividades():
    return render_template("actividades.html")

if __name__ == "__main__":
    app.run(debug=True)

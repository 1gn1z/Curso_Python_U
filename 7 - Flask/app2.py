from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
@app.route("/<nombre>")

def hola(nombre="Invitado"):
    return f"Hola {nombre}"


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")

def suma(num1=0 ,num2=0):
    return render_template("suma.html")                           

if __name__ == "__main__":
    app.run(debug=True)
    
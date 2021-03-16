from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hola(nombre="Invitado", edad="0"):
    nombre = request.args.get('nombre', nombre)
    edad = request.args.get('edad', edad)
    return f"Hola {nombre} tu edad es {edad}"


@app.route("/images")
def hello_images():
    return "Hello Images"

if __name__ == "__main__":
    app.run(debug=True)

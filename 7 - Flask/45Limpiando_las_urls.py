from flask import Flask
#from flask import request      # <<<--- Ya NO requerimos este import

app = Flask(__name__)

"""@app.route("/")
def hola(nombre="Invitado", edad="0"):
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad', edad)
    return f"Hola {nombre} tu edad es {edad}"
"""

@app.route("/suma/<int:num1>/<int:num2>")           # <<<--- Funcion que suma 2 numeros dentro de la misma Route.
def suma(num1=0 ,num2=0):
    return f"{num1} + {num2} = {num1 + num2}"


if __name__ == "__main__":
    app.run(debug=True)


# Vamos a implementar los parametros de la ruta tambien en nuestra funcion "hola"


# Podemos tener MAS DE UNA RUTA para una VISTA (VIEW) o FUNCION
# Lo unico que tenemos que hacer es AGREGAR OTRA RUTA, y poner la otra ruta que queremos que llame a esta funcion:


# Por ejemplo queremos que el usuario ponga un nombre:


@app.route("/")
@app.route("/<nombre>")                     # <<<--- Requerimos que el usuario ponga un nombre
def hola(nombre="Invitado", edad="0"):
    return f"Hola {nombre} tu edad es {edad}"


# PODEMOS TENER MUCHAS RUTAS PARA UNA SOLA VISTA O FUNCION :D


# En el caso de la funcion o vista para sumar, si ingresamos en el navegador un numero decimal MANDARA UN ERROR.
# Ya que nosotros pusimos que esta esperando un ENTERO:



@app.route("/suma/<int:num1>/<int:num2>")           # <<<--- Funcion que espera un ENTERO!!!
def suma(num1=0 ,num2=0):
    return f"{num1} + {num2} = {num1 + num2}"


# Asi que ya sabemos que las vistas o funciones pueden tener mas de una ruta, asi que agreguemos otra ruta por si el usuario
# agrega algun numero FLOAT:


@app.route("/suma/<int:num1>/<int:num2>")       
@app.route("/suma/<float:num2>/<float:num2>")   
def suma(num1=0 ,num2=0):
    return f"{num1} + {num2} = {num1 + num2}"


# El problema es que si ahora ingresamos un FLOAT y luego un INT NOS DARA ERROR, tenemos que hacer otras vistas o funciones que
# acepten que el primer numero como int y el segundo como float y viceversa:


@app.route("/suma/<int:num1>/<int:num2>")       
@app.route("/suma/<float:num2>/<float:num2>")   
@app.route("/suma/<int:num1>/<float:num2>")         # <<<---  Suma un numero entero y un float      
@app.route("/suma/<float:num2>/<int:num2>")         # <<<---  Suma un numero float y un entero

def suma(num1=0 ,num2=0):
    return f"{num1} + {num2} = {num1 + num2}"

# De este modo manejamos todos los tipos de datos posibles para hacer una suma (float e int), y todas sus variaciones :D




#   #   #   Codigo completo:


from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<nombre>")

def hola(nombre="Invitado", edad=0):
    return f"Hola {nombre}"


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")


def suma(num1=0 ,num2=0):
    return """
    <doctype html>
    <html>
        <head>
            <title>Suma</title>
        </head>
        <body>
            <h1>{num1} + {num2} = {num1 + num2}</h1>        
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)

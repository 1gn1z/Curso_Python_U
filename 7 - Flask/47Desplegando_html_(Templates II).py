# Ya tenemos nuestro template de "suma", pero ahora necesitamos otro para nuestra funcion "hola"

# RETO!!! crear por nosotros mismos el template, que tendra una variable, "nombre", y ya xd

# RETO CUMPLIDO!!! :3


#   #   #       Codigo de python con flask


@app.route("/")
@app.route("/<nombre>")
def hola(nombre="Invitado"):
    return render_template("index.html", nombre = nombre)   # <<<--- usamos solo una variable no es necesario desempaquetar un dict


#    context = {'nombre':nombre}                          El proge lo hizo asi, no se xq pero como 
#    return render_template("index.html", **context)      yo lo hice tambien funciono muy bien


#   #   #       Codigo html


<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola</title>
</head>
<body>
    <h1>Hola {{nombre}}</h1>
</body>
</html>



# index.html es la pagina de inicio de cualquier pagina o sitio o app web.

# En programacion hay un viejo dicho "Dont repeat yourself".

# Si estamos repitiendo codigo seguro hay una mejor manera de hacerlo, como vemos nuestros templates de html SON CASI IDENTICOS.



#   #   #   Codigo completo python:


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<nombre>")
def hola(nombre="Invitado"):
    return render_template("index.html", nombre = nombre)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")

def suma(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("suma.html", **nums)                           


if __name__ == "__main__":
    app.run(debug=True)



#   #   #   Codigo HTML (Suma):

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suma</title>
</head>
<body>
    <h1>{{num1}} + {{num2}} = {{num1+num2}}</h1>    <!--  Dobles llaves para indicar variables  -->
</body>
</html>



#   #   #   Codigo HTML (index):


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
</head>
<body>
    <h1>Hola {{nombre}}</h1>
</body>
</html>
   
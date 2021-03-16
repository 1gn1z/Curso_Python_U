# Hasta este momento hemos visto como desplegar TEXTO PLANO en nuestra app.

# Pero asi NO funcionan las apps o paginas web en genear, las paginas tienen HTML, CSS y JAVASCRIPT


# Vamos a usar FLASK para desplegar HTML.


# Hay 3 maneras de desplegar html con flask:



#   #   #       Primera forma:      (LA MAS LARGA!!!!!!!!!!!!!!!!!!)



# En nuestra Funcion o vista (view) de la suma, dentro de esta ponemos RETURN y TRES COMILLAS DOBLES:
# Las triples comillas nos ayudan a poner HTML por que respetan los espacios, saltos de linea, etc.


# Dentro del Return, desplegamos las etiquetas basicas de html (doctype, html, head, title y body)


def suma(num1=0 ,num2=0):
#    return f"""                            <<<--- Para usar el metodo ACTUAL del formateo de cadenas lo indicamos aqui, en el return

    return f"""                            
    <!doctype html>
    <html>
        <head>
            <title>Suma</title>
        </head>
        <body>
        <h1>{num1} + {num2} = {num1+num2}</h1>        
        </body>
    </html>
    """
    
#    return f"{num1} + {num2} = {num1 + num2}"      <<<--- Linea retornada dentro del body



# Dentro de las triples comillas ponemos nuestro html.

# Dentro de BODY pondremos el codigo que retornaba originalmente nuestra app:

# Finalmente ponemos el format (metodo antiguo) justo despues de las comillas y eliminamos el return original


# Ahora si, si vemos el codigo fuente de nuestra app, veremos exactamente esto, el html escrito por nosotros

# Si vemos el codigo fuente, respeta los espacios que hay antes de las etiquetas, vamos a eliminarlos y quedara asi:


def suma(num1=0 ,num2=0):

    return f"""                            
<!doctype html>
<html>
    <head>
        <title>Suma</title>
    </head>
    <body>
        <h1>{num1} + {num2} = {num1+num2}</h1>        
    </body>
</html>
    """
    
    
# Esta forma NO la vamos a implementar, debido a que si tendriamos que hacer esto POR CADA PAGINA, PARA CADA UNO DE NUESTROS VIEWS
# NO es muy util PONER TODO EL HTML DENTRO DE LAS FUNCIONES.





#   #   #   CODIGO COMPLETO:


from flask import Flask

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
    return f"""                            
<!doctype html>
<html>
    <head>
        <title>Suma</title>
    </head>
    <body>
        <h1>{num1} + {num2} = {num1+num2}</h1>        
    </body>
</html>
    """


if __name__ == "__main__":
    app.run(debug=True)    
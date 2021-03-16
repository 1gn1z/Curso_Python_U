#   #   #       Segunda forma:      (MENOS LARGA!!!!!!!!!!!!!!!!!!)


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
    
    
# Hacerlo asi es INCONVENIENTE, por que esta cabron hacer esto por cada view o funcion que tengamos.

# Vamos a ver como usar TEMPLATES en Flask, que es un documento HTML


# Vamos a crear una carpeta nueva. IMPORTANTE!!! LA CARPETA DEBE LLAMARSE "templates" (sin comillas).


# Se debe llamar "templates", por que esta es una UBICACION ESPECIAL, de la cual Flask busca nuestras templates de html
# para poder desplegarlas en nuestras views (funciones). Por eso es OBLIGATORIO que se llame asi, templates.


# Esta carpeta va en el DIRECTORIO DONDE TENGAMOS LA APLICACION    


# Ahora, dentro de la carpeta vamos a crear un nuevo archivo, este sera el CONTENEDOR DE HTML, osea sera un archivo HTML


# Vamos a ponerle "suma.html", por que eso es precisamente lo que hace esa pagina.



# Y en nuestro archivo html, pondremos lo que teniamos en el return de nustro view de suma:


<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suma</title>
</head>
<body>
    <h1>{num1} + {num2} = {num1+num2}</h1>
</body>
</html>


# Y ahora, para desplegar este documento HTML a nuestro view, lo primero que tenemos que hacer es UN NUEVO IMPORT:

from flask import render_template


# Ya importado nuestro import de render_template, vamos a BORRAR TODOO el html de nuestro view de suma:


def suma(num1=0 ,num2=0):
    return 


# Y en el return vamos a poner:

                           

def suma(num1=0 ,num2=0):
    return render_template("suma.html") # <<<--- Y como parametro vamos a poner EL NOMBRE DEL HTML que queremos desplegar.(ENTRE COMILLAS!)



#   #   #   #       NOTA IMPORTANTE!!!

# El archivo .py esta en x carpeta, Y DENTRO DE ESTA CARPETA DEBE ESTAR LA CARPETA TEMPLATES, Y DENTRO DE TEMPLATES LOS HTMLS


# El problema ahora es que el html nos despliega las llaves tal cual, por que eso es lo que indicamos en el h1:

    <h1>{num1} + {num2} = {num1+num2}</h1>

{num1} + {num2} = {num1+num2}   # <<<--- Asi tal cual lo despliega el navegador.


# Lo podiamos hacer con "F" (format), xq esto es parte de python, PERO EN LAS TEMPLATES NO ES POSIBLE :/

# Para corregirlo vamos a nuestro HTML.

# JINJA2, que es nuestro template en jane, y usa Flask para renderear nuestro html y css cuando usamos RENDER TEMPLATE


# Flask utiliza un motor llamado "Jinja2", que permite poner dentro de las llaves OTRAS LLAVES, y dentro de esas llaves 
# ponemos los nombres de las variables:


    <h1>{{num1}} + {{num2}} = {{num1+num2}}</h1>    # <<<--- DOBLES LLAVES!!!


# Pero ahora nos arroja un error, "num1 is not definied".

# Seguimos son decirle que hara el num1, NO se lo estamos pasando a nuestro TEMPLATE.

# Para corregir esto, vamos a poner COMA, y vamos a definir las variables:


return render_template("suma.html", num1 = num1, num2 = num2)

# num1, (que es la variable que le pasamos al html), es igual a num1, que es lo que obtuvimos del usuario en nuestra ruta


# Ahora si :D, la app despliega todo el html correctamente







#   #   #   METODO 3, DESEMPAQUETAMIENTO DE DICCIONARIO:


# Para no poner todas las variables junto al html, podemos hacer un desempaquetamiento de diccionario:

# Guardamos el diccionario en una variable, poniendo llave y valor (que son las mismas, num1:num1 y num2:num2)


nums = {'num1':num1, 'num2':num2}               # <<<--- LLAVES CON COMILLAS!!!


# Y en lugar de ESCRIBIR TODAS LAS VARIABLES EN EL TEMPLATE, SIMPLEMENTE DESEMPAQUETAMOS EL DICCIONARIO:


return render_template("suma.html", **nums)     # <<<--- DESEMPAQUETADO INDICADO CON DOBLE ASTERISCO!!!



#   #   #       Codigo  Completo:


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
    nums = {'num1':num1, 'num2':num2}
    return render_template("suma.html", **nums)                           
#   return render_template("suma.html", num1 = num1, num2 = num2)   <<<--- Metodo 2 (un poco mas largo)


if __name__ == "__main__":
    app.run(debug=True)
    
    
    

return render_template("suma.html", num1 = num1, num2 = num2)   # VARIABLES SIN COMILLAS CUANDO ES SIN DESEMPAQUETAMIENTO DE DICT
nums = {'num1':num1, 'num2':num2}               # <<<--- LLAVES CON COMILLAS PARA DESEMPAQUETAMIENTO DE DICCIONARIO
    
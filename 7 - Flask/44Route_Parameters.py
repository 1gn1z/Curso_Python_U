# Las query strings son utiles para recibir info del usuario.
# Pero dependiendo la cantidad de info obtenida puede ser confuso y dificil de entender, ademas se veo feo tener nombre=x apellido=X
# se ve fea la url

# Asi que aprenderemos a obtener las variables directamente desde el ROUTE

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hola(nombre="Invitado", edad="0"):
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad', edad)
    return f"Hola {nombre} tu edad es {edad}"

"""@app.route("/images")        
def hello_images():
    return "Hello Images""""        # <<<--- Ya no necesitamos esta route

if __name__ == "__main__":
    app.run(debug=True)
    
    
# Lo que queremos es una pagina que nos ayude a sumar 2 numeros que nos va a dar el usuario.

# vamos a hacer una nueva FUNCION, que acepta 2 parametros, que son los numeros a sumar:
# Y retorna con strings formateadas la suma de los 2 numeros:


def suma(num1, num2):
return f"{} + {} = {}"    


# Y lo vamos a obtener con una VIEW, llamada "suma":



@app.route("/suma")
def suma(num1=0, num2=0):               # <<<--- A ambos numeros les vamos a designar valor por default de 0

num1 = request.args.get('num1', num1)   # <<<--- Hacemos un request comun, si el usuario escribe el numero la variable 'num1' toma
                                        # ese valor, si no, se queda el valor por defecto que especificamos(num1 sin comillas), osea 0
                                        
num2 = request.args.get('num2', num2)                                 
return f"{num1} + {num2} = {num1 + num2}"   # <<<--- El formateo es para CADENAS, debemos convertir los datos de la suma a INTs.


# Ahora iremos anuestra aplicacion, osea en el navegador, pero escribiendo "/suma", seguido del SIGNO DE INTERROGACION
# Y especificamos los valores del num1 y del num2 (No olvidar signo AMPERSAND para separar las variables una de otra):

# Accedemos desde el navegador asi:


http://127.0.0.1:5000/suma?num1=2&num2=2


# Pero el resultado es el siguiente:

2 + 2 = 22

# Recordemos que el formateo que hicimos es para CADENAS, asi que cuando usamos el operador + en cadenas SE CONCATENAN.


# Vamos a convertir los datos de la suma a int para que se sumen los numeros y no se concatenen las cadenas, quedaria asi:


return f"{num1} + {num2} = {int(num1) + int(num2)}"


# Haciendo esto, ya nos devuelve la suma con el resultado correcto :D




#   #    #      Ahora, para NO usar las query strings, vamos a poner los PARAMETROS DIRECTAMENTE EN LA RUTA


# En nuestro ROUTE, agregamos UN DIAGONAL ADICIONAL, y los parametros los especificamos ENTRE LLAVES:


@app.route("/suma/<num1>/<num2>")   # Los parametros van entre simbolos mayor que menor que. Separamos los parametros con otro diagonal

# Haciendo esto podemos eliminar las REQUEST del codigo:



@app.route("/suma/<num1>/<num2>")               # <<<--- Especificando los parametros en la ruta
def suma(num1=0 ,num2=0):

#    num1 = request.args.get('num1', num1)      # <<<--- Ya podemos eliminar estas lineas, osea los Requests
#    num2 = request.args.get('num2', num2)
    
    return f"{num1} + {num2} = {int(num1) + int(num2)}"
    
    
    
# Ahora, si actualizamos la aplicacion en el navegador NOS DARA ERROR.
# Ya que NO debemos poner asi las variables.

# Simplemente pondremos los valores de los parametros SEGUIDOS, SEPARADOS POR DIAGONALES:



@app.route("    /suma   /<num1>   /<num2>") 
127.0.0.1:5000  /suma   /2        /3


# Como vemos, los parametros se separan por el slash, y la variable <num1> se reemplaza en la url por el numero que queramos,
# igualmente el <num2> se especifica con el numero deseado

# NO OLVIDAR LOS SLASHES O DIAGONALES!!!


http://127.0.0.1:5000/suma/2/3      # <<<--- Numeros especificados en la url

2 + 3 = 5                           # <<<--- Resultado que despliega la pagina



# Finalmente podemos hacer otra mejora, podemos ESPECIFICAR LOS PARAMETROS CON EL TIPO DE DATO QUE QUERAMOS.

# En otras palabras, podemos indicar que los parametros de la ruta son INT y no STR:

# Para hacer esto, escribimos el tipo de dato, SEGUIDO DE 2 PUNTOS Y SEGUIDO:


@app.route("/suma/<int:num1>/<int:num2>")           # <<<--- ESPECIFICACION DENTRO DE LOS SIGNOS MAYOR QUE MENOR QUE!!!


# Y ya podemos eliminar la especificacin de INT de el formateo del Return de la funcion:


    return f"{num1} + {num2} = {num1 + num2}"







#   #   #   Codigo completo:



from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hola(nombre="Invitado", edad="0"):
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad', edad)
    return f"Hola {nombre} tu edad es {edad}"


#   #   # Funcion para sumar 2 numeros (via view)

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1=0 ,num2=0):
    return f"{num1} + {num2} = {num1 + num2}"


if __name__ == "__main__":
    app.run(debug=True)
    
# A veces necesitamos datos que el usuario nos va a pasar.

# Para obtener esta informacion, una de las formas mas faciles es usando la QUERY STRING.

# La QUERY STRING es TODO lo que ponemos despues de un signo de interrogacion y encontramos una serie de LLAVES y VALORES.

http://127.0.0.1:5000/?name=pepe    # Por ejemplo.


# Despues podemos poner un AND, PERO! con el simbolo ampersand (&).

http://127.0.0.1:5000/?name=pepe&edad=18&   # Podemos tener infinidad de ands.


# Para que los cambios que hagamos se vean reflejados tenemos que cambiar el codigo, cerrar la aplicacion si estaba corriendo
# y volver a correrla, esto es tardado y tedioso, asi que vamos a ver una manera de ver las actualizaciones mas rapidamente :3


# En nuestra aplicacion, en la parte del APP.RUN VAMOS A ACTIVAR EL MODO DEBUG.

app.run(debug=True)

C:\Users\1gn1z\Documents\CDPpythonU\7 - Flask>app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on                           # <<<--- Debug activado
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 606-508-134                
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 
 
# Gracias a que el Debug esta activado, cuando hagamos un cambio, se detecta el cambio y se reinicia la aplicacion :D


 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 606-508-134
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Detected change in 'C:\\Users\\1gn1z\\Documents\\CDPpythonU\\7 - Flask\\app.py', reloading   # <<<--- Cambio detectado
 * Restarting with stat                                                                         # <<<--- Se reinicia la aplicacion
 * Debugger is active!                                                                          # <<<--- Se reactiva el modo debug
 * Debugger PIN: 606-508-134
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


# Ahora, simplemente REFRESCANDO la pagina, se muestran los cambios hechos, sin necesidad de detener la ejecucion de la app,
# volver a iniciarla y despues volver a entrar o actualizar la pagina :D


# Ahora vamos a hacer que nuestro codigo sea capaz de OBTENER LOS ARGUMENTOS DE LAS QUERY STRINGS

# Lo primero que tenemos que hacer, es hacer un nuevo import de flask, llamado REQUEST:

from flask import request


# Ahora, en lugar de poner "Hello World", queremos escribir "Hola" mas el nombre del usuario "Hola Luis", "Hola Diego", etc.

# PAra esto vamos a poner, dentro de la funcion "hola_mundo()" nombre="", por default dira "Invitado".

@app.route("/")
def hola(nombre="Invitado"):
    return "Hello World!!!"


# Y para pedir al usuario su nombre, lo hacemos con la libreria "REQUEST", via metodo "ARGS" de arguments, y la palabra "GET"
# para obtener algo.

# Y entre los parentesis del GET, vamos a añadir la cadena 'nombre', mas la variable nombre.

@app.route("/")
def hola(nombre="Invitado"):                    # nombre="Invitado". En este caso "Invitado" es el valor por defecto
    nombre = request.args.get('nombre', nombre) # 'nombre' se guarda en la variable. nombre es el valor por defecto
    return "Hello World!!!"


# PRIMERO. Accedimos al request

# SEGUNDO. Obtenemos los ARGUMENTOS (args), que son los que sigues despues del signo de interrogacion en la URL:

# 127.0.0.1:5000/?nombre=diego

# TERCERO. Le dijimos que obtenga el parametro con el nombre. 
# 
# NOMBRE CON COMILLAS 'nombre'. Si el nombre existe simplemente lo asignamos a nuestra variable nombre 

# NOMBRE SIN COMILLAS ,nombre. Si el nombre NO existe, simplemente le asignaremos el valor de los argumentos de la funcion "hola",
# es decir, le asignamos el nombre "Invitado". Nombre sin comillas ES EL VALOR POR DEFAULT


# Finalmente, en el return, en lugar de "Hello World", pondremos "Hola" y concatenando la variable nombre mediante el FORMATO
# de cadenas en python, es decir con las llaves {}


# RETO!!! Que aparte de la query string del nombre, hagamos otra query string que diga la edad.

# Reto logrado <3

@app.route("/")
def hola(nombre="Invitado", edad="0"):          # Le agregamos un segundo argumento, que en este caso es la edad
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad', edad)       # hacemos otro request, que sea la edad
    return f"Hola {nombre} tu edad es {edad}"   # retornamos ademas del nombre, la edad



#   #   #   Codigo completo:



from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hola(nombre="Invitado", edad="0"):
    nombre = request.args.get('nombre',nombre)
    edad = request.args.get('edad', edad)
    return f"Hola {nombre} tu edad es {edad}"

@app.route("/images")
def hello_images():
    return "Hello Images"

if __name__ == "__main__":
    app.run(debug=True)
    
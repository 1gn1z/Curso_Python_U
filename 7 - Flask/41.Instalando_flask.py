# Para instalar flask es tan facil como escribir:

pip install flask

C:\Users\1gn1z>pip install flask
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 224 kB/s
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 213 kB/s
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 2.2 MB/s
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 2.2 MB/s
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp36-cp36m-win32.whl (15 kB)
Installing collected packages: click, MarkupSafe, Jinja2, Werkzeug, itsdangerous, flask
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0


# Y listo nena! :)

# La pagina oficial de flask es:

https://flask.palletsprojects.com/en/1.1.x/


# Ya instalado Flask, vamos a la CONSOLA de windows.

# Vamos a hacer lo primero que se hace al aprender un lenguaje de programacion, un framework, etc, un "Hola mundo"



# Lo primero que tenemos que hacer es un:
#   #   # Todo esto lo tendremos en un archivo limpio aparte, llamado "app.py"

from flask import Flask

# Ahora, lo siguiente que tenemos que hacer, es una VARIABLE, llamada app, es decir, tenemos que decir que nuestra APP
# apunte a flask

app = Flask         # <<<--- Nuestra app apuntando hacia flask.

# Pero ademas de apuntar a Flask, entre parentesis tenemos que poner dunder name dunder:

# Basicamente estamos haciendo que nuestra aplicacion apunte a si misma, usando los NAMESPACES (__name__)

# RECORDEMOS, que si iniciamos la aplicacion directo del CMD, el NAMESPACE (__name__) seria MAIN
# Si la importamos como una libreria, el nombre de la aplicacion seria "app.py"


# Por eso usamos esta linea:

if __name__ == '__main__':

# Para que nuestro archivo funcione al ser ejecutado directamente desde la consola sin tener que importarlo

app = Flask(__name__)



# Despues tenemos qe crear UNA RUTA, esto se hace con la siguiente linea:

@app.route("/")     # <<<--- El slash (/) indica la ruta por defecto, o principal, si no hay nada desplegamos el hola mundo

# Esta linea es como una URL dentro del navegador, cuando no tenga nada, vamos a desplegar un "Hola mundo".

# Para desplegar el hola mundo, lo vamos a haccer con una funcion, que simplemente retorna el texto "Hello World!"

def hello():
    return "Hello World!"


# Finalmente solo vamos a hacer la comprobacion de que el programa se esta corriendo directamente desde el cmd sin ser importado:


if __name__ == "__main__":      # <<<--- Si el namespace es igual a main, osea si ejecutamos la aplicacion directamente
    app.run()                   # <<<--- Vamos a correr la aplicacion, con el metodo RUN (run())


    
# Ahora, ya teniendo nuestra primera aplicacion Flask lista, vamos a ejecutarla directamente desde el cmd:

app.py


# Si lo hicimos bien, nos mostrara un mensaje que dice que la aplicacion esta corriendo:    

# Me salieron mas mensajes que en el curso, que solo salio la linea 116

C:\Users\1gn1z\Documents\CDPpythonU\7 - Flask>app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)    # <<<--- Indica que esta corriendo en la ip 127.0.0.1 en el puerto 5000
 
 
# Ahora ingresando la url en nuestro navedagor, veremos la pagina web creada por flask (y nosotros :3), que mostrara "Hello World!" 
# Ver 1Hello world (1er programa con flask).png


# Tambien podemos escribir (sin comillas) "localhost:5000"

#   #   #   Codigo completo hasta ahora:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    
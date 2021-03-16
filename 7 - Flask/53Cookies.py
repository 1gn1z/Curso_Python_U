# Ya sabemos como tener un formulario, pasarle informacion y que nos retorne una pagina de envio exitosa.


# Mandar correos es algo complicado, ya que necesitamos un servidor especializado para ello :(
    
# Vamos a guardar una cookie que va a contener la informacion que obtuvimos

# Normalmente, despues de mandar la informacion, nos da la pagina de exito, y nos redirecciona al index, eso es lo que haremos.


# Lo primero que haremos sera REDIRECCIONAR.

# En uestro ruta de "submit", haremos una variable llamada RESPONSE, que sera igual a REDIRECT, entre parentesis URL_FOR
# y nuevamente entre parentesis el nombre de la FUNCION de la ruta principal, en este caso llamada "hola"


@app.route("/submit", methods=['POST'])
def submit():
    response = redirect(url_for('hola'))
    return "Succesfully Submit"


# Y podemos mejorar los imports, dejar los 2 en una sola linea:

#from flask import Flask
#from flask import Flask, render_template

from flask import Flask, render_template

# Pero necesitamos tambien el IMPORT de URL_FOR, simplemente añadimos una coma y lo agregamos:


from flask import Flask, render_template, url_for

# Ahora lo unico que tenemos que hacer, es devolver, en lugar del mensaje "Succesfully submit", retornar el RESPONSE:



@app.route("/submit", methods=['POST'])
def submit():
    response = redirect(url_for('hola'))
    return response

# Tambien debemos incluir el IMPORT REDIRECT:

from flask import Flask, render_template, url_for, redirect


# Todo listo, ahora al mandar la informacion via el boton submit, nos redirecciona a la pagina principal, pero esto NO nos sirve
# de mucho.

# Lo que queremos es poner una cookie con la informacion, para esto pondremos RESPONSE.SET_COOKIE


# UNA COOKIE ES UN ARCHIVO PEQUEÑO QUE SE GUARDA EN EL NAVEGADOR, Y CONTIENE INFORMACION DE NOSOTROS.
# ESTA INFORMACION PUEDE SER COMO EN ESTE CASO NUESTRO NOMBRE, PUEDE SER INFORMACION DE INICIO DE SESION, INFORMACION DE LAS PAGINAS
# QUE HEMOS VISITADO, etc.

response.set_cookie()

# Y dentro de los parentesis, ponemos JSON.DUMPS()

# Con SET_COOKIE estamos creando la cookie.     <<<--- set_cookie()


# E INDICAMOS QUE EN ESTA COOKIE queremos poner un archivo de JSON  <<<--- (json.dumps())


# JSON es una forma de diccionario, que tiene una serie de llaves y valores, como nombre=Diego, email=kebor327@gmail.com, etc.


# Como estamos usando JSON debemos importarlo:

import json


# DUMSP significa DUMPSTRING, es decir, queremos una cadena de texto que sera de tipo json.


# Esta cadena sera en BASE A UN DICCIONARIO:

response.set_cookie(json.dumps(dict()))


# Y este diccionario se generara a su vez a partir de nustra REQUEST.

response.set_cookie(json.dumps(dict(request.form.items())))


# Y como estamos usando REQUEST, vamos a importarlo en la linea de nuestras importaciones de FLASK:


from flask import Flask, render_template, url_for, redirect, request


# Nuestro codigo funciona, podemos ver la cookie en:

# Chrome -> Mas herramientas -> Herramientas para el desarrolador   (O usamos Ctrl + Mayús + I)
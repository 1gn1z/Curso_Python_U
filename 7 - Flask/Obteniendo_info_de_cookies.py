# Ya tenemos nuestro sitio con las cookies guardadas PERO TENEMOS UN ERROR!

# En nuestro caso, la cookie tiene TODOS LOS DATOS EN EL NOMBRE, EL VALOR DE LA COOKIE ESTA VACIO!!!:


# Las cookies pueden tener UN NOMBRE y UN VALOR, por que los sitios web PUEDEN PONER MAS DE UNA.

# Esto lo hacen xq tal vez una cookie guarda el inicio de sesion, otra guarda la info del carrito de compras,
# otra lo que visitamos la vez pasada para darnos sugerencias, etc.

# Es muy comun que haya mas de una cookie, asi que se les asigna un valor para identificarlas, ese fue nuestro error.


# Lo primero que haremos sera PONER UN NOMBRE, por ejemplo DATA:

response.set_cookie('data', json.dumps(dict(request.form.items())))


# Despues del espacio de DATA, que es el nombre de nuestra cookie, el VALOR que le damos, que es informacion en json

# Vamos a agregar una cookie extra, simplemente guardara una cadena de texto:


response.set_cookie('sesion', 'información de sesión')


# Ya podemos quitar esta cookie, que solo fue de ejemplo Ok ;)


# Para obtener la info de nuestra cookie es nuestra view de "hola".

# Vamos a suponer que ya no queremos obtener el nombre, asi que borramos esa Route:




@app.route("/")
#@app.route("/<nombre>")
def hola(nombre="Invitado"):
    return render_template("index.html", nombre = nombre)


# Ahora, si intentamos ingresar a por ejemplo: 127.0.0.1/kevor, o cualquier otro nombre, nos mandara el siguiente error:


Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.


# Esto pasa xq YA NO estamos permitiendo que nos pasen el nombre en la url, tenemos que obtenerlo de nuestra cookie.


# Para esto, vamos a crear una variable llamada, por ejemplo, 'data', que sera igual a: JSON.LOADS(REQUEST.COOKIES.GET(NOMBRE DE LA COOKIE))

data = json.loads(request.cookies.get('data'))


# Lo primero que hacemos es un REQUEST, luego ponemos cookies, por que pueden ser varias, GET para obtenerla, y el nombre (entre
# comillas) de la cookie.


# Finalmente asinamos una nueva variable llamada, 'nombre', que sera igual a DATA.GET(NOMBRE)

name = data.get(name) 


# Ahora tenemos que cambiar la funcion, y emplear un desempaquetamiento de diccionario:

@app.route("/")
#@app.route("/<nombre>")
def hola(nombre="Invitado"):
    data = json.loads(request.cookies.get('data'))
    name = data.get('name')
    context = {'nombre':nombre}
    return render_template("index.html", **context)



# Lo que paso es que en data.get('name'), asignamos el nombre en el CONTEXT, y de ahi lo toma al introducirlo en nuestra FORM


# Si ahora vamos a nuestra pagina principal, nos sigue diciendo "Hola Kevor", esto pasa por que la cookie ahora mismo tiene info,
# Tiene de informacion 

#   name:Kevor
#   email:kebor327@gmail.com    
#   comment:olakmira


# Ahora, si desde chrome limpiamos las cookies y recargamos la pagina, nos dara un error:

TypeError
TypeError: the JSON object must be str, bytes or bytearray, not 'NoneType'


# Dice que el JSON debe ser STRING y tenemos un NONETYPE.
# Lo que paso es que estamos tratando de recargar un JSON, pero NO TENEMOS ninguna cookie con el nombre DATA

# Para corregir esto simplemente tenemos que poner un TRY, en la variable DATA:

try:
    data = json.loads(request.cookies.get('data'))
except TypeError:
    data = {}               # <<<--- Si nuestra cookie no tiene nada, al arrojar un TypeError, le asignamos un json vacio
else:
    name = data.get('name')
context = {'name':name}
return render_template("index.html", **context)    
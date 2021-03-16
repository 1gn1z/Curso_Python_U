# A los scripts de python en los que hacemos una aplicacion de FLASK, se les llama APPS.

# Las aplicaciones flask se encargan de RECIBIR LAS PETICIONES WEB que vienen hacia nuestras apps.

# Y se encargan de REDIRIGIRLAS a la FUNCION (en FLASK LLAMADAS "VISTAS" o "VIEWS") y esto lo hace atraves de las ROUTES o RUTAS.

# Nuestra aplicacion de Flask se encarga de obtener todas las peticiones que vienen hacia nuestro codigo y las redirige
# hacia nuestras funciones.

# Nuestra funcion "hello", podemos tener una funcion que despliegue una imagen o un video, otra que despliegue un documento etc, etc.


# Flask sabe hacia que funcion redirigir la peticion A TRAVES DE LA RUTA.

# El slash (/), es la ruta PRINCIPAL de nuestro codigo, asi que al ingresar a la pagina lo primero que muestra es la direccion:

127.0.0.1:5000/ 

# Como vemos, al ingresar el link al navegador lo primero a lo que accedemos es al slash, la ruta principal.

app.route("/")
def hello():
    return "Hello World!"

# Cuando Flask encuentra esa ruta, despliega en la app web la(s) funcion(es) que tenga esa ruta, en nuestro caso solo un "Hello World!"


# Pero podemos hacer muchas otras cosas, por ejemplo, podiamos haber desplegado una respuesta en JSON, una respuesta en XML para 
# un servicio web, un HTML y CSS para una pagina web, etc etc.


# Vamos a verlo con codigo, ahora queremos hacer una funcion llamada "hello_images", que sera desplegada cuando el usuario visite:

127.0.0.1:5000/images

# Vamos a hacer la funcion, el nombre de la funcion puede ser CUALQUIER NOMBRE, flask no se fija en esto, a flask le interesan mas
# las ROUTES de nuestras apps.


# La funcion simplemente queda asi:

def hello_images():
    return "Hello Images!"


# Ahora, antes (SIEMPRE ANTES!) de la funcion, debemos especificar la RUTA. SIEMPRE EMPIEZAN CON @ LAS RUTAS!!!


@app.route(/images)
def hello_images():
    return "Hello Images"

# Ahora, cada que un usuario haga una peticion a 127.0.0.1:5000/images, Flask buscara via app.route, y cuando la encuentre
# desplegara el contenido de la funcion que pertenezca a esa ruta.



# Ahora vamos a TERMINAR la ejecucion de la aplicacion, xq NO se actualiza sola, y volvemos a ejecutar app.py




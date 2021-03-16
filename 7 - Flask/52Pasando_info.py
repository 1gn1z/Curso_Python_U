# Cuando vamos a nuestro formulario, y le damos click en SUBMIT PASA UN ERROR!!!
# EN MI CASO NO PASA ABSOLUTAMENTE NADA.

# Pero el Error pasa por que NO indicamos a que URL queremos ir cuando le damos click en SUBMIT.


# Para arreglar esto vamos a crear una nueva Route o View:


@app.route("/submit")
def submit():
    return "Succesfully Submit"


# En la ruta, debemos especificar que esta SOLO ES ACCESIBLE A TRAVES DE UN "POST", solamente esta hecha para RECIBIR INFORMACION.
# Por lo tanto debemos indicarle que usara el metodo POST, de esta manera:


@app.route("/submit", methods=['POST'])     # methods= ENTRE CORCHETES 'POST'   METHODS CON S AL FINAL!!!
def submit():
    return "Succesfully Submit"


# Ahora, en nuestro "contacto.html", vamos a usar una nueva funcion, exactamente en nuestra etiqueta FORM:

# Que sera, dentro de dobles llaves {{  }} un URL_FOR() y entre parentesis el nombre de la funcion, en este caso "submit"

<form action="{{ url_for('submit') }}"
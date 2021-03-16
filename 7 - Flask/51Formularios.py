# En nuestra carpeta templates creamos un nuevo archivo html llamado por ejemplo "contacto.html"

# Y en contacto, vamos a heredar de nuestra base, y simplemente reemplazaremos el titulo y el contenido:

{% extends 'base_layout.html' %}

{% block title %}Contacto{% endblock %}     # <<<--- Cambiar titulo.

# En el bloque de contenido vamos a dejar un poco de espacio, de la siguiente manera:

{% block content %}



{% endblock %}

# Para agregar una FORMA usamos la etiqueta de html FORM:

<form></form>

# Y dentro de la etiqueta de apertura de FORM ponemos un ACTION en blanco y un METHOD que admite POST, asi:


<form action="" method="POST"></form>       # POST con MAYUSCULAS

# Ahora dentro del form agregamos unos INPUTS:

# El primero sera TIPO TEXTO, y NAME sera igual a nombre, con el VALUE VACIO:

  <input type="text" name="nombre" value="">


# El segundo sera igual TIPO TEXTO, en NAME sera "email" y VALUE VACIO:

  <input type="text" name="email" value="">


# Ademas de nuestro nombre y email, vamos a agregar un tercer input para un comentario:

  <input type="text" name="comment" value="">    # Generalmente tenemos un "TextArea" con un espacio mayor que este, pero al profe
                                                # le dio weba y solo haremos este normal por que "propositos educativos"


# Finalmente agregamos un input de SUBMIT, que tendra TYPE SUBMIT y VALUE SUBMIT:

<input type="submit" value="Submit">


#       CODIGO COMPLETO:

{% extends 'base_layout.html' %}

{% block title %}Contacto{% endblock %}

{% block content %}

<form action="" method="POST"></form>
    <input type="text" name="nombre" value="">
    <input type="text" name="email" value="">
    <input type="text" name="comment" value="">
    <input type="submit" value="Submit">
</form>
    
{% endblock %}


# Para poder ir a esta pagina necesitamos crear una ROUTE.


@app.route("/contacto")
def contanto():
    return render_template("contacto.html")


# Ya nos aparece nuestro formulario, pero los campos por default estan vacios y NO sabemos que dato ingresar en que campo,
# Para arreglar eso, vamos a agregar, JUSTO ANTES de los INPUTS la etiqueta LABEL:

<laber for="nombre">Nombre: </label><input type="text" name="nombre" value="">


# Quedando asi:

<label for="nombre">Nombre: </label><input type="text" name="nombre" value="">
<label for="nombre">Email: </label><input type="text" name="email" value="">
<label for="nombre">Comentario: </label><input type="text" name="comment" value="">


# Ahora ya sabemos que dato en que campo, pero esta en una linea recta y eso no nos gusta, vamos a añadir un SALTO DE LINEA
# al final de cada etiqueta usando la etiqueta BR (VAMOS A PONER 2 BR)

# Quedando asi:

<label for="nombre">Nombre: </label><input type="text" name="nombre" value=""><br><br>
<label for="nombre">Email: </label><input type="text" name="email" value=""><br><br>
<label for="nombre">Comentario: </label><input type="text" name="comment" value=""><br><br>



# Hay una gran cantidad de html repetido, es casi identico solo que varia el titulo y el h1 que esta dentro del body.

# Vamos a usar lo que se conoce como "Template Inheritance", "HERENCIA DE TEMPLATES"

# Esto no ayuda a tener un "HTML base", o una especie de "Plantilla" html del que vamos a sacar gran cantidad de html
# y solo vamos a reemplazar las cosas que queramos/necesitemos.

# Vamos a crear un html base, con el nombre que queramos pero en esta ocacion le llamaremos "base_layout".


# En nuestra base pondremos TODOO el html COMUN en ambos:



<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>            # Ambos son identicos, solo varia el titulo
</head>
<body>
    <h1>Hola {{nombre}}</h1>        # Y el h1 que esta dentro del body
</body>
</html>



# En nuestra base, en lugar de cuaquiera de los 2 titulos, USAMOS LLAVES {} y dentro de las llaves pondremos 2 SIGNOS DE PORCENTAJE
# (al inicio y al final):

{% %}

# Y dentro de los signos de porcentaje la palabra BLOCK


# Y finalmente cerramos con otras llaves, otros 2 signos de porcentaje, y la palabra ENDBLOCK, para indicar que termina el bloque:


{% endblock %}


# Asi que las etiquetas "title" de nuestra base html quedarian asi:


    <title>{% block titulo %}{% endblock %}</title>


# Ahora borraremos la otra linea igual pero con distinto contenido, osea, la del h1 y crearemos un nuevo bloque, llamado "content"

# Todo el codigo HTML de la base queda asi:


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>{% block title %}{% endblock %}</title>  # <<<--- Bloque de titulo para el titulo
</head>
<body>
    <h1>{% block content %}{% endblock %}</h1>      # <<<--- Bloque de contenido para nuestro h1
</body>
</html>


# Para usar nuestra base, vamos a nuestro archivo "suma.html", y justo hasra arriba escribimos

# llaves, doble signo de porcentaje, la palabra EXTENDS y el nombre del template que vamos a HEREDAR, que seria nuestra BASE


{% extends 'base_layout.html' %}    # <<<--- extends, mas el nombre del archivo del que vamos a heredar (ENTRE COMILLAS)


# Ahora en nuestro archivo de "suma" podemos ya BORRAR todas las etiquetas "repetidas", es decir
# PODEMOS BORRAR TODOO LO QUE YA TIENE LA BASE, ya que nuestro archivo "suma" HEREDA de la base.


# Solo tenemos que REASIGNAR las etiquetas que queremos modificar, el titulo del archivo suma quedaria asi:


{% block title %}Suma{% endblock %}         # <<<--- Dentro de los bloques de inicio y fin pondremos "Suma", que es el texto

# que queremos desplegar en el titulo de la pagina


# Y finalmente, pondremos lo que queremos desplegar en nuestro h1, es decir, el formateo y operacion de los 2 numeros para
# obtener la suma:


{% block content %}{{ num1 }} + {{ num2 }} = {{ num1+num2 }}{% endblock %}


# El codigo de el archivo "suma.html", ahora se reduce a estas pocas lineas:


{% extends 'base_layout.html' %}

{% block title %}Suma{% endblock %}

{% block content %}{{ num1 }} + {{ num2 }} = {{ num1+num2 }}{% endblock %}


# Ahora hay que hacer lo mismo en nuestro "index.html", quedando asi:


{% extends 'base_layout.html' %}

{% block title %}Index{% endblock %}

{% block content %}Hola {{nombre}}{% endblock %}


# Ahora, al recargar la pagina vemos que todo sigue funcionando bien, igual que antes.

# PERO!!! con la diferencia de que ahora, si vemos el codigo fuente tenemos nuestro html, cosa que antes NO pasaba.



# Podemos dejar el h1 asi:


    <h1>{% block content %}{% endblock %}</h1>


# o podemos ponerlo manualmente en donde lo queramos, en los archivos "suma.html" y "index.html":




{% block content %}<h1>Hola {{nombre}}</h1>{% endblock %}                       # <<<--- index.html


{% block content %}<h1>{{ num1 }} + {{ num2 }} = {{ num1+num2 }}</h1>{% endblock %}      # <<<--- suma.html


# Vamos a dejarlo de la segunda manera, por si NO necesitamos que lo que este dentro de body sea necesariamente un h1


# Para estar MUY seguros que estamos heredando de nuestra base, pondremos en la misma base un h2, con un mensaje indicador:

<h2>Heredado desde 'base_layout.html'</h2>

# Le voy a poner yo h3 para que no quede demasiado largo


<h3>Heredado desde 'base_layout.html'</h3>


# La herencia de Templates tiene gran potencial, debido a que nos ahorra MUCHO codigo, como por ejemplo, en las paginas web

# hay muchas partes que son iguales, por ejemplo en el FOOTER de hasta abajo que contiene el clasico "copyright".

# El HEADER que tiene el logo de la compañia, y el menu de toda la pagina, el titulo etc.



# Lo mejor es que si queremos hacer una modificacion, NO TENEMOS QUE IR A CADA PAGINA, simplemente vamos a la base, cambiamos
# lo que queramos (por ejemplo el logo, o el titulo), y nuestra modificacion SE APLICA A TODAS LAS PAGINAS DE LAS QUE HEREDA :D.


# Que seria del html sin css y javascript

# En Flask, podemos tambien usar una carpeta especial, donde ponemos el CSS y el JS, llamada "static"

# Asi que vamos a crear una nueva carpeta AL NIVEL DE FLASK (NO DENTRO DE TEMPLATES), llamada static

# Dentro de ella pondremos nuestros archivos de css y js, vamos a empezar creando un archivo css llamado "style.css"

# Hacemos un pequeño css:

body{
    background: #228844;
    color: black;
}

# Para referenciarlo en nuestros layout vamos a nuestra base, (si queremos que todos los demas templates lo hereden)
# Y lo hacemos como con cualquier documento html:   (Justo arriba del title)

<link rel="stylesheet" href="/static/style.css"></link>     # <<<--- NO OLVIDAR PONER /static, que es la carpeta donde esta el css


# Por alguna razon, UNA VEZ ASIGNADO EL CSS NO SE PUEDE MODIFICAR!!! TENDRIAMOS QUE CREAR UN CSS NUEVO CON OTRO NOMBRE


# INCLUSO SI LO BORRAMOS Y LO GUARDAMOS DE NUEVO, QUEDA IGUAL COMO LO ASIGNAMOS LA PRIMERA VEZ
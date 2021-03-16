import re

archivo = open("sample.txt",encoding="utf-8")
info = archivo.read()
archivo.close()
print(info)

print(re.search(r"ABCDEFGHIJKLMNOPQRSTUVWXYZ",info))

# Ya vimos como buscar una cadena de caracteres en especifico. Pero si tuvieramos que buscar miles de paginas, todos los nombres
# y todos los numeros telefonicos, y por cada uno tuvieramos que poner el dato.

# Para eso existen las expresiones regulares.
# Las expresiones regulares permiten buscar patrones de texto, numeros y/o simbolos que se ajusten a nuestra descripcion

# Veremos algunas de las clases de caracteres para buscar letras, espacios, numeros, etc etc.

# Vamos a la pagina de regexr y vamos a la seccion de "Character clases": Vemos esto:

\w\d\s	word, digit, whitespace

# Cuando ponemos \w minuscula, quiere decir que estamos buscando WORD CHARACTERS
# Cuando ponemos \d minuscula, quiere decir que estamos buscando DIGITOS
## Cuando ponemos \s minuscula, quiere decir que estamos buscando CARACTER VACIO (ESPACIOS)

"""
                                \w -> Palabras con caracteres
                                \d -> Digitos
                                \s -> Espacios en blanco
"""

# PERO! cuando ponemos \W Mayuscula quiere decir que estamos buscando CUALQUIER COSA QUE NO SEA UNA PALABRA
# Cuando ponemos \D Mayuscula quiere decir que estamos buscando CUALQUIER COSA QUE NO SEAN DIGITOS
# y \S Mayuscula quiere decir que estamos buscando cualquier cosa que NO SEA CARACTER VACIO O ESPACIOS EN BLANCO

"""
                                \W -> Cualquier cosa que NO sean palabras con caracteres
                                \D -> Cualquier cosa que NO sean digitos
                                \S -> Cualquier cosa que NO sean espacios en blanco
"""

# Si al texto de ejemplo en regexr le pasamos el parametro \w, encuentra como coincidencias TODAS las palabras y numeros, incluso 
# el guion bajo, Pero los caracteres NO SON COINDICENCIA. Caracteres como:

# +-.,!@#$%^&*();\\/|<>\"\'

# Si ponemos el cursor en la expresion que estamos evaluando en regexr dice que:

# \w Coindice con CUALQUIER PALABRA DE CARACTERES, INCLUYENDO ALPHANUMERICO Y GUION BAJO

# Al usar esta expresion estamos buscando cualquier cosa que sea una letra, tanto mayuscula como minuscula, o un numero
# Ver captura regexr1.png

# Ahora, si usamos \d buscaremos los digitos. (Ver captura regexr2.png)

# Y si buscamos \s buscamos todos los caracteres vacios incluso 2,3 o mas espacios (espacios en blanco) (Ver captura regexr3.png)

# Ahora veamos que pasa con las mayusculas:

# Con \W

# Como vemos (captura regexr4.png), encuentra cualquier cosa que no sea un numero, letra o guion bajo.

# Si ponemos \D mayuscula encuentra todo lo que NO sea un numero (captura regexr5.png)

# Y con \S mayuscula encuentra cualquier cosa que NO sea un caracter vario, un espacio en blanco (captura regexr6.png)


# Como le hariamos para buscar un número, por ejemplo el que esta comentado aqui abajo


Sample text for testing:
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _w
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567	"""+1-(800)-555-2468"""
foo@demo.net	bar.ba@test.co.uk
www.demo.com	http://foo.co.uk/
http://regexr.com/foo.html?q=bar
https://mediatemple.net

# Podemos buscar, algo que tenga un +, algo que tenga un digito \d.
# Pero en regexr nos da un error por que el signo de + se usa tambien en las expresiones regulares.

# Entonces como le decimos que queremos buscar un signo de mas y no un cuantificador? 

# Como en los comentarios en los lenguajes de programacion, en este caso agregamos una diagonal invertida e ignorara
# La funcion de cuantificador, y nos muestra el + y el digito. (captura regexr7.png)

# Ahora añadimos el parentesis, pero tendremos otro error, en expresiones regulares el parentesis nos sirve para capturar grupos.

# Tambien tenemos que darle caracter escape: (diagonal invertida \)

# Muy bien vamos avanzando, ahora encontro hasta el parentesis de apertura (captura regexr8.png)

# Hasta el momento la expresion va asi:

\+\d-\(

# Ahora queremos 3 digitos, asi que agregaremos 3 diagonales invertidas seguidas de la letra d minuscula: (captura regexr9.png)

\+\d-\(\d\d\d

# Y asi seguimos consultando hasta que nuestra expresion regular sea exacta y nos encuentre unicamente lo que queremos.

# La expresion al final queda asi: (captura regexr10.png)

\+\d-\(\d\d\d\)-\d\d\d-\d\d\d\d

# Ya tenemos una expresion regular que detecta el numero especifico que estamos buscando :D

# Estamos siendo MUY especificos, ya que obligatoriamente estamos buscando que empieze con +, que tenga parentesis
# que tenga 4 digitos, etc.

# Pero depende de nosotros que tan especifimos seremos con nuestras expresiones regulares.

# Ahora, como ponemos esta expresion regular en python?

# En nuestro main, en print(re.match(r"")) Dentro de las comillas colocamos nuestra expresion regular
# Si todo sale bien, debe haber un match para nuestra expresion:

import re

archivo = open("sample.txt",encoding="utf-8")
info = archivo.read()
archivo.close()
print(info)

print(re.search(r"\+\d-\(\d\d\d\)-\d\d\d-\d\d\d\d",info))

# Y en efecto, hubo el match:

<re.Match object; span=(139, 156), match='+1-(800)-555-2468'>

# Al profe no le sale al principio por que el esta usando re.match, y esa funcion solo busca en la primera linea.
# tenemos que usar re.search ya que esta funcion permite buscar en todo el documento.

# Hay que ir formando las expresiones poco a poco.

#       P       R       A       C       T       I       C       A

# Voy a practicar un poco a partir de nuestro archivo sample.txt

# Vamos a buscar la cadena comentada aqui abajo:

abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _w
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567	+1-(800)-555-2468
"""foo@demo.net"""	bar.ba@test.co.uk
www.demo.com	http://foo.co.uk/
http://regexr.com/foo.html?q=bar
https://mediatemple.net

# La expresion para detectar la cadena que queremos quedo asi:

\w\w\w\@\w\w\w\w.\w\w\w

# El punto se usa para encontrar cualquier caracter excepto nuevas lineas

print(re.search(r"\w\w\w\@\w\w\w\w.\w\w\w",info))

<re.Match object; span=(157, 169), match='foo@demo.net'>

# Como vemos, detecto la linea que queremos :D


# Vamos a buscar ahora lo comentado aqui abajo:

abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\\/|<>\"\'
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567    +1-(800)-555-2468
foo@demo.net    bar.ba@test.co.uk
www.demo.com    http://foo.co.uk/
"""http://regexr.com/foo.html?q=bar"""
https://mediatemple.net

# La expresion quedo asi:

\w\w\w\w:\/\/\w\w\w\w\w\w.\w\w\w\/\w\w\w.\w\w\w\w\?\w=\w\w\w

# Como vemos, algunos caracteres NO es necesario escaparlos (\)

print(re.search(r"\w\w\w\w:\/\/\w\w\w\w\w\w.\w\w\w\/\w\w\w.\w\w\w\w\?\w=\w\w\w",info))

<re.Match object; span=(219, 251), match='http://regexr.com/foo.html?q=bar'>


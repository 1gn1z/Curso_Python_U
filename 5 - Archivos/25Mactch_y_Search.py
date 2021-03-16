# Match y Search son 2 metodos muy importantes en expresiones regulares, son los 2 mas usuales.

import re

archivo = open("sample.txt",encoding="utf-8")
info = archivo.read()
archivo.close()
print(info)

# Para usar estos metodos dentro del print escribimos RE.MATCH()

print(re.match())

# Dentro de los parentesis del re.match primero tenemos que poner como parametro nuestra expresion regular:

print(re.match(r""))

# seguido de una coma, y el ARCHIVO O CADENA de donde vamos a buscar.

print(re.match(r"abcdefghijklmnopqrstuvwxyz",info))

# Dentro de las comillas de la letra r vamos a poner la expresion regular que vamos a evaluar, por ahora pondremos el abecedario
#
# La R quiere decir que es RAW DATA, osea, que NO vamos a omitir caracteres de la expresion regular a evaluar.

# el RAW DATA BUSCA TODA LA EXPRESION, sin omitir ni saltarse nada de la expresion 

# Como sabemos que la expresion existe, nos arroja que encontro el match, asi:

<re.Match object; span=(0, 26), match='abcdefghijklmnopqrstuvwxyz'>

# Si por ejemplo ponemos hasta la y, tambien encontrara la expresion por que aunq la z no este la expresion existe tal cual:

print(re.match(r"abcdefghijklmnopqrstuvwxy",info))

<re.Match object; span=(0, 25), match='abcdefghijklmnopqrstuvwxy'>  # Sin la z

# Si por ejemplo ponemos un 1 en medio:

print(re.match(r"abcdefghijk1lmnopqrstuvwxyz",info))

# NO encontrara la cadena xq NO TIENE UN UNO EN MEDIO, con el raw data tiene que coincidir exactamente como es:

None

# Ya vimo que el abecedario (en minusculas) existe, digamos ahora que queremos buscar los numeros:

print(re.match(r"0123456789",info))

# Pero devuelve NONE, lo que pasa es que MATCH busca la expresion regular, PERO SOLO EN LA PRIMERA LINEA de nuestro archivo
#----------------------------------------------------------------------------------------------------------------------------
# MATCH BUSCA LA EXPRESION REGULAR SOLO EN LA PRIMERA LINEA DE NUESTRO ARCHIVO!!!
#----------------------------------------------------------------------------------------------------------------------------

# Por eso NO encuentra la expresion, por que en la primera linea solo tenemos el abecedario en minusculas y mayusculas.

#----------------------------------------------------------------------------------------------------------------------------
# SI QUEREMOS BUSCAR EN TODO EL ARCHIVO USAMOS EL METODO SEARCH:
#----------------------------------------------------------------------------------------------------------------------------

print(re.search(r"0123456789",info))
<re.Match object; span=(54, 64), match='0123456789'>

# Y como vemos, ahora si encontró la expresion de los numeros :D

# Ahora con search podemos buscar cualquier expresion sin importar en que linea del archivo esté

print(re.search(r"http://foo.co.uk/",info))
<re.Match object; span=(201, 218), match='http://foo.co.uk/'>


# MATCH SOLO PARA LA PRIMERA LINEA          SEARCH PARA TODO EL DOCUMENTO (INCLUYENDO LA PRIMERA LINEA)
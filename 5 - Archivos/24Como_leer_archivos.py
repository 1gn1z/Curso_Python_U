# Vamos a aprender a ABRIR un archivo en python.

# NO siempre usaremos archivos PY, usaremos tambien archivos txt para ejemplos de cadenas distintas que detectaremos
# con expresiones regulares etc.

# Vamos a crear un MAIN y otro archivo pero en FORMATO TXT

# Vamos a entrar a la pagina regexr y vamos a genear un MATCH STRING, y copiamos el texto de ejemplo a nuestro archivo
# "sample.txt", el texto es el siguiente:
"""

abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\\/|<>\"\'
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567	+1-(800)-555-2468
foo@demo.net	bar.ba@test.co.uk
www.demo.com	http://foo.co.uk/
http://regexr.com/foo.html?q=bar
https://mediatemple.net

"""

# Ahora es nuestro archivo main vamos a importar una libreria que se usa para trabajar con expresiones regulares
# se llama RE

import re

# RE viene de Regular Expresions (Expresiones Regulares)

# Y para abrir un archivo simplemente escribimos una variable, por ejemplo "file", seguide de OPEN, parentesis,
# y entre comillas el nombre del archivo CON SU EXTENSION:

file = open("sample.txt")

# Y para asegurarnos que el encoding es el que estamos usando, agregamos una coma fuera de las comillas, seguido de la palabra
# ENCODING igual y entre comillas nuevamente "utf-8"

file = open("sample.txt",encoding="utf-8")

# La variable "file", es una variable que contiene una REFERENCIA al archivo, NO TIENE LA INFORMACION DEL ARCHIVO

# Para obtener la INFORMACION QUE CONTIENE ESE ARCHIVO se usa la variable que hace referencia al archivo y le agregamos el metodo READ
# Vamos a cambiar todo al español:


archivo = open("sample.txt",encoding="utf-8")   # REFERENCIA AL ARCHIVO
info = archivo.read()                           # LECTURA DEL ARCHIVO

# Una vez leida la informacion del archivo tenemos que cerrarlo, simplemente escribimos archivo.close

archivo.close()

# Haciendo esto la memoria se libera de todo lo que contiene el archivo, es buena practica cerrar los archivos que no usaremos o usamos

# Para compronar que abrimos y leimos el archivo correctamente haremos un print:
# 
print(info) 

# Funciona nuestro codigo, se imprimie todo lo que tiene dentro nuestro archivo
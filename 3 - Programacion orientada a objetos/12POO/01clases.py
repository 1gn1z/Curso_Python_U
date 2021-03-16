#   C   L   A   S   E   S

# No podemos tener un codigo con miles y miles de funciones, es poco legible y poco practico.
# Aqui entra la PROGRAMACION ORIENTADA A OBJETOS.

# Hay un juego llamado "Tibia", donde los jugadores pueden ser: Hechiceros, Druidas, Caballeros y Paladines
# Los hechiceros tienen menos vida pero mas magia
# Los caballeros tienen mas vida pero menos magia
# Los paladines atacan a distancia, decentes en magia pero no tanto como los hechiceros

# Mencionamos esto por que para ejercicio de esta seccion vamos a codificar a los jugadores:

# Las clases SON PLANTILLAS, de como se veran los OBJETOS. 

# Las clases en python, EMPIEZAN CON MAYUSCULAS SIEMPRE!!!. No afecta el código, es una convencion

# Se definen unsando la palabra reservada CLASS, seguida del nombre de la clase, en nuestro caso "Player"

# Las clases tienen que tener sus datos(ATRIBUTOS) y funcionalidad(Métodos).

# Los METODOS son LAS FUNCIONES QUE ESTAN DENTRO DE CLASES.     FUNCION DENTRO DE CLASES = MÉTODOS

# Método y funcion son lo mismo en el aspecto de que ambos consisten en ejecutar una pieza de código, pero en los lenguajes POO
# generalmente, si tenemos una funcion dentro de una clase pasa a llamarse Metodo:

# Ya definida nuestra clase, procedemos a agregarle sus Atributos.

class Player:
    hit_points = 50
    mana = 50
    vocacion = "sorcerer"

# Hit points vendria siendo su vida, es decir, tiene una resistencia de 50 golpes
# el mana su magia, su energia para los hechizos
# y la vocacion pues eso, su vocacion xd, en este caso "Sorcerer" (Hechicero).

# Ahora, en nuestro archivo MAIN, para obtener todo el codigo de otro archivo (player.py), usamos IMPORT. y escribimos lo siguiente

# from player import Player

# From (DE) nuestra libreria player, nuestro archivo player.py, queremos IMPORT(ar), nuestra CLASE Player.

# Despues, imprimimos algun atributo para ver si esta correcto. Lo haremos indicando con un PUNTO despues de la clase el 
# ATRIBUTO deseado, por ejemplo:

print(Player.hit_points)
#     CLASE . ATRIBUTO
# 
# Me dio un error por que llame los archivos "001player.py" y "000main.py", mejor los deje como "player.py" y "main.py" y no
# mando errores ya, asi los dejare para no tener errores.

# EL main.py quedo asi:

#from player   import  Player
#DE   Libreria importa Clase
# La libreria es nuestro archivo player.py

from player import Player

print(Player.hit_points)

print(Player.mana)

print(Player.vocation)

# Al ejecutarlo, nos damos cuenta que importamos la clase "player" exitosamente :)
# Hicimos nuestra primera clase en python :3

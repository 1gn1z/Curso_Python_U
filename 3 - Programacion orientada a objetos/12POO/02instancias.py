# Ya creamos la clase, pero en si misma la clase no es muy util, son buenas para guardar info obvio
# PERO! si modificamos algo de la clase, afectara a todas las partes donde las estemos usando.

# Por eso es mejor crear objetos a partir de nuestras clases, a esto se le llama INSTANCIAR.

# UN OBJETO ES UNA INSTANCIA DE UNA CLASE.

# Los objetos son COPIAS DE NUESTRA CLASE, pero cada objeto tiene sus atributos adicionales.

# En nuestro caso, cada instancia (objeto) de player, tendra sus hit points, su mana y su vocacion 

# Veremos como crear objetos a partir de nuestras clases.

# En nuestro archivo de main haremos un nuevo objeto de la clase player:

sorcerer = Player()

# Aqui estamos indicando que sorcerer sera un NUEVO OBJETO (INSTANCIA), de nuestra clase player.

# En nuestra clase Player, cambiaremos la vocacion a "No vocation". para poder usar la que queramos en las diferentes instancias(objetos)

from player import Player

print(Player.hit_points)
print(Player.mana)
print(Player.vocation)

sorcerer = Player()

print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)

50
50
No vocation
50
50
No vocation

# Como vemos, ambos jugadores, tienen 50 de hit points, 50 de mana y no tienen vocacion.

# PERO! podemos modificar los datos (atributos) de una instancia (objeto), SIN MODIFICAR LA CLASE.

# Esto lo hacemos abajo de donde creamos nuestro sorcerer, escribimos sorcerer PUNTO y el atributo que vamos a modificar (Re asignar)

# Por ejemplo, como es el hechicero tiene menos vida que el guerrero, pero como es el hechicero tiene mas mana:

# MANÁ: En términos de juegos de ficción es una fuente de energía evocada principalmente en juegos de rol, 
# así como en el juego de cartas coleccionables



sorcerer = Player()

sorcerer.hit_points = 40

sorcerer.mana = 80

sorcerer.vocation = "sorcerer"

# Al probar nuestro codigo vemos que nuestro hechicero ya tiene 40 hit points, 80 de mana y su vocacion es sorcerer.

# De la misma forma podemos crear otra variable llamada "knigt" (caballero), especificando que es una instancia de Player.

knight = Player()

# El caballero es mas fuerte que el hechicero, asi que le ponemos mas hit points y menos mana. Al reves que el hechicero
knight.hit_points = 80
knight.mana = 40
knight.vocation = "knight"

# Como podemos ver, cada objeto (instacia) SE BASA en la CLASE, pero podemos MODIFICAR sus atributos. IMPORTANTE ok ;)
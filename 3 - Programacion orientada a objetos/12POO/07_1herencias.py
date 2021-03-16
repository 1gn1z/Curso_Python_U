# En python TODO ES UN OBJETO!, y todas las clases heredan de la clase objeto

# En python la HERENCIA es como en la vida real, de nuestros padres heredamos el color de ojos, el color de pelo
# El color de piel, etc.

# PERO! tambien tenemos cosas distintas, podemos ser mas altos, pueden gustarnos los videojuegos y a ellos no, etc.

# La herencia PERMITE HEREDAR de ciertas clases para no tener que repetir sus atributos o funciones
# Pero ademas podemos MODIFICAR o SOBREESCRIBIR sus atributos y poner los atributos y funciones que queramos :D Para no repetir codigo.


# Seria molesto que cada vez que queramos crear un nuevo mago, tengamos que crear una nueva instancia y modificar cada uno
# de sus atributos por separado.

# Lo mismo para los caballeros, los paladines y los druidas.

# Vamos a aprender como hacer una clase Sorcerer, que ira directo en la clase player, pero que tenga atributos distintos:

# En nuestra clase Player vamos a especificar valores por defecto para todas las instancias creadas de esta clase
# Haremos esto xq es lo normal, cada jugador por defecto no tiene vocacion hasta que se convierte en mago o caballero x ejemplo.

# Vamos a convertir todo a ingles xq es el standar

class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)
#        self.vocation = kwargs.get("vocarion","No vocation")       Quitamos estos atributos xq el jugador por defecto no tiene
#        self.spell = kwargs.get("spell","Puff")                    vocacion ni hechizos

    def cast_spell(self):
        return self.spell    

# Vamos a borrar la vocacion y la magia de nuestro jugador, lo unico que se podra modificar es su vida y mana

# Antes dijimos que en python TODO ES UN OBJETO, todas las clases heredan de OBJETO
# Podemos indicar entre parentesis en la clase Player un objeto
#   class Player(object): LINEA 24

# En python3 NO TENEMOS QUE DECIR explicitamente esto, Asi que podemos ponerlo O DEJARLO EN BLANCO COMO LO TENIAMOS

# Ahora crearemos una nueva clase, llamada sorcerer, y entre parentesis ponemos la clase de la que queremos heredar
# queremos heredar todos los atributos y metodos de la clase Player, asi que lo escribimos asi:

# Con el sistema de herencia en python, podemos MODIFICAR y AÑADIR nuevos metodos y atributos a las clases, ademas de
# llamar metodos de otras clases heredadas.

# Como esta es nuestra clase Sorcerer, Si queremos que tenga un atributo "Vocation", NO que tome el atributo
# por defecto "No vocation", asi que se lo agregamos:

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Igne fulgur"
    movement_speed = 20
    mana = 80
    hit_points = 40

# Vamos a crear al Knight tambien:

class Knight(Player):
    vocation = "Knight"
    spell = "impetu"
    movement_speed = 60
    mana = 20
    hit_points = 80



print("\nEl Sorcerer tiene:\n")
print(Sorcerer.vocation)
print(Sorcerer.spell)
print(Sorcerer.movement_speed)
print(Sorcerer.mana)
print(Sorcerer.hit_points)


print("\nEl Knight tiene:\n")
print(Knight.vocation)
print(Knight.spell)
print(Knight.movement_speed)
print(Sorcerer.movement_speed)





#       H       E       R       E       N       C       I       A       VIDEO 2


#  ERRORES POR QUE VAN SEPARADOS LOS ARCHIVOS DE CLASES (PLAYER) Y EL MAIN

class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def cast_spell(self):
        return self.spell    


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Igne fulgur"
    movement_speed = "20"
#   mana = 80
#   hit_points = 40

class Knight(Player):
    vocation = "Knight"
    spell = "impetu"
    movement_speed = "60"
#   mana = 20
#   hit_points = 80           # Estos atributos los definimos en la instancia, xq el mana y la vida son del metodo init:
                              # ejemplo:  knight = Player.Knight(hit_points=80,mana=20)

print("\nEl Sorcerer tiene:\n")
print(Sorcerer.vocation)
print(Sorcerer.spell)
print(Sorcerer.movement_speed)
print(Sorcerer.mana)
print(Sorcerer.hit_points)


print("\nEl Knight tiene:\n")
print(Knight.vocation)
print(Knight.spell)
print(Knight.movement_speed)
print(Knight.mana)
print(Knight.hit_points)


# En esta leccion, para repasar y practicar un poquito, vamos a crear las instancias de DRUID y PALADIN

# Recordemos que para heredar de una clase, ponemos dentro del parentesis de nuestra clase nueva, el nombre de la clase
# de la cual vamos a heredar. por ejemplo ###   class Druid(Player):

# Creemos la clase DRUID y PALADIN


class Druid(Player):
    vocation = "Druid"
    spell = "Hechizo de Druida"
    movement_speed = "20"

class Paladin(Player):
    vocation = "Paladín"
    spell = "Hechizo de Paladín"
    movement_speed = "80"

# Recordemos que los atributos que heredamos de la clase pladre "Player", podemos SOBREESCRIBIRLOS

# Los atributos de INIT, tambien podemos MODIFICARLOS o SOBREESCRIBIRLOS, PERO! desde la instancia misma xq recordemos
# que es un desempaquetamiento de diccionario con KWARG

# Por ejemplo:

#           knight = player.Knight(hit_points=80,mana=20)

         ###     P       L       A       Y       E       R       (C      L       A       S       E       S)

class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def cast_spell(self):
            return self.spell

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Sorcerer Spell"
    movement_speed = "20"

class Knight(Player):
    vocation = "Knight"
    spell = "Knight Spell"
    movement_speed = "60" 

                                         M       A       I       N



 import player               ### IMPORTAMOS LA LIBRERIA PLAYER, QUE ES NUESTRO ARCHIVO player.py

sorcerer = player.Sorcerer(hit_points=40,mana=80)

print("\nEL Sorcerer tiene:\n")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.cast_spell())
print(sorcerer.movement_speed)

knight = player.Sorcerer(hit_points=80,mana=20)

print("\nEL Knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.cast_spell())
print(knight.movement_speed)

# Vamos a crear las instancias de druid y paladin


# Creo por fin entendi xq esto es una funcion, lo que pasa es que esta funcion no solo muestra un valor como vocacion o mana o vida
# esta funcion lo que hace es ARROJAR EL HECHIZO, no solo mostrar el nombre del hechizo, por eso es una funcion y no
# un atributo mas. (creo xd)


    def cast_spell(self):
            return self.spell

# Para ahorrarnos todos esos prints, PODEMOS PONERLOS TODOS EN LA MISMA LINEA, por medio de la funcion FORMAT.

print("El Paladin tiene: {}".format(hit_points,mana,vocation,cast_spell(),movement_speed))

print("El Paladin tiene: {} hit points, {} mana, {} vocacion, {} hechizo, y {} velocidad".
format(paladin.hit_points,paladin.mana,paladin.vocation,paladin.cast_spell(),paladin.movement_speed))

# Haciendo esto podemos mostrar todos los atributos con un solo print, y usando el metodo o la funcion FORMAT como vemos :D
# 

# Para que quede un poco mas claro podemos hacerlo asi.

print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(paladin.vocation,
       paladin.hit_points,
       paladin.mana,
       paladin.cast_spell(),
       paladin.movement_speed))



 
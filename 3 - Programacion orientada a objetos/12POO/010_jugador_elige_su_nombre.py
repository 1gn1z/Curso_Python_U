

# Permitiremos que nuestros jugadores eligan un nombre :D

# lo primero que haremos es, en nuestra clase player, dentro del metodo INIT, pondremos:

self.name = input("Elige tú nombre: ")


# y en STR, donde imprimimos las caracteristicas de nuestra instancia pondremos llaves {}, seguido de, por ejemplo, es un
# para que diga "Kevor es un mago"

        return "\n{} es un {} tiene: {} hit points y {} de mana, su hechizo es {} y tiene {} de velocidad".format(
        self.name,        


# Seguido de, dentro del format, justo al inicio, pondremos: self.name
        self.name,        

# No olvidar la coma.
# Despues de las primeras llaves que indican el nombre, dejar un espacio para que no se una el nombre del jugado con la palabra ES
#
# Ya listo queda asi:

class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.name = input("Elige tú nombre: ")     # Añadiendo esta linea pedimos mediante un input el nombre que quiera el jugador
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self):      
        return "\n{} es un {} tiene: {} hit points y {} de mana, su hechizo es {} y tiene {} de velocidad".format(
        self.name,                                 # Las primeras llaves van a albergar este parametro "self.name"     
        self.vocation,
        self.hit_points,
        self.mana,
        self.cast_spell(),
        self.movement_speed)

    def cast_spell(self):
        return self.spell


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Sorcerer Spell"
    movement_speed = "20"

import player

sorcerer = player.Sorcerer(hit_points=40,mana=80)
print(sorcerer)    
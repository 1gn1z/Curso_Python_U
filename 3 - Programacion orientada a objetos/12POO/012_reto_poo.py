
# Hacer una clase de troll.
# hacer unos 5 tipos (clases) de trolls del juego de tibia que hereden de la clase padre troll

# la clase padre que almacene una lista de los items que dan los trolls

# color por defecto de los trolls, y ahi le añadimos mas madres del juego de tibia.

# Ya emputados podemos hacer otro monstruo por ejemplo los ORCS

# Podemos sobreescribir INIT Y STR.

# Troll por defecto, que sera la clase padre_

# TROLL : 50 hitpoints, 290 mana, 20 movement speed, color por defecto rojo, 
# items gold coins, hand axes, leather boots, leather helmets, meat, spears,


# CLASE PADRE CON SUS ATRIBUTOS POR DEFECTO!

class Troll:
    vocation = "Troll"
    spell = "Puff"
    movement_speed = "20"
    items = ["gold coins","hand axes","leather boots","leather helmets","meat","spears"]

    def __init__(self,**kwargs):
        self.name = input("Elige tu nombre")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self):
        return "\n es un {}, tiene: {} de hit points y {} de mana, su hechizo es {} y tiene {} de velocidad".format(
        self.name,
        self.vocation,
        self.mana,
        self.hit_points,
        self.cast_spell(),
        self.movement_speed,    
        )

    def cast_spell(self):
        return self.spell

# RECORDAR QUE YA TENEMOS UNA CLASE PADRE POR DEFECTO

class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"

    def __init__(self,**kwargs):
        self.name = input("Elige tú nombre: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self):      
        return "\n{} es un {} tiene: {} hit points y {} de mana, su hechizo es {} y tiene {} de velocidad".format(
        self.name,        
        self.vocation,
        self.hit_points,
        self.mana,
        self.cast_spell(),
        self.movement_speed)

    def cast_spell(self):
        return self.spell

# Ya que la clase troll hereda TODOS los atributos del player

class Troll(Player):
    vocation = "Troll"
    spell = "Hechizo de Troll"
    movement_speed = "20"

# Solo falta reasignarle la vida y el mana:

troll = player.Troll(hit_points=50,mana=290)

# Y simplemente imprimimos al troll:

print(troll)

# Me quedo asi y funciono chido :D

class Troll(Player):
    vocation = "Troll"
    spell = "Hechizo de Troll"
    movement_speed = "20"
    items = ["gold coins","hand axes","leather boots","leather helmets","meat","spears"]

    def __str__(self):      
        return "\n{} es un {} tiene: {} hit points y {} de mana, su hechizo es {} ,tiene {} de velocidad y carga los siguientes items: {}".format(
        self.name,        
        self.vocation,
        self.hit_points,
        self.mana,
        self.cast_spell(),
        self.movement_speed,
        self.items)

# Simplemente añadi la variable de items, con una lista que contiene los elementos que carga el troll.
# Ademas sobreescribi la STR para añadir self.items

class Troll_Champion(Troll,Player):     

# NO ES NECESARIO PONER AMBAS, YA QUE ESTA INSTANCIA HEREDA DE TROLL Y TROLL # HEREDA DE PLAYER. 
# por lo tanto YA TENEMOS TODAS LAS FUNCIONES Y METODOS DE LA CLASE TROLL Y DE LA CLASE PLAYER

# YA LO LOGRE, QUEDO ASI:

class Troll_champion(Troll):    # Troll_champion hereda de TROLL, que a su vez hereda de Player :D
    vocation = "Troll Champion"
    spell = "T Champ Spell"
    movement_speed = "40"
    items = ["gold coins","leather boots","meat","spears"]

# Aqui ya ni siquiera hubo que sobreescribir el metodo STR, por que la clase TROLL ya tiene sobreescrito que tambien imprima
# la variable items, que es la lista de objetos que carga el troll.
#
# Simplemente sobreescribimos la variable items con los objetos que carga el troll champion.

# Ya nadamas reasignamos sus valores por defecto (hit_points y mana), esto desde la creacion de la instancia:

troll_champion = player.Troll_champion(hit_points=75,mana=350)

# Ya hicimos el troll champion, que es un troll que hereda de la clase troll, que a su vez hereda de player.
# ahora simplemente tenemos que hacer las otras clases de troll que heredaran igual que el troll champion, es decir
# de la clase Troll, y de la clase padre Player.

class Troll_swamp(Troll):
    vocation = "Troll Swamp"
    spell = "T Swamp Magic"
    movement_speed = "25"
    items = ["carry fish", "gold coins", "leather boots", "mouldy cheeses", "spears", "torches"]

troll_swamp = player.Troll_swamp(hit_points=55,mana=320)

print(troll_swamp)

# CORRECTO!

class Island_troll(Troll):
    vocation = "Island Troll"
    spell = "Island Spell Troll"
    movement_speed = "20"
    items = ["gold coins", "hand axes", "leather boots", "leather helmets", "spears", "wood", "wooden shields"]

island_troll = player.Island_troll(hit_ponits=50,mana=290)
print(island_troll)

# TODO BIEN :D, solo falta la ultima clase de troll que son los trolls de hielo:

class Frost_troll(Troll):
    vocation = "Frost Troll"
    spell = "Troll Ice Magic"
    movement_speed = "23"
    items = ["fish", "gold coins", "rapiers", "spears", "wooden shields"]

frost_troll = player.Troll(hit_points=55,mana="300")
print(frost_troll)

# LISTO :) Luego hago otra clase como los orc

# Vamos a hacer los orcos de una vez, solo que son un chingo, 14 :O

class Orc(Player):
    vocation = "Orc"
    spell = "Orc Magic"
    movement_speed = "25"
    items = ["gold coins","meat"]

orc = player.Orc(hit_points=70,mana=300)
print(orc)


class Orc_warrior(Orc):
    vocation = "Orc Warrior"
    spell = "WarriORC spell"
    movement_speed = "50"
    items = ["broken helmets", "gold coins", "meat"]

orc_warrior = player.Orc_warrior(hit_points=125,mana="360")

class Orc_spearmen(Orc):
    vocation = "Orc Spearmen"
    spell = "Orc Spear Spell"
    movement_speed = "38"
    items = ["gold coins", "meat", "spears", "studded legs"]

orc_spearmen = player.Orc_spearmen(hit_points=105,mana=310)

class Orc_rider(Orc):
    vocation = "Orc Rider"
    spell = "Orc Ridah Magic"
    movement_speed = "60"
    items = ["gold coins", "meat", "orc leather", "warwolf fur", "wolf teeth chain"]

orc_rider = player.Orc_rider(hit_points=180,mana=490)

class Orc_marauder(Orc):
    vocation = "Orc Marauder"
    spell = "Orc Marauder Spell"
    movement_speed = "60"
    items = ["gold coins", "meat", "shaggy tails"]

orc_marauder = player.Orc_marauder(hit_points=235,mana=490)

class Orc_leader(Orc):
    vocation = "Orc Leader"
    spell = "Orc Leader Magic"
    movement_speed = "70"
    items = ["brown mushrooms", "fish", "gold coins", "orc leather", "plate shields", "throwing knives"]

orc_leader = player.Orc_leader

class Orc_cultist(Orc):
    vocation = "Orc Cultist"
    spell = "Orc Cultispell"
    movement_speed = "80"
    items = ["gold coins", "orc tusks", "strong health potions"]

orc_cultist = player.Orc_cultist

class Orc_berserker(Orc):
    vocation = "Orc Berserker"
    spell = "Berserker magic"
    movement_speed = "100"
    items = ["gold coins", "ham", "orcish gear"]

orc_berserker = player.Orc_berserker

# LISTO NENA ;)
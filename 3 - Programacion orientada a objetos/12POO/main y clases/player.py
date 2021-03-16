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


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Sorcerer Spell"
    movement_speed = "20"

    def cast_spell(self):
        return "{} y Curación".format(self.spell)

class Knight(Player):
    vocation = "Knight"
    spell = "Knight Spell"
    movement_speed = "60"

class Druid(Player):
    vocation = "Druid"
    spell = "Druid Spell"
    movement_speed = "20"

    def cast_spell(self):
        return "{} y Curación".format(self.spell)

class Paladin(Player):
    vocation = "Paladin"
    spell = "Paladin spell"
    movement_speed = "80"

#                           C   L   A   S   E   S       D   E       T   R   O   L   L   S

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

class Troll_champion(Troll):
    vocation = "Troll Champion"
    spell = "T champ spell"
    movement_speed = "40"
    items = ["gold coins","leather boots","meat","spears"]

class Troll_swamp(Troll):
    vocation = "Troll Swamp"
    spell = "T Swamp Magic"
    movement_speed = "25"
    items = ["fish", "gold coins", "leather boots", "mouldy cheeses", "spears", "torches"]

class Island_troll(Troll):
    vocation = "Island Troll"
    spell = "Island Spell Troll"
    movement_speed = "20"
    items = ["gold coins", "hand axes", "leather boots", "leather helmets", "spears", "wood", "wooden shields"]    

class Frost_troll(Troll):
    vocation = "Frost Troll"
    spell = "Troll Ice Magic"
    movement_speed = "23"
    items = ["fish", "gold coins", "rapiers", "spears", "wooden shields"]

#                               C   L   A   S   E   S       D   E       O   R   C   O   S

class Orc(Player):
    vocation = "Orc"
    spell = "Orc Magic"
    movement_speed = "25"
    items = ["gold coins","meat"]

    def __str__(self):      
        return "\n{} es un {} tiene: {} hit points y {} de mana, su hechizo es {} ,tiene {} de velocidad y carga los siguientes items: {}".format(
        self.name,        
        self.vocation,
        self.hit_points,
        self.mana,
        self.cast_spell(),
        self.movement_speed,
        self.items)

class Orc_warrior(Orc):
    vocation = "Orc Warrior"
    spell = "WarriORC spell"
    movement_speed = "50"
    items = ["broken helmets", "gold coins", "meat"]

class Orc_spearmen(Orc):
    vocation = "Orc Spearmen"
    spell = "Orc Spear Spell"
    movement_speed = "38"
    items = ["gold coins", "meat", "spears", "studded legs"]

class Orc_rider(Orc):
    vocation = "Orc Rider"
    spell = "Orc Ridah Magic"
    movement_speed = "60"
    items = ["gold coins", "meat", "orc leather", "warwolf fur", "wolf teeth chain"]

class Orc_marauder(Orc):
    vocation = "Orc Marauder"
    spell = "Orc Marauder Spell"
    movement_speed = "60"
    items = ["gold coins", "meat", "shaggy tails"]

class Orc_leader(Orc):
    vocation = "Orc Leader"
    spell = "Orc Leader Magic"
    movement_speed = "70"
    items = ["brown mushrooms", "fish", "gold coins", "orc leather", "plate shields", "throwing knives"]

class Orc_cultist(Orc):
    vocation = "Orc Cultist"
    spell = "Orc Cultispell"
    movement_speed = "80"
    items = ["gold coins", "orc tusks", "strong health potions"]


class Orc_berserker(Orc):
    vocation = "Orc Berserker"
    spell = "Berserker magic"
    movement_speed = "100"
    items = ["gold coins", "ham", "orcish gear"]
  
import player

sorcerer = player.Sorcerer(hit_points=40,mana=80)
knight = player.Knight(hit_points=80,mana=20)
druid = player.Druid(hit_points=40,mana=80)
paladin = player.Paladin(hit_points=60,mana=60)

# Clases de Trolls
troll = player.Troll(hit_points=50,mana=290)
troll_champion = player.Troll_champion(hit_points=75,mana=350)
troll_swamp = player.Troll_swamp(hit_points=55,mana=320)
island_troll = player.Island_troll(hit_points=50,mana=290)
frost_troll = player.Frost_troll(hit_points=55,mana="300")

# Clases de Orcos
orc = player.Orc(hit_points=70,mana=300)
orc_warrior = player.Orc_warrior(hit_points=125,mana=360)
orc_spearmen = player.Orc_spearmen(hit_points=105,mana=310)
orc_rider = player.Orc_rider(hit_points=180,mana=490)
orc_marauder = player.Orc_marauder(hit_points=235,mana=490)
orc_leader = player.Orc_leader(hit_points=300,mana=380)
orc_cultist = player.Orc_cultist(hit_points=190,mana=400)
orc_berserker = player.Orc_berserker(hit_points=210,mana=590)



print(sorcerer)
print(knight)
print(druid)
print(paladin)

print(troll)
print(troll_champion)
print(troll_swamp)
print(island_troll)
print(frost_troll)

print(orc)
print(orc_warrior)
print(orc_spearmen)
print(orc_rider)
print(orc_marauder)
print(orc_leader)
print(orc_cultist)
print(orc_berserker)


#print(sorcerer)
# Defimos el metodo __str__ en la clase player, y le pasamos todos los parametros
# Asi que, como el metodo str tambien usa el SELF, simplemente lo llamamos desde la instancia que queramos :D
# y como el metodo str indica como se imprimen las instancias, simplemente ponemos un print con el nombre 
# de la instancia, como vemos arriba en la linea 5   

#   P   R   I   N   T   S       A   N   T   E   R   I   O   R   E   S   (SIN METODO __STR__)

"""
print("\nEL Paladin tiene:\n")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
print(paladin.cast_spell())
print(paladin.movement_speed) 
"""

#   P   R   I   N   T   S       A   N   T   E   R   I   O   R   E   S   (SIN METODO __STR__ PERO CON MEDOTO FORMAT)

"""
print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(sorcerer.vocation,
       sorcerer.hit_points,
       sorcerer.mana,
       sorcerer.cast_spell(),
       sorcerer.movement_speed)) 
"""
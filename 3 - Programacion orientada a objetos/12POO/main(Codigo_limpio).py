import player    

sorcerer = player.Sorcerer(hit_points=40,mana=80)  

print("\nEl Sorcerer tiene:\n")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = player.Knight(hit_points=40,mana=80)            

print("\nEl Knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())


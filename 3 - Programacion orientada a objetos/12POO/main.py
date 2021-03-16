#from player import Player
"""
#print("\nEl player tiene:\n")
#print(Player.hit_points)
#print(Player.mana)
#print(Player.vocation)

sorcerer = Player(40,80,"Sorcerer","Igne fulgur")   # Haciendo esto, ya podemos borrar las declaraciones de abajo
                                                    # Por que ya especificamos los atributos en el metodo INIT
                                                    # Y entre los parentesis les damos los valores a los atributos de
                                                    # de los parentesis del metodo init de la clase Player.                            
#sorcerer.hit_points = 40
#sorcerer.mana = 80
#sorcerer.vocation = "sorcerer"
#sorcerer.hechizo = "Igne fulgur"

print("\nEl Sorcerer tiene:\n")

print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = Player(80,20,"Knight","Impetu")            # Aqui igual podemos borrar las asignaciones de abajo por que ya estan
                                                    # espeficidos los atributos en el metodo init 
                                                    # y a la hora de crear la instancia los atributos ya estan asignados aqui.

#knight.hit_points = 80
#knight.mana = 20
#knight.vocation = "knight"
#knight.hechizo = "Impetu"

print("\nEl knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

# RETO!!! Crear una nueva variable que sea otra instancia de player que sea un Paladin, que tenga 60 de vida
# 40 de mana, un hechizo diferente y de vocacion paladin obviamente xD.

# RETO CUMPLIDO!!!
paladin = Player(60,40,"Paladin","Fortis magica")

print("\nEl Paladin tiene:\n")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
print(paladin.lanzar_hechizo())

druid = Player(50,80,"Druida","Anima mea")

print("\nEl Druida tiene:\n")
print(druid.hit_points)
print(druid.mana)
print(druid.vocation)
print(druid.lanzar_hechizo())



sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"')

print("\nEl Sorcerer tiene:\n")
print("Vida:",sorcerer.hit_points)
print("Maná:",sorcerer.mana)
print("Vocación:",sorcerer.vocation)
print("Hechizo:",sorcerer.lanzar_hechizo())

knight = Player(80,20,"Knight",'"Impetu"')

print("\nEl Knight tiene:\n")
print("Vida:",knight.hit_points)
print("Maná:",knight.mana)
print("Vocación:",knight.vocation)
print("Hechizo:",knight.lanzar_hechizo())

paladin = Player(60,40,"Paladin",'"Fortis magica"')

print("\nEl Paladín tiene:\n")
print("Vida:",paladin.hit_points)
print("Maná:",paladin.mana)
print("Vocación:",paladin.vocation)
print("Hechizo:",paladin.lanzar_hechizo())

druid = Player(50,80,"Druida",'"Anima mea"')

print("\nEl Druida tiene:\n")
print("Vida:",druid.hit_points)
print("Maná:",druid.mana)
print("Vocación:",druid.vocation)
print("Hechizo:",druid.lanzar_hechizo())



sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",spell="Igne fulgur")  # EN LA INSTANCIA NO SE PONEN LAS COMILLAS

print("\nEl Sorcerer tiene:\n")
print("Vida:",sorcerer.hit_points)
print("Maná:",sorcerer.mana)
print("Vocación:",sorcerer.vocation)
print("Hechizo:",sorcerer.cast_spell())

knight = Player(hit_points=80,mana=20,vocation="knight",spell="Impetu")
     
print("\nEl Knight tiene:\n")
print("Vida:",knight.hit_points)
print("Maná:",knight.mana)
print("Vocación:",knight.vocation)
print("Hechizo:",knight.cast_spell())     

paladin = Player(hit_points=60,mana=40,vocation="Paladín",spell="Fortis magica")

print("\nEl Paladín tiene:\n")
print("Vida:",paladin.hit_points)
print("Maná:",paladin.mana)
print("Vocación:",paladin.vocation)
print("Hechizo:",paladin.cast_spell())  

druid = Player(hit_points=50,mana=80,vocation="Druida",spell="Anima mea")

print("\nEl Paladín tiene:\n")
print("Vida:",druid.hit_points)
print("Maná:",druid.mana)
print("Vocación:",druid.vocation)
print("Hechizo:",druid.cast_spell()) 

"""
#from player import Player
import player       # Esto indica que vamos a importar TODO lo de la libreria player (nuestro archivo player.py)

#sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",spell="Igne fulgur")  

# El Sorcerer Ya no es un jugador, ahora es una instancia de la clase Sorcerer:

# le vamos a quitar el hechizo y la vocacion xq ya los definimos en la nueva clase que sera para todos los sorcerers.
"""class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Igne fulgur"
    movement_speed = "20"
"""
# Osea, cualquier instancia que se cree de esta clase llamada Sorcerer, hereda todos los atributos y funciones que tenemos por
# defecto en la clase padre (Player), y ademas hereda o tiene los atributos y funciones que definamos en la clase Sorcerer :D

sorcerer = player.Sorcerer(hit_points=40,mana=80)  # Solo modificamos los hit_points y el mana, los demas atributos
                                                   # son los que tendra de la clase Sorcerer
print("\nEl Sorcerer tiene:\n")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.cast_spell())
print(sorcerer.movement_speed)

knight = player.Knight(hit_points=80,mana=20)            

print("\nEl Knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.cast_spell())
print(knight.movement_speed)













































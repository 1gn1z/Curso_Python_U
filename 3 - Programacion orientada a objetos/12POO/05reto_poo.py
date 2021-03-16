# RETO!!! Crear 2 variables, creando una nueva instancia de paladin(ya) y de druida.

# Para practicar :)


paladin = Player(60,40,"Paladin","Fortis magica")

print("\nEl Paladin tiene:\n")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
print(paladin.lanzar_hechizo())


# DRUIDA  Druida. Denominación de los sacerdotes del sistema religioso celta.
# Fueron los "filósofos naturales" y enseñaban la inmortalidad del alma humana. 
# La palabra "Druida" parece provenir de la palabra céltica "dur, derw" que significa "roble", 
# el árbol sagrado de los druidas, que buscaban en él el muérdago sagrado. 


druid = Player(50,80,"Druida","Anima mea")

print("\nEl Druida tiene:\n")
print(druid.hit_points)
print(druid.mana)
print(druid.vocation)
print(druid.lanzar_hechizo())

# CUMPLIDO!!!

# __str__

# Al doble guion bajo se le llama "DUNDER", el guion bajo en ingles se dice "underscore", doble se dice "double"
# entonces double + underscore = dunder

# Asi que en python es usual decir "dunder init dunder" y/o "dunder str dunder"

# STR es un metodo especial QUE TIENEN TODAS LAS CLASES en python, pero a diferencia de init
# STR DEFINE COMO SE IMPRIME LA INSTANCIA DE NUESTRA CLASE.

# Cuando usemos print en la clase, va a decir que es lo que vamos a imprimir.

# Vimos como imprimir todos los atributos de nuestra instancia con un solo print con el metodo format:

print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(sorcerer.vocation,
       sorcerer.hit_points,
       sorcerer.mana,
       sorcerer.cast_spell(),
       sorcerer.movement_speed))

# justo abajo del metodo init definimos el metodo str:
# y este metodo va a retornar una cadena

# Como vemos, al igual que el metodo init tambien lleva el parametro self.

def __str__(self):
    return

# Ahora vamos a pasarle el codigo que queremos imprimir, osea, el print PERO SOLO EL TEXTO SIN EL PARENTESIS DEL PRINT:
# 
def __str__(self):
    return "\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".format(sorcerer.vocation,
    sorcerer.hit_points,
    sorcerer.mana,
    sorcerer.cast_spell(),
    sorcerer.movement_speed)  

# ahora, nos devuelve error, xq tenemos que pasarle SELF en lugar de la instancia (En este caso sorcerer).

def __str__(self):          # SIN EL PRINT, SOLO LA CADENA
    return "\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".format(self.vocation,
    self.hit_points,        
    self.mana,              # Este metodo ya tiene definidos todos los parametros, asi que solo lo llamamos desde la instancia
    self.cast_spell(),      # que queramos :D. Y como str DEFINE como se imprime la instancia, para llamarla simplemente
    self.movement_speed)    # usamos un print y entre los parentesis la instancia que queramos, por ejemplo:
                            # print(instancia),         print(sorcerer)


# De este modo, este return de el metodo STR DEVUELVE LA MISMA CADENA, PERO! EL SELF SE REEMPLAZA POR LA INSTANCIA desde donde
# la llamemos. Si la llamamos del sorcerer se mostrara con los datos del sorcerer, y asi con el knight, el druid, etc.

# Ahora, en nuestro main, en lugar de poner TODOOOO ESTE CODIGO:
# 
print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".format(sorcerer.vocation,
       sorcerer.hit_points,
       sorcerer.mana,
       sorcerer.cast_spell(),
       sorcerer.movement_speed))
# 
# lo unico que tenemos que hacer es IMPRIMIR LA INSTANCIA QUE QUERAMOS. Asi:

print(sorcerer)

# STR define como se IMPRIME la instancia desde donde la invoquemos, por eso ocupa el parametro SELF.

# como ya definimos el metodo str con todos los parametros, simplemente imprimimos la instancia que queramos :D


# PERO!!! si imprimimos la instancia SIN DEFINIR EL METODO STR, pasa esto:

<player.Sorcerer object at 0x00420AF0>

# Como vemos nos dice la clase (player.Sorcerer), y es un objeto, y nos dice en la direccion de memoria en la que
# esta instancia esta localizada, en mi caso es 0x00420AF0

# Ahora podemos borrar TODOOOOO esto y simplemente imprimir las instancias:



#   S   I   N       M   E   T   O   D   O       S   T   R:

print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(sorcerer.vocation,
       sorcerer.hit_points,
       sorcerer.mana,
       sorcerer.cast_spell(),
       sorcerer.movement_speed)) 


print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(knight.vocation,
       knight.hit_points,
       knight.mana,
       knight.cast_spell(),
       knight.movement_speed))


print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(druid.vocation,
       druid.hit_points,
       druid.mana,
       druid.cast_spell(),
       druid.movement_speed))


print("\nEl {} tiene: {} hit points y {} de mana, su hechizo es {} y {} de velocidad".
format(paladin.vocation,
       paladin.hit_points,
       paladin.mana,
       paladin.cast_spell(),
       paladin.movement_speed))


#   C   O   N       M   E   T   O   D   O       S   T   R       
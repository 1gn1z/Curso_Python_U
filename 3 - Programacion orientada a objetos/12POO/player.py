
"""class Player:
    #hit_points = 50
    #mana = 50
    #vocation = "No vocation"
    #hechizo = "Puff"            # Para que el jugador pueda lanzar hechizos debe ser hechicero, asi que "Puff" indica que no hizo nada xD

  def __init__(self):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo

    def lanzar_hechizo(self):
        return self.hechizo     # RETURN finaliza la funcion (método si esta dentro de una clase.)
        
    def __init__(self,**kwargs):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = "No vocation"
        self.spell = spell
""" 

class Player:
    vocation = "No vocation"            # Estos 3 atributos los definimos aqui en la clase padre por que si los definimos
    spell = "Puff"                      # en el metodo init saldrian exactamente como los definimos ahi en todas las instancias
    movement_speed = "50"               # Estos 3 se SOBREESCRIBEN en las clases del hechicero y del caballero.

    def __init__(self,**kwargs):        
        self.hit_points = kwargs.get("hit_points",50)   # Estos atributos los modificamos en la estancia creada via desempaquetamiento  
        self.mana = kwargs.get("mana", 50)              # de diccionario: sorcerer = player.Sorcerer(hit_points=40,mana=80)

    def cast_spell(self):
        return self.spell 

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Igne fulgur"
    movement_speed = "20"

class Knight(Player):
    vocation = "Knight"
    spell = "impetu"
    movement_speed = "60"

# Lo que pasa aqui es que los atributos de la clase Player van a ser heredados por las otras clases, pero al crear estas clases
# podemos SOBREESCRIBIR esos atributos.

# Con el metodo INIT estamos desempaquetando un diccionario, estos atributos se modifican en la estancia por los que queramos
# los demas atributos se sobreescriben xq los definimos en cada clase, ya sea la de Sorcerer o la de Knight

# Esto nos ayuda a tener clases especificas para cada vocacion, solamente teniendo que modificar la vida y el mana.
# Si solo tuvieramos la clase padre con todos los atributos, tendriamos que especificar todos los atributos a cada nuevo jugador:

sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",spell="Igne fulgur")  

# Asi, solo indicamos que esta heredando ademas de player, de la clase Sorcerer, unicamente teniendo que modificar la vida y el mana

sorcerer = player.Sorcerer(hit_points=40,mana=80)

# Los atributos "vocation" y "spell", ya estan definidos para todas las instancias creadas que hereden de Sorcerer.
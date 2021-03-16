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
    movement_speed = "20"

# Vamos a crear al Knight tambien:

class Knight(Player):
    vocation = "Knight"
    spell = "impetu"
    movement_speed = "60"


# Aqui decimos que sorcerer es una instancia que hereda de la clase player, que se escribe en minuscula por que esta
# importando la clase del mismo nombre (Player), pero del archivo "player.py". 
# Y que la nueva instancia hereda, ademas de los atributos de "Player", tambien los atributos de la clase "Sorcerer"

                    #   nueva_instancia = clase_padre(o archivo de importacion).Nueva_instancia()

sorcerer = player.Sorcerer("""spell="Igne Fulgur""",hit_points=40,mana=80) # Quitamos el spell xq ya esta denifido en la
                                                # instancia Sorcerer. solo modificamos la vida y la mana

print("\nEl Sorcerer tiene:\n")
print(Sorcerer.vocation)
print(Sorcerer.spell)
print(Sorcerer.movement_speed)
print(Sorcerer.mana)
print(Sorcerer.hit_points)


 #   C   L   A   S   E   S       S   O   L   A   S       S   I   N       METODO          __i    n   i   t__

# Estos atributos seran los datos POR DEFECTO DE LA CLASE PLAYER. Podemos modificarlos como vemos abajo

class Player:
    vida = 50                       # Se especifican los atributos directamente en la clase.
    mana = 50                       # estos atributos se aplican en todas las instancias creadas a partir de esta clase
    vocacion = "No vocation"        # Pero se pueden modificar como vemos abajo (lineas 24 - 27)
    hechizo = "Puff"

print("\nValores por defecto del personaje igual por defecto\n")
print("\nEl Player tiene:\n")
print(Player.vida)
print(Player.mana)
print(Player.vocacion)
print(Player.hechizo)

# Ahora bien, podemos MODIFICAR los atributos de una nueva instancia: Simplemente reasignamos los atributos
# de esa instancia. 

knight = Player()                    # Nueva instancia de la clase Player. Si no se especifican de otro modo 
                                     # toma los valores por defecto de la clase player

knight.vida = 80                     # MODIFICACION DE LOS ATRIBUTOS para esta instancia (knight)
knight.mana = 20
knight.vocacion = "Knight"                  
knight.hechizo = "Hechizo del caballero"

print("\nEl Knight tiene:\n")        # Simplemente imprimimos la instancia del knight ya con sus datos modificados   
print(knight.vida)
print(knight.mana)
print(knight.vocacion)
print(knight.hechizo) 








# C    L    A   S   E   S       C   O   N       M   E   T   O   D   O       __  I   N   I   T   __

# En lugar de poner los atributos directo en la clase:

# Vamos a especificarlos EN EL METODO INIT
# 
class Player:
    #hit_points = 50                        # Ya declarados los atributos en el metodo init, podemos borrar los atributos
    #mana = 50                              # que teniamos originalmente en la clase.
    #vocation = "No vocation"               # Estos atributos ahora estan como parametros en el metodo init.
    #hechizo = "Puff"            

    def __init__(self,hit_points,mana,vocation,hechizo):    # Atributos definidos dentro del metodo INIT
        self.hit_points = hit_points                        # Simplemente le damos el mismo valor de nombre y valor
        self.mana = mana                                    # Pero agregamos antes SELF. para que la instancia los tome
        self.vocation = vocation
        self.hechizo = hechizo 

# Estos atributos denifidos en el metodo init SE LOS VAMOS A PASAR A LA INSTANCIA, y PODEMOS MODIFICARLOS COMO QUERMAMOS

knight = Player(80,20,"Knight","Hechizo del caballero")     # Aqui reemplazamos los datos, SOLO PONIENDO SU VALOR
# Haciendo esto ya nos ahorramos el trabajo de asignar uno a uno los datos en la clase player. (Como en las lineas 43 - 46)

# Simplemente imprimimos igual los atributos de nuestra instancia

print("\nEl knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.hechizo)

# Tambien podemos asignar valores por defecto en el metodo INIT

    def __init__(self,hit_points=0,mana=0,vocation="None",hechizo="Puff"):

# Como vemos, lo que estamos haciendo es ASIGNARLES UN VALOR A LOS ATRIBUTOS, ya despues en la instancia creada
# podemos reasignarlos en las instancias:

sorcerer = Player(40,80,"sorcerer","Igne fulgur")   # Reasignacion.

# Ahora si NO MODIFICAMOS O NO ESCRIBIMOS ESE DATO TOMA EL DATO POR DEFECTO definido en el metodo INIT

# Asi que podemos asignarle al metodo INIT los atributos por defecto que queramos.
#
# Y tambien podemos MODIFICAR esos atributos en cualquier instancia, simplemente poniendo los valores
#  en la creacion de la instancia (linea 196)  








#D   E   S   E  M  P   A   Q   U   E   T   A   M   I   E   N   T   O       D   E       D   I   C   C   I   O   N   A   R   I   O   S

# Dentro de el metodo INIT, despues de self, vamos a poner dos asteriscos seguido de la palabra kwargs

          # def __init__(self,**kwargs):          

# Ahora, para especificar los atributos, escribimos SELF.ATRIBUTO = kwargs.get()
# y dentro de los parentesis, definimos los datos, como es un diccionario,
# LAS LLAVES VAN CON COMILLAS, SEGUIDO DE COMA, Y FINALMENTE EL VALOR. Por ejemplo: 

             self.hit_points = kwargs.get("hit_points",50)       

class Player:

    def __init__(self,**kwargs):    # Ponemos SELF, coma, y doble asterisco kwargs: self,*kwargs
        self.hit_points = kwargs.get("hit_points",50)   # EN INIT SI SE PONEN LAS COMILLAS EN EL DICCIONARIO
        self.mana = kwargs.get("mana", 50)              # self.atributo = kwargs.get("atributo",valor)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo","Puff")


# Ahora, en lugar de modificar los atributos dentro de la instancia, podemos ahora MODIFICAR LOS DATOS
# PERO PONIENDO LA LLAVE Y EL VALOR, xq recordemos que este metodo es DESEMPAQUETAMIENTO DE DICCIONARIO.

# Haciendo esto, es mas claro por que la llave indica que atributo es, seguido del valor de esa llave:

# Como vemos, se especifica SIN COMILLAS EL ATRIBUTO (la llave), SIGNO DE IGUAL, Y EL VALOR DEL ATRIBUTO (llave)
# SEPARADOS POR COMAS

knight = Player(mana=20,hit_points=80,vocation="Knight",hechizo="Hechizo del caballero")

print("\nEl Knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.hechizo)  

# Ademas de saber a que atributo pertenece cual valor, tenemos la ventaja ademas:
# PODEMOS PONER LOS ATRIBUTOS EN CUALQUIER ORDEN.
# No obligatoriamente en orden si los ponemos directamente en el metodo INIT

    def __init__(self,hit_points,mana,vocation,hechizo):    # SIN KWARGS, solo podemos definir los atributos SIN VALOR    
        self.hit_points = hit_points                        # Y tenemos que definir uno por uno los atributos
        self.mana = mana                                   
        self.vocation = vocation
        self.hechizo = hechizo 

knight = Player(80,20,"Knight","Hechizo del caballero")     # Loa valores se definen SOLOS, y CON KWARGS, no tenemos que recordar
                                                            # cual valor pertecene a que atributo


# Con kwargs, ya podemos definir los atributos (llaves del dict) y los valores de las mismas directo desde la instancia

knight = Player(mana=20,hit_points=80,vocation="Knight",hechizo="Hechizo del caballero")

# ADEMAS TAMBIEN PODEMOS MODIFICAR LOS DATOS DE OTRAS INSTANCIAS SIN PROBLEMAS:

sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",hechizo="Igne fulgur")
paladin = Player(hit_points=60,mana=40,vocation="Paladín",hechizo="Fortis magica")
druid = Player(hit_points=50,mana=80,vocation="Druida",hechizo="Anima mea")  






#                        H       E       R       E       N       C       I       A       S

# Con el sistema de HERENCIAS, podemos usar TODOS LOS ATRIBUTOS DE UNA CLASE EN OTRA DIFERENTE.

# Simplemente ESPECIFICAMOS QUE UNA CLASE HEREDA DE OTRA, ASI:

class Player:                       ### Atributos por defecto del player
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "20"
    #mana = 50                      # Si especificamos aqui los atributos del init funciona igual

    def __init__(self,**kwargs):   # Aqui podriamos poner los datos directo en la clase padre player y funciona igual.
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

class Sorcerer(Player):             ### En la clase que hereda podemos modificar los datos por defecto de la clase Player
    vocation = "Sorcerer"
    spell = "Igne fulgur"
    movement_speed = "50"

    hit_points = "80"               # Igualmente, podemos modificar los atributos del metodo INIT

# Aqui, al crear una instancia nueva ("Sorcerer"), HEREDA TODOS LOS ATRIBUTOS DE LA CLASE PLAYER.
# 
# 
print(Sorcerer.vocation)              

# Vamos a practicar creando el knight y el paladin.

class Knight(Player):
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"




















#
# Ahora definiremos otro método para nuestra clase, el método __init__

# Este método es especial por que es un método que TIENEN TODAS LAS CLASES en python.

# Se usa para definir el comportamiento cuando se crea una instancia de nuestra clase.
# Aqui podemos decir que pasara con los valores de los atributos, si queremos que un atributo sea la entrada del usuario, etc.

# __init__ Es el CONSTRUCTOR de python, para construir objetos de una clase, INIT viene de INITIALIZE, (inicializar)


# Con el método init podemos ESPECIFICAR los atributos de las instancias, pasandoselos como atributos dentro del método
# de este modo, al crear una instancia, simplemente podemos agregarle los atributos que queramos:

# MAIN Y PLAYER:

#                                   P       L       A       Y       E       R
class Player:
    hit_points = 50
    mana = 50
    vocation = "No vocation"
    hechizo = "Puff"            

    def lanzar_hechizo(self):
        return self.hechizo  

#                                            M       A       I       N        

from player import Player

print("\nEl player tiene:\n")
print(Player.hit_points)
print(Player.mana)
print(Player.vocation)

sorcerer = Player()

sorcerer.hit_points = 40
sorcerer.mana = 80
sorcerer.vocation = "sorcerer"
sorcerer.hechizo = "Igne fulgur"

print("\nEl sorcerer tiene:\n")

print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = Player()

knight.hit_points = 80
knight.mana = 20
knight.vocation = "knight"
knight.hechizo = "Impetu"

print("\nEl knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

# En lugar de poner todas las variables en la clase, podemos hacerlo con el método INIT:

class Player:
    #hit_points = 50                        # Ya declarados los atributos en el metodo init, podemos borrarlos atributos
    #mana = 50                              # que teniamos originalmente en la clase.
    #vocation = "No vocation"               # Estos atributos ahora estan como parametros en el metodo init.
    #hechizo = "Puff"            

    def __init__(self,hit_points,mana,vocation,hechizo):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo    

    def lanzar_hechizo(self):
        return self.hechizo  


# Como vemos, usando el metodo init, podemos poner los atributos directamente en el metodo init.

# PERO! tenemos que especificar que estos atributos pertenecen a self, que sera reemplazado por todas las instancias donde los llamemos

# Gracias al metodo INIT, cuando creamos una instancia en nuestra clase (en este caso Player), podemos poner los datos.


#print("\nEl player tiene:\n")
#print(Player.hit_points)       Ya podemos borrar al jugador, al crear una instancia nueva, como ya definimos el metodo INIT (linea 71)
#print(Player.mana)             Ya no es necesario esto, xq la nueva instancia tendra los valores por defecto en el INIT
#print(Player.vocation)         (Ya la clase Player tiene sus atributos definidos en el metodo init) Lineas 65 -

sorcerer = Player(40,80,"sorcerer","Igne fulgur")   # Ponemos los datos en orden, separados por comas uno de otro.


#print("\nEl player tiene:\n")
#print(Player.hit_points)
#print(Player.mana)
#print(Player.vocation)

sorcerer = Player(40,80,"sorcerer","Igne fulgur")   # Haciendo esto, ya podemos borrar las declaraciones de abajo (lineas 105 - 108)
                                                    # Por que ya especificamos los atributos en el metodo INIT
                                                    # Y entre los parentesis les damos los valores a los atributos de
                                                    # de los parentesis del metodo init de la clase Player.                            
#sorcerer.hit_points = 40
#sorcerer.mana = 80
#sorcerer.vocation = "sorcerer"
#sorcerer.hechizo = "Igne fulgur"

print("\nEl sorcerer tiene:\n")

print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = Player(80,20,"knight","Impetu")            # Aqui igual podemos borrar las asignaciones de abajo por que ya estan
                                                    # espeficidos los atributos en el metodo init 
                                                    # y a la hora de crear la instancia los atributos ya estan asignados aqui.
                                                    # Lineas 121-124
#knight.hit_points = 80
#knight.mana = 20
#knight.vocation = "knight"
#knight.hechizo = "Impetu"

print("\nEl knight tiene:\n")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

# Es necesario espeficiar TODOS los argumentos que hayamos declarado, si no nos mandara un erorr:

# Si a una instancia le falta un atributo, por ejemplo el sorcerer no tiene especificado el hechizo:

sorcerer = Player(40,80,"sorcerer","Igne fulgur")

# Mandara el siguiente error:
TypeError: __init__() missing 1 required positional argument: 'hechizo'

# Esto nos dice que falta un argumento posicional requerido llamado "hechizo".
# En otras palabras dice que nosotros en nuestro INIT, obligatoriamente requerimos 4 argumentos (hit_points,mana,vocation,hechizo)
# Pero solo pasamos 3, por eso manda error:

# Para generar VALORES POR DEFECTO, como en los atributos, lo que hacemos es poner los valores por defecto 
# DENTRO DEL METODO INIT, asi:

    def __init__(self,hit_points=0,mana=0,vocation="None",hechizo="Puff"):

# Como vemos, lo que estamos haciendo es ASIGNARLES UN VALOR A LOS ATRIBUTOS, ya despues en la instancia creada
# podemos reasignarlos en las instancias:

sorcerer = Player(40,80,"sorcerer","Igne fulgur")   # Reasignacion.

# Ahora, si les asignamos un valor por defecto a los atributos desde el init, y NO lo asignamos en la instancia
# TOMARA EL VALOR POR DEFECTO asignado en el init:

    def __init__(self,hit_points,mana,vocation,hechizo="Puff"):

    sorcerer = Player(40,80,"sorcerer" """Cuarto atributo NO especificado""")

    print(sorcerer.hit_points)
    print(sorcerer.mana)
    print(sorcerer.vocation)
    print(sorcerer.lanzar_hechizo())

# Devuelve:

El sorcerer tiene:

40
80
sorcerer
Puff

# SI EL METODO INIT TIENE ESPECIFICADO UN VALOR POR DEFECTO Y NO SE ESPECIFICA EN LA INSTANCIA OTRO VALOR, TOMA EL VALOR POR DEFECTO:

class Player:
  
    def __init__(self,hit_points=0,mana=0,vocation="None",hechizo="Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo

    def lanzar_hechizo(self):
        return self.hechizo 

sorcerer = Player() # Aqui NO especificamos los atributos para que tome los que trae por defecto del metodo INIT
print()
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.hechizo)    # Si llamamos al atributo "hechizo", en lugar del metodo "lanzar_hechizo", devuelve el valor de hechizo por defecto

knight = Player(80,20,"knight","Impetu")    # Aqui estan especificados los ATRIBUTOS MODIFICADOS para esta instancia en particular
print()
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

# ESTO DEVUELVE:


0
0
None
Puff

80
20
knight
Impetu

# Asi que podemos asignarle al metodo INIT los atributos por defecto que queramos.
#
# Y tambien podemos MODIFICAR esos atributos en cualquier instancia, simplemente poniendo los valores en la creacion de la instancia (linea 196)
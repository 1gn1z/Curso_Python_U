# Ya tenemos atributos en nuestra clase, pero queremos tambien funciones que pueda hacer un jugador

# Nuestro sorcerer debe ser capaz de lanzar hechizos, asi que definamos una funcion en nuestra clase.

# Recordemos que una funcion dentro de una clase se llama MÉTODO
# Representa lo mismo que una funcion tal cual, pero como esta dentro de una clase pues se llama método.

# Para definir un método de una clase lo hacemos igual que una funcion, con la palabra reservada DEF, y el nombre del método
# Con parentesis y 2 puntos:

def lanzar_hechizo(self):

# TODOS los métodos en python TOMAN POR LO MENOS UN ARGUMENTO. Ese argumento se llama SELF
# SELF se usa para referirse a la instancia(objeto) de esa clase, este self va a tomar la instancia del sorcerer, o del knight,
# o de la instancia que queramos

# SELF se refiere al objeto instanciado, al objeto que usamos para llamar al metodo (en este caso sorcerer, knight, etc.)

# El SELF es como un identificador para que aplique el metodo a la instancia que le digamos. (creo)

def lanzar_hechizo(self):
    return self.hechizo

# El metodo se tiene que llamar necesariamente desde la INSTANCIA, (Objeto: sorcerer, knight, etc.) por eso al crear el método, pide
# el argumento SELF, NO es una palabra reservada, hace referencia al objeto en instancia pero se pueden usar otras variables.

# SELF se refiere al objeto (instancia) que usamos para llamar a ese método

class Player:
    hit_points = 50
    mana = 50
    vocation = "No vocation"
    hechizo = "Puff"

    def lanzar_hechizo(self):       #SELF
        return self.hechizo         #SELF

print(sorcerer.lanzar_hechizo())    #SELF se reemplaza por la instancia que queramos

# Es decir, cuando llamemos al método lo podemos hacer desde cualquier instancia, SELF se reemplaza por el objeto instanciado de esa clase
sorcerer = Player()

sorcerer.hit_points = 40
sorcerer.mana = 80
sorcerer.vocation = "sorcerer"









class Player:                       # CLASE
    hit_points = 50
    mana = 50
    vocation = "No vocation"
    hechizo = "Puff"

    def lanzar_hechizo(self):       # SELF es el objeto usado para invocar el método
        return self.hechizo         # SELF es usado dentro del metodo para modificar los atributos del objeto como queramos


sorcerer = Player()                 # Creacion de una instancia a partir de una clase previamente hecha

sorcerer.hit_points = 40            #
sorcerer.mana = 80                  # Modificacion de los atributos de esa instancia en particular
sorcerer.vocation = "sorcerer"      # sin afectar los atributos de la clase

print(sorcerer.lanzar_hechizo())    # Self referencia a la instancia, (sorcerer) para que se invoquen los métodos a esa instancia



# SELF necesita que el método se llame desde una instancia.
# SELF lo que hace es invocar al metodo desde la instancia que queramos/necesitemos
# SELF AUTOREFERENCIA a la clase a la que pertenece
# al hacer self.variable, invoca en la instancia donde lo pongamos el valor de esa variable


#SELF tambien sirve para llamar funciones ya declaradas desde otra funcion diferente:

# Aqui vemos como funciona el sistema de HERENCIA
# en una nueva instancia de la clase "Tortugas", si llamamos a cualquier funcion desde ella, sera invocada

# Por las herencias, donatello puede acceder a todas las funciones que tenemos, ya que la CLASE TORTUGAS HEREDA las funciones
# de la CLASE REPTILES, y esta CLASE REPTILES HEREDA todas las funciones de la clase padre: CLASE ANIMALES.

class Animales():
    def moverse(self):
        print("moviéndose")
    def comer(self):
        print("comiendo")

class Reptiles(Animales):
    def sangre_fria(self):
        print("tienen sangre fría")

class Tortugas(Reptiles):
    def ponen_huevos(self):
        print("poniendo huevos")

donatello = Tortugas()      # Creacion de una instancia de la clase tortugas.


donatello.moverse()

# Aqui, como vemos, deuelve esto:

moviéndose

# Lo que significa que estamos llamando a la funcion "moverse", desde una instancia creada de otra clase.
# PERO! esa clase trae HEREDADAS todas las funciones que tenemos, ya que la CLASE TORTUGAS HEREDA TODAS LAS FUNCIONES
# DE LA CLASE REPTILES, y LA CLASE REPTILES HEREDA TODAS LAS FUNCIONES DE LA CLASE ANIMALES.

# Gracias a SELF podemos llamar a las funciones desde cualquier instancia :) SELF reemplaza la instancia.

# SELF sirve para llamar, dentro de una funcion, SUSTITUIR el nombre de la instancia, y poder llamar otras funciones
# de otras clases (de otras clases heredadas), dentro de ella, por ejemplo, crearemos una funcion de "encontrar comida".
# y esa funcion llamara a una funcion QUE YA EXISTE "comer".

# La funcion "encontrar_comida" hara que la tortuga se mueva, busque comida y que cuando encuentre la comida que se la coma.

# Para esto necesitamos 3 funciones, PERO! 2 funciones ya estan declaradas (moverse y comer) y el objeto tortuga (donatello)
# puede acceder a ellas xq ya las tiene gracias al sistema de herencias.

# Aqui entra en juego SELF, en lugar de usar la instancia (objeto), en la funcion, usamos SELF, para no tener que escribir miles 
# funciones por cada instancia que tengamos.

# PRIMERO. La primera funcion es un metodo ya existente, "moverse:" 

# Vamos a crear la nueva funcion "encontrar comida". asi que la llamamos desde la nueva funcion:


class Animales():
    def moverse(self):
        print("moviéndose")
    def comer(self):
        print("comiendo")

class Reptiles(Animales):
    def sangre_fria(self):
        print("tienen sangre fría")

class Tortugas(Reptiles):
    def ponen_huevos(self):
        print("poniendo huevos")

    def encontrar_comida(self):
        self.moverse()                # PRIMERO
        print("Encontré comida!")     # SEGUNDO
        

donatello = Tortugas()      

# Cuando llamemos a la funcion "encontrar_comida"m se llamara tambien a la funcion "moverse"

# SEGUNDO. Como la funcion "encontrar_comida" no tiene mas codigo, simplemente ponemos un print que duga "encontre comida!"

# TERCERO. una vez encontrada la comida procede a comerla, para esto SI tenemos una funcion, asi que simplemente
# la invocamos con SELF.

# Ahora, si llamamos a la funcion "encontrar_comida", desde una iteracion (de la clase tortugas, que es donde esta
# definida la funcion), se ejecuta sin problemas :)
# 

# SIGO AQUI CON LOS VIDEOS DEL CURSO.

def lanzar_hechizo(self):
        return self.hechizo         

class Player:
    hit_points = 50
    mana = 50
    vocation = "No vocation"
    hechizo = "Puff"            # Para que el jugador pueda lanzar hechizos debe ser hechicero, asi que "Puff" indica que no hizo nada xD

    def lanzar_hechizo(self):
        return self.hechizo     # RETURN finaliza la funcion (método si esta dentro de una clase.)
                                # RETURN termina la funcion. Es como un BREAK en los ciclos.
        
# Recordar que al llamar los a los métodos, se tienen que poner los parentesis al final, exactamente igual que las funciones.

print(sorcerer.lanzar_hechizo())

# Ahora vamos a lanzar el hechizo desde nuestro knight:

print(knight.lanzar_hechizo())

#  En este momento, ambos hacen "Puff", xq no hemos modificado el atributo del hechizo.
# Vamos a modificar el atributo del sorcerer, para esto tenemos que modificar LA VARIABLE HECHIZO, NO LA FUNCION LANZAR_HECHIZO ok.

sorcerer = Player()

sorcerer.hit_points = 40
sorcerer.mana = 80
sorcerer.vocation = "sorcerer"
sorcerer.hechizo = "Relampago de fuego!"    # Modificacion del atributo hechizo, pero solo del sorcerer.

print("\nEl sorcerer tiene:\n")

print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

El sorcerer tiene:

40
80
sorcerer
Ataque con hechizo!







































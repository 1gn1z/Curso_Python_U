#                                C                 O                 N                 J                 U                 N                 T                 O                 S                         I



# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())        # La funcion SET creara un conjunto a partir de nuestro input.
print(conjunto_a)

# Al hacerlo asi, nos devuelve el conjunto ADEMAS DE UN ESPACIO. Esto lo hace por que en python las cadenas son
# iterables, es decir, el conjunto recorre cada uno de los caracteres de la cadena.
# como el input que escribimos nos dice que separemos los elementos con un espacio por eso devuelve tambien ese espacio
# y como recordamos, cuando hay varios elementos distintos, el conjunto los unifica. (no puede haber elementos iguales)
# por eso, aunq nosotros escribimos varios espacios que separan los elementos, el set devuelve solo uno.

# NO podemos borrar ese espacio, los conjuntos no son mutables, tiene que quedar como los pusimos desde un inicio

# Podemos usar alguna FUNCION DEL OBJETO CADENA, que sirva para separar los elementos y ya enviarla al set.

# Si no sabemos, podemos pedir ayuda en la consola de python typeando "help(str)"
# Al hacerlo veremos muchas funciones y atributos de la clase cadena, la que buscamos es SPLIT.

#split(self, /, sep=None, maxsplit=-1)
# |            Return a list of the words in the string, using sep as 
#the delimiter string.

# Como vemos, nos dice que devuelve una lista de las palabras en string, en la cadena, usando el
# SEPARADOR COMO DELIMITADOR DE LA CADENA, justo lo que necesitamos :)

# Podemos usar distintos delimitadores, pero si no se especifica EL ESPACIO VACIO ES EL DELIMITADOR POR DEFECTO.

# Entonces nuestra variable de conjunto_a quedaria asi:

conjunto_a = set(input("Conjunto A: ").split())

# Podemos hacer un ejemplo desde la consola:

> "Kevor sera haker pronto :)".split()
['Kevor', 'sera', 'haker', 'pronto', ':)']

# Como vemos, devuelve una lista que contiene cada palabra como elemento de la lista.
# Por defecto, si no ponemos ningun argumento como separador o maximo de rebanadas toma el espacio 
# como delimitador por default.

# Como estamo trabajando con sets, podemos separar los elementos con comas, y especificar el separador, que sea coma:

> "Kevor,sera,hacker,pronto,:)".split(",")
['Kevor', 'sera', 'hacker', 'pronto', ':)']

# Haciendo esto se soluciona nuestro problema, ya que la funcion split toma por si misma el espacio. 
# lo escribe el usuario pero la funcion split lo convierte en lista añadiendo ella misma el espacio

# Ya resulto declaremos el conjunto B

conjunto_b = set(input("Conjunto B: ").split())

# Ya tenemos nuestros conjuntos listos para ser usados :3

#                                C                 O                 N                 J                 U                 N                 T                 O                 S                         II

# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

def ver_instrucciones():
        print("Operaciones que puedes hacer: ")
        print("1.- Union")
        print("2.- Intersección")
        print("3.- Diferencia")
        print("4.- Diferencia simétrica")
        print("5.- Ver instrucciones")
        print("6.- Salir")

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())


ver_instrucciones()
while True:
        operacion = int(input(": "))
        if operacion == 1:
                print("Unión")
        elif operacion == 2:
                print("Intersección")
        elif operacion == 3:
                print("Diferencia")
        elif operacion == 4:
                print("Diferencia Simétrica")
        elif operacion == 5:
                ver_instrucciones()
        elif operacion == 6:
                break
        else:
                print("Operación inválida, favor de verificar")


#       C       O       N       J       U       N       T       O       S              III           Y          IV

# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())

conjunto_b = set(input("Conjunto B: ").split())

# Haciendo los prints asi, despues del while true, nos evitamos tener que mostrar siempre las operaciones despues de ingresar
# los conjuntos, de este modo se muestran antes de introducir los conjuntos.

print("Operaciones que puedes hacer: ")
print("1.- Union")
print("2.- Intersección")
print("3.- Diferencia")
print("4.- Diferencia simétrica")
print("5.- Ver instrucciones")
print("6.- Salir")

"""
while True:
        operacion = int(input(": "))
        if operacion == 1:
                print("La unión de los conjuntos es: ",conjunto_a | conjunto_b)
        elif operacion == 2:
                print("La intersección de los conjuntos es: ",conjunto_a & conjunto_b)
        elif operacion == 3:
                print("La diferencia de los conjuntos es: "conjunto_a - conjunto_b)
        elif operacion == 4:
                print("La diferencia simétrica de los conjuntos es: ",conjunto_a.symmetric_difference(conjunto_b))
        elif operacion == 5:
                print("Operaciones que puedes hacer: ")
                print("1.- Union")
                print("2.- Intersección")
                print("3.- Diferencia")
                print("4.- Diferencia simétrica")
                print("5.- Ver instrucciones")
                print("6.- Salir")
        else:
                break

"""

# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

"""
print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())
"""

# Haciendo los prints asi, despues del while true, nos evitamos tener que mostrar siempre las operaciones despues de ingresar
# los conjuntos, de este modo se muestran antes de introducir los conjuntos.

def ver_instrucciones():
        print("Operaciones que puedes hacer: ")
        print("1.- Union")
        print("2.- Intersección")
        print("3.- Diferencia")
        print("4.- Diferencia simétrica")
        print("5.- Ver instrucciones")
        print("6.- Salir")

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())

ver_instrucciones()         # Antes de entrar al while true debemos mostrar las instrucciones.
while True:
        operacion = int(input(": "))
        if operacion == 1:
                print("Unión")
        elif operacion == 2:
                print("Intersección")
        elif operacion == 3:
                print("Diferencia")
        elif operacion == 4:
                print("Diferencia Simétrica")
        elif operacion == 5:
                ver_instrucciones()
        elif operacion == 6:
                break
        else:
                print("Operación inválida, favor de verificar")

# Podemos hacer la funcion de ver instrucciones simplemente agregando todos los prints de las instrucciones en una funcion.

# La bienvenida la ponemos abajo de nuestra funcion ver_instrucciones

# Ahora, si el usuario pone 5 para ver las instrucciones simplemente llamamos a la funcion.

# Ahora vamos a hacer una funcion con todo el código de la calculadora de conjuntos:

# Definimos una funcion para la UNION DE CONJUNTOS, y lo haremos con la funcion llamada UNION
def union_conjuntos(conjunto_a, conjunto_b):
        #print()
        print("\nLa unión de A y B es:\n",conjunto_a | conjunto_b)
        #print()
# Como lo hacen en el curso con la funcion UNION:
#        print("LA unión de A y B es {}".format(conjunto_a.union(conjunto_b)))


# En el curso se usa la funcion union, pero me parece mas simple hacerlo con el equivalente pipe |
# print("La union de A y B es {}".format(conjunto_a.union(conjunto_b)))

# Vamos a borrar esos prints de la funcion union_conjuntos, simplemente usando la funcion \n, que es la funcion de salto de linea.
# La funcion de salto de linea VA DENTRO DE LAS COMILLAS DE LA CADENA ok :)

# Me le voy a adelantar al profe para ver si me sale bien la interseccion ;)
# LOGRADO :3
# Ya encarrerado le voy a seguir con las demas :)

#                T         O         D         O         S                    L         O         G         R         A         D         O         S

def interseccion_conjuntos(conjunto_a,conjunto_b):
        print("\nLa interseccion de A y B es:\n", conjunto_a & conjunto_b)
# Como lo hacen en el curso con la funcion UNION:
#        print("LA unión de A y B es {}".format(conjunto_a.intersection(conjunto_b)))

def diferencia_conjuntos(conjunto_b,conjunto_b):
        print("\nLa diferencia de A y B es\n", conjunto_a - conjunto_b)

def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
        print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
        print("Operaciones que puedes hacer: ")
        print("1.- Union")
        print("2.- Intersección")
        print("3.- Diferencia")
        print("4.- Diferencia simétrica")
        print("5.- Ver instrucciones")
        print("6.- Salir")


def calculadora_conjuntos():                # Funcion con todo el código hasta ahora.
        print("Bienvenido a los Conjuntos")
        print("Introduce los elementos de los conjuntos separados por espacios")
        print("Ejemplo: 1 3 5 8 0 2")

        conjunto_a = set(input("Conjunto A: ").split())
        conjunto_b = set(input("Conjunto B: ").split())

        ver_instrucciones()

        while True:
                operacion = int(input(": "))
                if operacion == 1:
                        union_conjuntos(conjunto_a, conjunto_b)
                elif operacion == 2:
                        interseccion_conjuntos(conjunto_b,conjunto_b)
                elif operacion == 3:
                        diferencia_conjuntos(conjunto_a, conjunto_b)
                elif operacion == 4:
                        diferencia_simetrica_conjuntos(conjunto_a, conjunto_b)
                elif operacion == 5:
                        ver_instrucciones()
                elif operacion == 6:
                        break
                else:
                        print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# Ahora vamos a hacer la UNION, para esto vamos a definir UNA FUNCION QUE ACEPTARA 2 PARAMETROS:
# Esta funcion quedara en la opcion 1 de nuestro ciclo while

# DIFERENCIA. La diferencia simetrica, la union y la interseccion SON CONMUTATIVAS, EL ORDEN DE LOS FACTORES NO ALTERA EL PRODUCTO.

# En la diferencia es distinto, NO ES LO MISMO TENER 4-1 que 1-4, es decir,
#
# NO ES LO MISMO CONJUNTO A - CONJUNTO B que CONJUNTO B - CONJUNTO A.

# En este caso, debemos darle al usuario la opcion de elegir cual conjunto se restara de cual.


#print("Cual conjunto deseas restar del otro?")
def diferencia_conjuntos(conjunto_a,conjunto_b):
        print("Elige la diferencia a realizar:")
opcion_1 = int(input(("1.- A - B"))
opcion_2 = int(input(("2.- B - A"))
operacion = int(input(": "))
if operacion == 1:
        print("\nLa diferencia de A - B es {}\n".format(conjunto_a.difference(conjunto_b)))
elif operacion == 2:
        print("\nLa diferencia de B - A es {}\n".format(conjunto_b.difference(conjunto_a)))
else:
        print("Opción incorrecta, favor de verificar")
        diferencia_conjuntos(conjunto_a,conjunto_b)                         # Si salta el error del else, le damos al usuario la opcion de elegir de nuevo
                                                                                                                                                                                                                # asi que llamamos de nuevo a la funcion para que reinicie :)
# LLAVES DE FORMAT ANTES DE SALTO DE LINEA!!!





#                                C                 O                 N                 J                 U                 N                 T                 O                 S                         V



def union_conjuntos(conjunto_a,conjunto_b):
        print("\nLa unión de A y B es\n{}".format(conjunto_a.union(conjunto_b)))

def interseccion_conjuntos(conjunto_a,conjunto_b):
    print("\nLa intersección de A y B es\n{}".format(conjunto_a.intersection(conjunto_b)))


def diferencia_conjuntos(conjunto_a,conjunto_b):
    print("Elige la operación:")
    print("1.- A - B")
    print("2.- B - A")
    try:                                                                                                                                                                                # Manejo de errores. LISTO :) 
        operacion = int(input(": "))
    except ValueError:
        print("Debes introducir 1 o 2")
        diferencia_conjuntos(conjunto_a, conjunto_b)        # Volvemos a llamar la funcion para que se reinicie si el usuario no eligio 1 o 2
    else:
        if operacion == 1:
            print("\nLa diferencia de A - B es{}\n".format(conjunto_a.difference(conjunto_b)))
        elif operacion == 2:
            print("\nLa diferencia de B - A es{}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print("Operación inválida, favor de verificar")
            diferencia_conjuntos(conjunto_a, conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
        print("Operaciones que puedes realizar: ")
        print("1.- Union")
        print("2.- Intersección")
        print("3.- Diferencia")
        print("4.- Diferencia simétrica")
        print("5.- Ver instrucciones")
        print("6.- Salir")

def despedida():
        print("\nGracias por usar la calculadora de conjuntos!")
        print("\n Vuelve pronto :)")


def calculadora_conjuntos():
        print("Bienvenido a los Conjuntos")
        print("Introduce los elementos de los conjuntos separados por espacios")
        print("Ejemplo: 1 3 5 8 0 2")

        conjunto_a = set(input("Conjunto A: ").split())
        conjunto_b = set(input("Conjunto B: ").split())

        ver_instrucciones()

        while True:
                try:                                                                                                                                                                                                                # Manejo de errores. LISTO :) 
                        operacion = int(input("Operación a realizar: "))
                except ValueError:
                        print("Operación incorrecta, favor de verificar")
                else:
                        if operacion == 1:
                                union_conjuntos(conjunto_a,conjunto_b)
                        elif operacion == 2:
                                interseccion_conjuntos(conjunto_a,conjunto_b)
                        elif operacion == 3:
                                diferencia_conjuntos(conjunto_a,conjunto_b)
                        elif operacion == 4:
                                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
                        elif operacion == 5:
                                ver_instrucciones()
                        elif operacion == 6:
                                despedida()
                                break
                        else:
                                print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# La ultima cosa que haremos sera darle un mensaje al usuario cuando salga de la aplicacion.


#       C       O       N       J       U       N       T       O       S               V

def union_conjuntos(conjunto_a,conjunto_b):
    print("\nLa unión de A y B es\n{}".format(conjunto_a.union(conjunto_b)))

def interseccion_conjuntos(conjunto_a,conjunto_b):
    print("\nLa intersección de A y B es\n{}".format(conjunto_a.intersection(conjunto_b)))

def diferencia_conjuntos(conjunto_a,conjunto_b):
    print("Elige la operación:")
    print("1.- A - B")
    print("2.- B - A")
    try:                                                                                                                                                                                # Manejo de errores. LISTO :) 
        operacion = int(input(": "))
    except ValueError:
        print("Debes introducir 1 o 2")
        diferencia_conjuntos(conjunto_a, conjunto_b)        # Volvemos a llamar la funcion para que se reinicie si el usuario no eligio 1 o 2
    else:
        if operacion == 1:
            print("\nLa diferencia de A - B es{}\n".format(conjunto_a.difference(conjunto_b)))
        elif operacion == 2:
            print("\nLa diferencia de B - A es{}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print("Operación inválida, favor de verificar")
            diferencia_conjuntos(conjunto_a, conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
    print("Operaciones que puedes realizar: ")
    print("1.- Union")
    print("2.- Intersección")
    print("3.- Diferencia")
    print("4.- Diferencia simétrica")
    print("5.- Ver instrucciones")
    print("6.- Insertar nuevos conjuntos")
    print("7.- Salir")

def despedida():
    print("\nGracias por usar la calculadora de conjuntos!")
    print("\nVuelve pronto :)")

#def insertar_nuevos_conjuntos(conjunto_a,conjunto_b):
#    calculadora_conjuntos()     # Lo logre por casualidad xD. Lo que pasa es que esta funcion inicia de nuevo el programa
                                # de nuevo, tomando los nuevos conjuntos introducidos y reemplazandolos :)
                                # hay un problema :(, si reemplazamos, al salir, pide la operacion a realizar, y hay que
                                # insertar 7 OTRA VEZ para que el programa termine :(
                               
#def insertar_nuevos_conjuntos(conjunto_a,conjunto_b):

def calculadora_conjuntos():
    print("Bienvenido a los Conjuntos")
    print("Introduce los elementos de los conjuntos separados por espacios")
    print("Ejemplo: 1 3 5 8 0 2")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())

    ver_instrucciones()

    while True:
        try:                                                                                                                                                                                                                # Manejo de errores. LISTO :) 
            operacion = int(input("Operación a realizar: "))
        except ValueError:
            print("Operación incorrecta, favor de verificar")
        else:
            if operacion == 1:
                union_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                calculadora_conjuntos() # Reiniciamos el programa llamando nuevamente la funcion principal. Que toma los nuevos conjuntos
                break                   # Con el break terminamos el programa, sin que se reinicie y tengamos que poner 2 veces 7 (salir)
            elif operacion == 7:
                despedida()
                break
            else:
                print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# La ultima cosa que haremos sera darle un mensaje al usuario cuando salga de la aplicacion.

# RETO!!!
# Tratar de crashear el programa.
# Puede que el usuario quiera poner otros conjuntos diferentes sin salir de la aplicacion.

# Poner una nueva operacion donde le digamos al usuario algo como "insertar nuevos conjuntos"
# El profe como que no explica bien xd, lo que entendi es que hay que poder REEMPLAZAR los conjuntos por unos nuevos para experimentar

# RETO LOGRADO!!! :)
# Simplemente volvemos a llamar la funcion principal que reinicia el programa y ponemos un break para que termine
# y no vuelva a pedir una vez mas la operacion antes de salir.


# Quien sabe que pedo, al hacer todas las operaciones que NO eran UNION (interseccion, diferencia y diferencia simetrica)
# me arrojaba simplemente "set()". NO mandaba error ni nada, simplemente imprimia eso.

# Lo corregi en el archivo "conjuntos_V(Reto_2).py".
# Lo que hice fue simplemente usar sus EQUIVALENTES en lugar del codigo ofuscado con .format bla bla bla, funciona bien :)

# UNION:                    conjunto_a | conjunto_b
# INTERSECCION:             conjunto_a & conjunto_b
# DIFERENCIA:               conjunto_a - conjunto_b o conjunto_b - conjunto:a
# DIFERENCIA SIMETRICA:     conjunto_a.symmetric_difference(conjunto_b)
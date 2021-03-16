# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())	# La funcion SET creara un conjunto a partir de nuestro input.
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
# |      Return a list of the words in the string, using sep as 
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

# Ya tenemos nuestros conjuntos listos para ser usados

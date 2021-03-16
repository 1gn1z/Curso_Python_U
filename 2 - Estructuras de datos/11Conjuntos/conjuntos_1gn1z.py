# Creacion de un conjunto
# Para crear un conjunto especificamos sus elementos entre llaves:

conjunto = {1, 2, 3, 4}

# Puede tener datos de diversos tipos:

conjunto01 = {True, 3.14, None, False, "Hola mundo", (1, 2)}

# PERO! un conjunto NO puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos.

"""
s = {[1, 2]}
Traceback (most recent call last):
      ...
TypeError: unhashable type: 'list'
"""

#Python distingue este tipo operación de la creación de un diccionario ya que no incluye dos puntos. 
#Sin embargo, no puede dirimir el siguiente caso:

s = {}

# Por defecto, la asignación anterior crea un diccionario.
# Para generar un conjunto vacío, directamente creamos una instancia de la clase set:

s = set()

# Tambien podemos obtener un conjunto a partir de cualquier objeto iterable:

>>> s1 = set([1, 2, 3, 4])
>>> s2 = set(range(10))

>>> s1

{1, 2, 3, 4}

>>> s2

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Un set puede ser convertido a una lista y viceversa. En este último caso, LOS ELEMENTOS DUPLICADOS SON UNIFICADOS

>>> list ({1, 2, 3, 4})

[1, 2, 3, 4]

>>> set([1, 2, 2, 3, 4])

{1, 2, 3, 4}

# Elementos

#Los conjuntos son objetos mutables. Vía los métodos ADD() y DISCARD() podemos añadir y remover 
#un elemento indicándolo como argumento. Tambien podemos usar el método REMOVE, pero si elemento a eliminar NO EXISTE
#arrojara un error, en cambio con el método DISCARD SI EL ELEMENTO NO EXISTE SIMPLEMENTE LO IGNORA, SIN ERRORES :) 

>>> s = {1, 2, 3, 4}

>>> s.add(5)

>>> s

{1, 2, 3, 4, 5}

>>> s.discard(2)

>>> s

{1, 3, 4, 5}


# Para determinar si un elemento pertenece a un conjunto, utilizamos la palabra reservada IN.

>>> 2 in {1, 2, 3}

True

>>> 4 in {1, 2, 3}

False


#La función CLEAR() elimina todos los elementos.

>>> s = {1, 2, 3, 4}
>>> s.clear()
>>> s
set()

#El método pop() retorna un elemento en forma aleatoria (no podría ser de otra manera ya que los elementos no están ordenados). 
#Así, el siguiente bucle imprime y remueve uno por uno los miembros de un conjunto.

>>> s = {1, 2, 3, 4, 5}
>>> while s:
	print(s.pop())

1
2
3
4
5
>>> s
set()

#remove() y pop() lanzan la excepción KeyError cuando un elemento no se encuentra en el conjunto o bien éste está vacío, 
#respectivamente.

#Para obtener el número de elementos aplicamos la ya conocida función LEN():

>>> len({1, 2, 3, 4})
4

#    O    P    E    R    A    D    O    R    E    S        P    R    I    N    C    I    P    A    L    E    S

#Algunas de las propiedades más interesantes de los conjuntos radican en sus operaciones principales: 

# UNIÓN

# INTERSECCIÓN

# DIFERENCIA

#									U 		N 		I 		O 		N

#La UNIÓN se realiza con el caracter | y retorna un conjunto que contiene los elementos que se encuentran en al 
#menos uno de los dos conjuntos involucrados en la operación.

>>> a = {1, 2, 3, 4}			>>> a = {1, 2, "3", "4"}	

>>> b = {3, 4, 5, 6}			>>> b = {"3", "4", 5, 6}

>>> a | b 						# Como ya vimos, si hay elementos duplicados, se unifican, por eso solo hay
								# un número 3 y solo hay un número 4
{1, 2, 3, 4, 5, 6}

# Como vemos, la operacion de unios, devuelve los elementos que se encuentren que estan en al menos uno de los 2 conjuntos


# 					I 		N 		T 		E 		R 		S 		E 		C 		C 		I 		Ó 		N


# La INTERSECCIÓN opera de forma análoga, pero con el operador &, y retorna un nuevo conjunto con los elementos 
# que se encuentran en ambos.


>>> a = {1, 2, 3, 4}

>>> b = {3, 4, 5, 6}

>>> a & b

{3, 4}

# Es decir, intersección devuelve SOLO LOS ELEMENTOS que estan EN AMBOS conjuntos.


# 			D 		I 		F 		E 		R 		E 		N 		C 		I 		A


#La DIFERENCIA, por último, retorna un nuevo conjunto que contiene LOS ELEMENTOS DE A QUE NO ESTAN EN B. Se usa el símbolo - (menos)

>>> a = {1, 2, 3, 4}

>>> b = {2, 3}

>>> a - b

{1, 4}


#	O    T    R    A    S        O    P    E    R    A    C    I    O    N    E    S

#Se dice que B es un SUBCONJUNTO de A cuando todos los elementos de aquél (b) pertenecen también a éste (a). 
#Python puede determinar esta relación vía el método issubset().

>>> a = {1, 2, 3, 4}

>>> b = {2, 3}

>>> b.issubset(a)

True

# Cuando TODOS los elementos de un conjunto (b) tambien estan en el otro conjunto (a), se dice que
# es un SUBCONJUNTO. Como vemos aqui arriba, la funcion b.issubset(a) devuelve TRUE


#Inversamente, se dice que A es un SUPERCONJUNTO de B.


>>> a = {1, 2, 3, 4}

>>> b = {2, 3}

>>> a.issuperset(b)

True


# La definición de estas dos relaciones nos lleva a concluir que todo conjunto es al mismo tiempo 
# un SUBCONJUNTO y un SUPERCONJUNTO de sí mismo.

>>> a = {1, 2, 3, 4}
>>> a.issubset(a)
True
>>> a.issuperset(a)
True


# 				D 	I 	F 	E 	R 	E 	N 	C 	I 	A 		S 	I 	M 	É 	T 	R 	I 	C 	A


# La diferencia simétrica retorna un nuevo conjunto el cual contiene los elementos que pertenecen a alguno de los dos 
# conjuntos que participan en la operación pero no a ambos

# RETORNA LOS ELEMENTOS QUE PERTENECEN A ALGUNO DE LOS 2 CONJUNTOS, PERO NO DE AMBOS!!!


>>> a = {"1", "2", 3, 4}

>>> b = {3, 4, "5", "6"}

>>> a.symmetric_difference(b)

{1, 2, 5, 6}































































































































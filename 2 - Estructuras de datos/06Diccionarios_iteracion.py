Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 	D	I	C	C	I	O	N	A	R	I	O	S
>>> #	I	T	E	R	A	C	I	O	N
>>> 
>>> # Iteracion se refiere a recorrer los elementos del diccionario.
>>> 
>>> # RECORDAR que NO esta garantizado el orden de los elementos en un diccionario!!!
>>> 
>>> calificaciones = {"aldo":9,"kevin":6,"pedro":8}
>>> calificaiones
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    calificaiones
NameError: name 'calificaiones' is not defined
>>> calificaciones
{'aldo': 9, 'kevin': 6, 'pedro': 8}
>>> 
>>> # Una lista la recorremos con un ciclo FOR. En un diccionario es muy similar:
>>> for calificacion in calificaciones:
	print(calificacion)

	
aldo
kevin
pedro
>>> 
>>> # Como vemos, este ciclo ITERA LAS LLAVES del diccionario.
>>> # Para acceder a los valores de las llaves escribimos lo siguiente:
>>> 
>>> for calificacion in calificaciones:
	print(calificaciones[calificacion])

	
9
6
8
>>> # Para acceder a los valores de las llaves, simplemente imprimimos nuestro diccionario (llamado calificaciones), y ponemos entre corchetes la llave a la que queremos acceder, en este caso "calificacion" es donde guarda cada llave en cada iteracion
>>> 
>>> # Para acceder mas facilmente al valor de nuestras llaves, usaremos un METODO llamado KEYS (LLAVES)
>>> # Es mucho mas facil que especificando el diccionario y la iteracion actual, como vemos arriba, se escribe asi:
>>> 
>>> for key in calificaciones.keys()
	print(key)
	
SyntaxError: invalid syntax
>>> 
>>> # Error xD, ahora si:
>>> 
>>> for key in calificaiones.keys():
	print(key)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for key in calificaiones.keys():
NameError: name 'calificaiones' is not defined
>>> 
>>> # OTRO ERROR! LOL
>>> 
>>> for key in calificaciones():
	print(key)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for key in calificaciones():
TypeError: 'dict' object is not callable
>>> 
>>> 


>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> for key in calificaciones.keys():
	print(key)

	
aldo
kevin
pedro
>>> 
>>> # Como vemos, este metodo (keys), nos devuelve un iterable, que contiene las llaves de nuestro diccionario
>>> # Del mismo modo, si queremos OBTENER LOS VALORES de las llaves, existe el metodo VALUES:
>>> 
>>> for value in calificaciones.values():
	print(value)

	
9
6
8
>>> # Este metodo devuelve un iterable con los valores.
>>> # Para que devuelva AMBOS (llave y valor), existe el metodo llamado ITEMS:
>>> 
>>> for item in calificaiones.items():
	print(item)

	
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    for item in calificaiones.items():
NameError: name 'calificaiones' is not defined
>>> 
>>> for item in calificaciones.items():
	print(item)

	
('aldo', 9)
('kevin', 6)
('pedro', 8)
>>> 
>>> # Esto devuelve una TUPLA por cada elemento de nuestro diccionario, que va a contener la LLAVE y su respectivo VALOR.
>>> 
>>> #	P	R	A	C	T	I	C	A
>>> 
>>> diccionario = {"a":1, "b":2, "c":3, "d":4}
>>> 
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> 
>>> diccionario["e"] = 5
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> diccionario.update({"f":6,"g":7,"h"8})
SyntaxError: invalid syntax
>>> diccionario.update({"f":6,"g":7,"h":8})
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
>>> 
>>> 
>>> diccionario["i"] = 9
>>> del diccionario["i"]
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
>>> 
>>> diccionario["h"] = 9
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 9}
>>> diccionario["h"] = 8
>>> diccionario
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
>>> for key in diccionario.keys():
	print(key)

	
a
b
c
d
e
f
g
h
>>> for value in diccionario.values():
	print(value)

	
1
2
3
4
5
6
7
8
>>> for item in diccionario.items():
	print(item)

	
('a', 1)
('b', 2)
('c', 3)
('d', 4)
('e', 5)
('f', 6)
('g', 7)
('h', 8)
>>> 

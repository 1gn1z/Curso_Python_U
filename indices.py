Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alfabeto = "abcdefgihjklmnopqstrvwxyz"
>>> alfabeto = "abcdefghijklmnopqrstuvwxyz"
>>> alfabeto_lista = list(alfabeto)
>>> 
>>> alfabeto_lista
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> alfabeto_lista.index('a')
0
>>> alfabeto_lista.index('b')
1
>>> alfabeto_lista.index('z.')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    alfabeto_lista.index('z.')
ValueError: 'z.' is not in list
>>> alfabeto_lista.index('z')
25
>>> 
>>> alfabeto.index('a')
0
>>> alfabeto.index('bc')
1
>>> #Cuando son 2 elementos arroja desde la primera posicion en la que se encuentra, por eso empieza a contar desde la b
>>> #Cuando queremos saber que elemento esta en una posicion X escribimos entre corchetes el numero de la posicion:
>>> alfabeto_lista[10]
'k'
>>> alfabeto[10]
'k'
>>> #Cuando queremos saber que elemento esta en una posicion X escribimos entre corchetes el numero de la posicion:
>>> #Esto sin necesidad de agregar el metodo INDEX como vemos arriba
>>> 
>>> # El INDEX se ocupa para indicar el elemento que deseamos conocer su posicion, si consultamos la posicion
>>> # El index ya no es necesario, solo se especifica el numero de posicion entre corchetes como vemos arriba
>>> #Tambien podemos usar INDICES NEGATIVOS, empezando por menos 1 (-1), que sera el ultimo elemento:
>>> alfabeto_lista[-1]
'z'
>>> alfabeto_lista[26]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    alfabeto_lista[26]
IndexError: list index out of range
>>> alfabeto_lista[25]
'z'
>>> alfabeto[-1]
'z'
>>> alfabeto[25]
'z'
>>> 

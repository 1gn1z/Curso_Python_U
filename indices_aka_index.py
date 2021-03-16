Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	I	N	D	I	C	E	S
>>> 
>>> alfabeto = 'abcdefghijklmnopqrstuvwxyz'
>>> alfabeto
'abcdefghijklmnopqrstuvwxyz'
>>> alfabeto_lista = list(alfabeto)
>>> alfabeto_lista
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> 
>>> # Los indices indican la POSICION de un elemento en una lista o cadena
>>> # PERO! los indices empiezan a contar desde el 0
>>> 
>>> alfabeto_lista.index('a')
0
>>> # Ponemos la lista, .index y entre parentesis el elemento que deseamos
>>> # saber su ubicacion
>>> # Tambien se puede hacer para las cadenas
>>> alfabeto.index('z')
25
>>> alfabeto.index('a')
0
>>> alfabeto.index('b')
1
>>> # Si buscamos un elemento que NO esta:
>>> alfabeto.index(0)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    alfabeto.index(0)
TypeError: must be str, not int
>>> # Como vemos en la ultima linea, dice que tiene que ser una cadena, no un entero
>>> 

>>> # Tambien podemos usar el metodo index para 2 elementos:
>>> alfabeto.index('bc')
1
>>> # En este caso encuentra primero la b, que es por donde empieza a contar, por eso devuelve 1
>>> 
>>> # Para buscar un elemento POR SU POSICION, usamos corchetes. Por ejemplo, si queremos saber que elemento se encuentra en la posicion 10, escribimos asi:
>>> 
>>> 
>>> alfabeto_lista[10]
'k'
>>> # Buscamos exactamente igual ya sea en una lista o una cadena:
>>> alfabeto[10]
'k'
>>> # En python tambien se puede buscar via INDICE NEGATIVO:
>>> alfabeto.index(-1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    alfabeto.index(-1)
TypeError: must be str, not int
>>> alfabeto[-1]
'z'
>>> alfabeto_lista[-1]
'z'
>>> 

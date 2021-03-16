Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #		D	E	L
>>> # DEL, de DELETE, sirve para BORRAR ELEMENTOS DE UNA LISTA O CADENA o incluso para BORRAR VARIABLES COMPLETAS.
>>> 
>>> vocales = 'aeiou'
>>> lista_vocales = list(vocales)
>>> lista_vocales
['a', 'e', 'i', 'o', 'u']
>>> vocales
'aeiou'
>>> var_basura = 'Spam and eggs'
>>> 
>>> # Para borrar una variable completa, escribimos DEL mas el nombre de la variable:
>>> var_basura
'Spam and eggs'
>>> del var_basura
>>> var_basura
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    var_basura
NameError: name 'var_basura' is not defined
>>> # Como vemos, indica que la variable basura NO esta definida
>>> # Como dijimos, DEL tambien permite borrar elementos de una lista o cadena.
>>> # Para borrar un elemento usamos la palabra reservada DEL seguida de la variable donde se ubica el elemento, y el elemento entre corchetes, asi:
>>> #	del variable[]
>>> #	del variable[numero de posicion]
>>> del lista_vocales[0]
>>> lista_vocales
['e', 'i', 'o', 'u']
>>> # Como vemos, ya no esta la letra a, osea la posicion 0 de la lista
>>> # Igualmente podemos usar indices negativos.
>>> del lista_vocales[-1]
>>> lista_vocales
['e', 'i', 'o']
>>> # LAS CADENAS SON INMUTABLES!!! NO PODEMOS MODIFICAR UNA CADENA SIN CREAR UNA NUEVA, lo mas facil es volverla una lista, modificarla, y regresarla a cadena
>>> 
>>> cadena = 'wxyz'
>>> 
>>> 
>>> 
>>> #	E	J	E	R	C	I	C	I	O
>>> # Modificar una cadena, convirtiendola en lista y modificada volver a convertirla en cadena
>>> 
>>> cadena = 'wxyz'
>>> cadena_lista = cadena.split()
>>> cadena_lista
['wxyz']
>>> cadena_lista = cadena.split(´, ´)
SyntaxError: invalid character in identifier
>>> cadena_lista = cadena.split(', ')
>>> cadena_lista
['wxyz']
>>> cadena_lista = cadena.split(',')
>>> cadena_lista
['wxyz']
>>> cadena_lista = list(cadena)
>>> cadena_lista
['w', 'x', 'y', 'z']
>>> cadena_lista.extend([1, 2, 3])
>>> cadena_lista
['w', 'x', 'y', 'z', 1, 2, 3]
>>> # Ya modificada la lista, volvemos a convertirla en cadena con el metodo JOIN
>>> ''.join(cadena_lista)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    ''.join(cadena_lista)
TypeError: sequence item 4: expected str instance, int found
>>> cadena_lista.extend(['1, 2, 3'])
>>> ''.join(cadena_lista)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    ''.join(cadena_lista)
TypeError: sequence item 4: expected str instance, int found
>>> ''.join(cadena_lista)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ''.join(cadena_lista)
TypeError: sequence item 4: expected str instance, int found
>>> cadena = ','.join(cadena_lista)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    cadena = ','.join(cadena_lista)
TypeError: sequence item 4: expected str instance, int found
>>> cadena_lista.extend(['1, 2, 3'])
>>> cadena = ','.join(cadena_lista)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    cadena = ','.join(cadena_lista)
TypeError: sequence item 4: expected str instance, int found
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

>>> cadena = 'aeiou'
>>> cadena_lista = list(cadena)
>>> cadena_lista
['a', 'e', 'i', 'o', 'u']
>>> cadena_lista.extend('x,y,z')
>>> cadena_lista
['a', 'e', 'i', 'o', 'u', 'x', ',', 'y', ',', 'z']
>>> cadena_lista.extend('xyz')
>>> cadena_lista
['a', 'e', 'i', 'o', 'u', 'x', ',', 'y', ',', 'z', 'x', 'y', 'z']
>>> del cadena_lista[0]
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


>>> 

>>> 


>>> 
>>> cadena = 'aeiou'
>>> cadena_lista = list(cadena)
>>> cadena_lista
['a', 'e', 'i', 'o', 'u']
>>> cadena_lista.extend('xyz')
>>> cadena_lista
['a', 'e', 'i', 'o', 'u', 'x', 'y', 'z']
>>> # Ya tenemos la lista modificada, ahora solo falta convertirla en cadena
>>> cadena_prueba = ','.join(cadena_lista)
>>> cadena_prueba
'a,e,i,o,u,x,y,z'
>>> # Ya tenemos la cadena modificada :)
>>> cadena_prueba = ', '.join(cadena_lista)
>>> cadena_prueba
'a, e, i, o, u, x, y, z'
>>> # Podemos agregarle un espacio si lo necesitamos :D
>>> cadena_prueba = '==='.join(cadena_lista)
>>> cadena_prueba
'a===e===i===o===u===x===y===z'
>>> # O podemos usar otros delimitadores con el metodo JOIN :DDD
>>> 

>>> # APPEND SOLO AGREGA UN ELEMENTO al final de la lista, la lista incrementa SOLO EN UNO.
>>> # EXTEND AÑADE TODOS LOS ELEMENTOS al final de la lista, la lista incrementa TODOS LOS ELEMENTOS ESPECIFICADOS
>>> 
>>> 

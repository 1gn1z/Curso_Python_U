Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	T	U	P	L	A	S
>>> 
>>> # Los diccionarios y las listas SON MUTABLES. En las listas por ejemplo, podemos añadir, borrar o reemplazar elementos.
>>> # Pero a veces necesitamos que los datos NO CAMBIEN, para ello tenemos a las tuplas
>>> 
>>> # Las tuplas son parecidas a las listas, pero las tuplas NUNCA van a variar su informacion.
>>> 
>>> # Las tuplas se escriben entre PARENTESIS ()
>>> 
>>> tupla_1 = (1,2,3,4)
>>> tupla_1
(1, 2, 3, 4)
>>> 
>>> # Lo que forma escencialmente las tuplas son LAS COMAS, podemos escribir tuplas SIN PARENTESIS:
>>> 
>>> tupla_2 = 1,2,3,4
>>> tupla_2
(1, 2, 3, 4)
>>> 
>>> # Como vemos, sucede exactamente lo mismo sin agregar el parentesis
>>> # El parentesis es una especie de convencion general, aunq no es del todo necesario.
>>> 
>>> tupla_3 = (1)
>>> tupla_3
1
>>> # Como vemos, al imprimir este dato, NO es tupla, simplemente es un entero simple.
>>> # Lo que hace la tupla es la coma.
>>> 
>>> tupla_3 = (1,)
>>> tupla_3
(1,)
>>> # Listo, ahora si es una tupla.
>>> # La tupla es INMUTABLE, no podemos borrar ni modificar elementos ni nada.
>>> 
>>> del tupla_1[1]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del tupla_1[1]
TypeError: 'tuple' object doesn't support item deletion
>>> # Como vemos en la linea de aqui arriba, indica que las tuplas no soportan borrado de items
>>> 
>>> # Al igual que con los diccionarios y las listas, para acceder a un elemento en especifico lo hacemos via su INDICE.
>>> 
>>> tupla_1[0]
1
>>> tupla_1[1]
2
>>> 
>>> 
>>> tupla_4 = (1, "1gn1z",[0,1,2])
>>> tupla_4[0] = 2
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    tupla_4[0] = 2
TypeError: 'tuple' object does not support item assignment
>>> # Las tuplas son inmutables
>>> 
>>> # Si intentamos SUMAR por ejemplo, si lo hace:
>>> 
>>> tupla_4[0]+1
2
>>> # Pero solo suma en esta iteracion, la tupla permanece exactamente igual.
>>> tupla_4
(1, '1gn1z', [0, 1, 2])
>>> 
>>> # Solo hay un detalle, si tenemos UN ELEMENTO MUTABLE DENTRO DE NUESTRA TUPLA, SI PODEMOS MODIFICAR ESE ELEMENTO, en este caso por ejemplo, UNA LISTA:
>>> 
>>> # Lo unico que NO podemos hacer, es borrar la lista completamente:
>>> 
>>> tupla_4[2][2] = 3
>>> tupla_4
(1, '1gn1z', [0, 1, 3])
>>> 
>>> # Aqui ponemos doble corchete, el primero indica el indice del elemento, en este caso la lista, y el segundo indica el indice dentro de la lista, que seria tambien el ultimo, es decir el 2
>>> 
>>> # tupla_4 = (1, "1gn1z",[0,1,2])
>>> 
>>> # Primeros corchetes: Indican el tercer elemento de la tupla, es decir, la lista
>>> # Segundos corchetes: Indican el tercer elemento dentro de la lista, es decir, el numero 2
>>> 
>>> 

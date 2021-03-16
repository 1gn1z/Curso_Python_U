Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Los slices permiten tomar mas de una posicion en las LISTAS o CADENAS
>>> 
>>> numeros = [0,1,2,3,4,5,6,7,8,9,10]
>>> numeeros
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    numeeros
NameError: name 'numeeros' is not defined
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Cuando queriamos tomar SOLO UN elemento de la lista lo haciamos de la siguiente manera:
>>> numeros[1]
1
>>> # Si queremos sacar varios elementos a la vez, por ejemplo del 1 al 5, simplemente escribimos el punto de PARTIDA, y el punto FINAL. Si queremos llegar al 5 el punto de llegada SIEMPRE ES PUNTO DE LLEGADA +1
>>> 
>>> numeros[0:6]
[0, 1, 2, 3, 4, 5]
>>> 
>>> # El punto de partida es INCLUSIVO, es decir, empieza exactamente donde le indiquemos.
>>> # El punto de llegada es EXCLUSIVO, es decir, TOMA el numero ANTERIOR, por eso ponemos punto de llegada +1
>>> 
>>> numeros[0:7]
[0, 1, 2, 3, 4, 5, 6]
>>> 
>>> # Si solo queremos tomar el primer elemento con slices, lo hariamos asi:
>>> 
>>> numeros[0:1]
[0]
>>> 
>>> # Ahora, si ponemos un numero que no este en la lista, nos dara error de indice, o index error
>>> numeros[11]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    numeros[11]
IndexError: list index out of range
>>> 
>>> # Si queremos tomar todos los elementos de la lista, como le hacemos con slices? Ya que si ponemos 11, es decir, un numero mayor que el ultimo de la lista, nos mandara error como ya vimos.
>>> 
>>> # La respuesta es, simplemente indicar el punto de partida, los 2 puntos y no especificamos el punto de llegada, de este modo toma el ultimo elemento posible de la lista
>>> 
>>> # Esto funciona igual si ponemos un numero muy grande
>>> 
>>> numeros[0:9999]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> # Para sacar todos los elementos, sin tener que usar numeros grandes en el punto de llegada, simplemente indicamos el punto de inicio y los 2 puntos SIN ESPEIFICAR EL PUNTO DE LLEGADA
>>> 
>>> 
>>> numeros[0:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[1:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[2:]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> ..
SyntaxError: invalid syntax
>>> # Igual si NO especificamos el punto de partida, tomara desde la primera posicion de la lista
>>> 
>>> numeros[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[:6]
[0, 1, 2, 3, 4, 5]
>>> 
>>> # Como vemos aqui arriba, si no especificamos el punto de partida, toma desde la primera posicion de la lista, y podemos indicar solamente el punto de llegada sin ningun problema.
>>> 
>>> # Y si NO indicamos ni el punto de llegada ni el de partida, simplemente toma todos los elementos de la lista.
>>> 
>>> numeros[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Los Slices tambien tienen indices negativos, y se usan exactamente igual que en los indices de las listas
>>> 
>>> numeros[-1]
10
>>> 
>>> # RETO! sacar del 5 al 7 usando slices e indices negativos
>>> 
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[-6:-3]
[5, 6, 7]
>>> 
>>> # Reto cumplido! :3
>>> 
>>> 
>>> # Los slices aplican igual que los indices, por ejemplo:
>>> 
>>> numeros[-6:]
[5, 6, 7, 8, 9, 10]
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nu
>>> numeros[-11:-7]
[0, 1, 2, 3]
>>> numeros[:-7]

[0, 1, 2, 3]
>>> numeros[:-3]
[0, 1, 2, 3, 4, 5, 6, 7]
>>> 

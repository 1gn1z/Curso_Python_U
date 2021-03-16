Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # A veces queremos mas de un elemento en una lista, tal vez queramos 2 elementos, 3, el de enmdedio hasta el final menos 2, para esto tenemos los llamados SLICES (rebanadas).
>>> # Podemos pensar por ejemplo en las rebanadas de un pastel, podemos tomar mas de una, o la que queramos.
>>> # La rebanada de la posicion que mas nos guste, en fin, CUALQUIER rebanada, esos son los SLICES:
>>> 
>>> # Las Slices permiten obtener trozos de cosas como una LISTA o una CADENA.
>>> 
>>> # Para trabajar con los slices en python:
>>> # Primero hagamos una lista:
>>> 
>>> nums = [0,1,2,3,4,5,6,7,8,9,10]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Antes, para tomar UN SOLO elemento podriamos hacer lo siguiente:
>>> nums[0]
0
>>> nums[1]
1
>>> # En este caso los numeros estan de acuerdo a su indice, 0 es 0, 1 es 1, etc.
>>> 
>>> # Para extraer los numeros, por ejemplo, del 1 al 5, se usan los SLICES.
>>> # Para usar los Slices escribimos el PUNTO DE PARTIDA, DOS PUNTOS, Y EL PUNTO FINAL + 1:
>>> nums[0:6]
[0, 1, 2, 3, 4, 5]
>>> 
>>> # Por que usamos el punto final +1? Xq el punto de partida es INCLUSIVO, es decir, empieza exactamente donde le digamos
>>> # El punto final es EXCLUSIVO, osea no toca el punto final, toca el punto ANTERIOR al punto final.
>>> 
>>> 

>>> # Si quisieramos tomar desde el 0 hasta el 6, por ejemplo, lo hariamos de la siguiente manera:
>>> 
>>> nums[0:7]
[0, 1, 2, 3, 4, 5, 6]
>>> 
>>> # Si queremos tomar solo el primer elemento con slices, lo podemos hacer asi:
>>> 
>>> nums[0:1]
[0]
>>> # De este modo toma la primera posicion (0), el uno ya no lo cuenta xq toma el indice anterior, osea el 0.
>>> 
>>> # Si nos salimos de rango, es decir, si pedimos un indice que NO existe, nos dará un IndexError:
>>> 
>>> nums[11]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nums[11]
IndexError: list index out of range
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> # Si el elemento final de un slice es EXCLUSIVO, como le hariamos para obtener todos los elementos con rebanadas?
>>> # Ya que si ponemos del 0 al 10 devuelve hasta el 9, y como ya vimos, si ponemos del 0 al 11 nos mandara un error
>>> # Entonces, los slices, son mas inteligentes que los indices, si ponemos del 0 al 11, llegara desde el 0 y
>>> # Tomara el ultimo elemento posible.
>>> 
>>> nums[0:11]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # De la misma forma, si ponemos del 0 a un número muy largo, igualmente tomara la ultima posicion posible:

>>> 
nums[0:99999999]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # El slice retorna hasta el ultimo valor o indice posible, por eso al poner un numero muy grande dice
>>> # Yo ya no encuentro nada despues del 10, asi que te devuelvo hasta ese
>>> 
>>> 

>>> # Pero debe haber un modo mas facil de trabajar con listas y slices, que pasa por ejemplo si la lista SI tiene un
>>> # numero gigante.
>>> 
>>> # Para obtener TODO usando slices podemos hacer algo como esto:
>>> 
>>> nums[0:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Como vemos, podemos usar solo la primera posicion (en este caso 0), y los 2 puntos SIN el indice final o de llegada
>>> # De este modo, nos retornara desde el primer elemento hasta el ultimo elemento existente en esa lista o cadena.
>>> 
>>> 



>>> 
>>> 
>>> # Y asi podemos obtener los elementos desde la posicion que queramos, hasta el final, sin especificar el punto de llegada
>>> nums[1:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums[2:]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # De la misma forma, si dejamos el punto de inicio vacio, y ponemos el punto de llegada, contara desde el principio
>>> # Hasta el numero que especificamos, es decir, de la primera posicion hasta el numero de llegada MENOS 1
>>> 
nu
>>> nums[:3]
[0, 1, 2]
>>> 
>>> # Y si no ponemos NADA, ni punto de inicio ni punto de llegada, pues simplemente DEVUELVE TODOS
>>> nums[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 

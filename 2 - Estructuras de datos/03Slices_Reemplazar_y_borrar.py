Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> numeros = [0,1,2,3,4,5,6,7,8,9,10]
>>> 
>>> # Recordemos que en las listas para borrar un elemento usamos la palabra reservada DEL, la lista o cadena, y entre corchetes el indice del elemento que queremos borrar:
>>> del numeros[0]
>>> numeros
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Es facil para listas pequeñas, pero que haremos con una lista de cientos o miles de elementos?
>>> # Con los Slices podemos borrar mas de un elemento, por ejemplo, queremos borrar del 1 al 5
>>> # Pues lo hacemos igual solamente que en este caso usamos las rebanadas
>>> 
>>> del numeros[0:5]
>>> numeros
[6, 7, 8, 9, 10]
>>> 
>>> # RECORDAR QUE EL PUNTO DE LLEGADA ES EXCLUSIVO, debemo escribir el INDICE MAS UNO, esto borra el elemento ANTERIOR AL ESPECIFICADO
>>> 
>>> # Podemos borrar cualquier elemento de cualquier posicion, por ejemplo, vamos a borrar el 8 y el 9
>>> 
>>> del numeros[2:4]
>>> numeros
[6, 7, 10]
>>> 
>>> #	R	E	E	M	P	L	A	Z	A	R
>>> 
>>> # Digamos que nos equivocamos y queremos volver a poner el 8 y 9, para eso usamos los Slices, especificando desde que posicion inicia el reemplazo, hasta que posicion, y luego ponemos igual y añadimos otra lista con los elementos deseados:
>>> 
>>> #
>>> # numeros[1:2] = [7,8,9]
>>> 
>>> # Aqui estamos diciendo que se va a reemplazar el elemento que esta de la posicion 1 a la 2, osea el numero 7, y en esa posicion vamos a insertar la nueva lista, osea los numeros deseados INCLUYENDO EL REEMPLAZO, ya que si no lo incluimos se reemplaza por el primer numero indicado en la nueva lista a añadir.
>>> 
>>> numeros
[6, 7, 10]
>>> numeros[1:2] = [6,7,8]
>>> numeros
[6, 6, 7, 8, 10]
>>> 
>>> 
>>> 
>>> 
>>> numeros[1:2] = [7,8]
>>> numeros
[6, 7, 8, 7, 8, 10]

>>> numeros = [5,6,9,10]
>>> numeros[1:2] = [6,7,8]
>>> numeros
[5, 6, 7, 8, 9, 10]
>>> # Correcto.
>>> 
>>> numeros
[5, 6, 7, 8, 9, 10]
>>> #
>>> # RETO!!! Digamos que queremos reemplazar el 9 y 10 por 90 y 100, por ejemplo
>>> 
>>> 
>>> numeros[4:5] = [90,100]
>>> numeros
[5, 6, 7, 8, 90, 100, 10]
>>> numeros = [5, 6, 7, 8, 9, 10]
>>> numeros[4:6] = [90,100]
>>> numeros
[5, 6, 7, 8, 90, 100]
>>> # Reto cumplido!, aqui para reemplazar el 10, tenemos que especificar el punto de llegada normalmente, es decir, punto de llegada mas 1!.
>>> 
>>> numeros = [5, 6, 7, 8, 9, 10]
>>> numeros[4:6] = [90,100]
>>> numeros
[5, 6, 7, 8, 90, 100]
>>> # RETO!!! Reemplazar 90 y 100 por 9 y 10 de regreso:
>>> 
>>> numeros[4:6] = [9,10]
>>> numeros
[5, 6, 7, 8, 9, 10]
>>> # Reto cumplido!
>>> numeros = [5, 6, 7, 8, 9, 10]
>>> numeros[4:6] = [90,100]
>>> numeros
[5, 6, 7, 8, 90, 100]
>>> # Podemos reemplazarlos tambien SIN ESPECIFICAR EL PUNTO DE LLEGADA, ya que si lo dejamos en blanco python toma el ultimo elemento disponible en la lista:
>>> 
>>> numeros
[5, 6, 7, 8, 90, 100]
>>> numeros[4:] = [9,10]
>>> numeros
[5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> 
>>> 
>>> nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> #	P	R	A	C	T	I	C	A
>>> 
>>> # Reemplazar, mmmmm del 0 al 10 con decenas. el 0 pues por doble 0 xD
>>> 
>>> nums[0:6] = [00,10,20,30,40,50]
>>> nums
[0, 10, 20, 30, 40, 50, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Borrar las decenas.
>>> nums[:6] = [00,10,20,30,40,50]
>>> nums
[0, 10, 20, 30, 40, 50, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
>>> nums[0:6] = [00,10,20,30,40,50]
>>> nums
[0, 10, 20, 30, 40, 50, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Creo el 0 no se reemplaza por el doble por que pues ambos valen lo mismo, cero! xD
>>> 
>>> # Borrar las decenas.
>>> del nums[0:6]
>>> nums
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Regresar los primeros numeros, incluido el 0 ok
>>> 
>>> nums[0:1] = [0,1,2,3,4,5]
>>> nums
[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Se me olvido incluir el 6 xD, recordemos que se reemplaza por el primero de la nueva lista
>>> nums = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> nums[0:1] = [0,1,2,3,4,5,6]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Borrar alv del 10 al final
>>> del nums[10:]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> # Pues segun el punto de inicio era inclusivo, pero parece que si no se especifica el punto de llegada tambien es exclusivo, es decir, se tiene que especificar el punto de inicio +1
>>> 
>>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> del nums[11:]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Volver a añadir del 11 al 20
>>> 
>>> nums[10:] = [10,11,12,13,14,15,16,17,18,19,20]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> 
>>> nums[::2]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> nums[::3]
[0, 3, 6, 9, 12, 15, 18]
>>> 

>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> 
>>> # Borrar del 5 al 15 y reemplazar por decenas
>>> 
>>> del nums[5:15]
>>> nums
[0, 1, 2, 3, 4, 15, 16, 17, 18, 19, 20]
>>> 
>>> # Se me volvio a olvidar que el punto de llegada es exclusivo xd, otro intento :3
>>> 
>>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> # Borrar del 5 al 15 y reemplazar por decenas
>>> del nums[5:16]
>>> nums
[0, 1, 2, 3, 4, 16, 17, 18, 19, 20]
>>> # Añadir de nuevo los numeros eliminados.
>>> 
>>> nums[4:5] = [4,5,6,7,8,9,10,11,12,13,14,15]
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> 

>>> # Borrar pares
>>> 
>>> del nums[::2]
>>> nums
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
>>> nums[::2] = [0,2,4,6,8,10,12,14,16,18,20]
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    nums[::2] = [0,2,4,6,8,10,12,14,16,18,20]
ValueError: attempt to assign sequence of size 11 to extended slice of size 5
num
>>> 

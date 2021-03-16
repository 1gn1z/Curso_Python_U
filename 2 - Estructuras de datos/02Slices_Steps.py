Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	S	L	I	C	E	S	-	S	T	E	P	S
>>> 
>>> # Hay un tercer elemento en los slices, aparte del punto de llegada y el de final. Son los STEPS (pasos)
>>> 
>>> # Los STEPS, indican el numero de pasos entre cada elemento de nuestra rebanada.
>>> 
>>> numeros = [0,1,2,3,4,5,6,7,8,9,10]
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> # Para usar los steps tenemos los 2 numeros de inicio y fin, con sus 2 puntos numeros[0:1]
>>> # En los steps tenemos OTROS 2 PUNTOS DESPUES DEL PUNTO DE LLEGADA, que nos dicen el numero de pasos entre cada uno de los elementos de nuestra rebanada.
>>> 
>>> numeros[::2]
[0, 2, 4, 6, 8, 10]
>>> 
>>> # Como vemos, el numero de pasos, que es 2, toma los elementos que esten CADA 2 PASOS de la lista, por eso toma el 2, luego cuenta 2 pasos y toma el elemento, que seria el 4, luego cuenta 2 pasos y toma el elemento, que es el 6 y asi sucesivamente.
>>> # Igual podemos indicar 3, y toma los elementos que esten cada 3 pasos en la lista:
>>> 
>>> numeros[::3]
[0, 3, 6, 9]
>>> 
>>> # ya que sabemos como funcionan los slices, podemos por ejemplo tomar los numeros del 2 al 8 y contando pares (2)
>>> 
>>> numeros[2:9:2]
[2, 4, 6, 8]
>>> 
>>> # Tambien tenemos PASOS NEGATIVOS, por ejemplo, si indicamos un paso negativo nos devolvera la lista de forma invertida.
>>> 
>>> numeros[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[-2:-5:-1]
[9, 8, 7]
>>> 
>>> # Al usar el paso negativo -1 invierte completamente la lista
>>> numeros[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> # Estando asi la lista, invertida, tenemos los indices negativos ordenados de izquierda a derecha
>>> # Osea el indice -1 es el 10, que esta en el orden normal, de inicio a fin y no de fin a inicio (derecha a izquierda)
>>> 
>>> # RETOS!!! mmmm por ejemplo imprimir del 1 al 5 con slices negativos
>>> 
>>> numeros[-10:-7]
[1, 2, 3]
>>> numeros[-10:-5]
[1, 2, 3, 4, 5]
>>> # Recordemos que el punto de llegada es EXCLUSIVO. en este caso -5 seria el 6, pero toma el anterior, que es el 5
>>> 
>>> numeros[-10:-5]
[1, 2, 3, 4, 5]
>>> numeros[-10:-5:-1]
[]
>>> numeros[-10:-5:-1]
[]
>>> numeros[-10:-5:-2]
[]
>>> numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numeros[-10:-5:-2]
[]
>>> numeros[-10:-5]
[1, 2, 3, 4, 5]
>>> numeros[-10:-5:-1]
[]
>>> numeros[-10:-5:-3]
[]
>>> numeros[-10:-5]
[1, 2, 3, 4, 5]
>>> numeros[-10:-5:-2]
[]
>>> numeros[-10:-5:-2]
[]
>>> numeros[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> numeros[-10:-5:-1]
[]
>>> numeros[-2:-5:-1]
[9, 8, 7]
>>> numeros[::-3]
[10, 7, 4, 1]
>>> # Aqui, como usamos step negativo, empieza contando con indices negativos, es decir, comienza desde el 10
>>> 
>>> numeros[-11:-1:-3]
[]
>>> numeros[-10:-1:-3]
[]
>>> numeros[-2:-5:-2]
[9, 7]
>>> 
>>> 




>>> 

>>> 
>>> numeros[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> # Imprimir del 7 al 1 y sacar pares
>>> 
>>> 
>>> numeros[-10:-3:2]
[1, 3, 5, 7]
>>> numeros[-10:-3:-2]
[]
>>> numeros[-10:-3:1]
[1, 2, 3, 4, 5, 6, 7]
>>> numeros[-10:-3:3]
[1, 4, 7]
>>> numeros[-10:-3:-2]
[]
>>> numeros[-10:-3:-1]
[]
>>> numeros[-10:-3:-3]
[]
>>> numeros[-10:-3:3]
[1, 4, 7]
>>> numeros[-11:-3:-2]
[]
>>> numeros[-11:-3:2]
[0, 2, 4, 6]
>>> numeros[-11::2]
[0, 2, 4, 6, 8, 10]
>>> numeros[11::2]
[]
>>> numeros[::2]
[0, 2, 4, 6, 8, 10]
>>> 

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	D	I	C	C	I	O	N	A	R	I	O	S
>>> #	A	G	R	E	G	A	R,	B	O	R	R	A	R
>>> #	Y		A	C	T	U	A	L	I	Z	A	R
>>> 
>>> 

>>> dias_semana = {"Lunes":9, "Martes":10, "Miercoles":11}
>>> dias_semana
{'Lunes': 9, 'Martes': 10, 'Miercoles': 11}
>>> 
>>> # Para añadir un elemento a un diccionario lo unico que debemos hacer es poner el nombre del diccionario, entre corchetes la nueva llave, seguido de un signo de igual y el valor de esa llave:
>>> 
>>> dias_semana["Jueves"] = 12
>>> dias_seman
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dias_seman
NameError: name 'dias_seman' is not defined
>>> dias_semana
{'Lunes': 9, 'Martes': 10, 'Miercoles': 11, 'Jueves': 12}
>>> 
>>> # Para borrar un elemento simplemente escribimos DEL, el nombre del diccionario y entre corchetes la llave del elemento que deseamos borrar:
>>> 
>>> del dias_semana["Lunes"]
>>> dias_semana
{'Martes': 10, 'Miercoles': 11, 'Jueves': 12}
>>> 
>>> # Vamos a ACTUALIZAR varios elementos de nuestro diccionario. Esta cabron actualizar de uno por uno, afortunadamente hay un METODO para agregar mas de un elemento a un diccionario, se llama metodo UPDATE
>>> # Se escribe "nombre_del_diccionario".update y entre parentesis agregamos llaves, es decir, dentro de los parentesis agregamos un nuevo diccionario:
>>> 
>>> dias_semana.update({"Viernes":13, "Sabado":14})
>>> dias_semana
{'Martes': 10, 'Miercoles': 11, 'Jueves': 12, 'Viernes': 13, 'Sabado': 14}
>>> 
>>> # El metodo UPDATE tambien acepta llaves que ya teniamos con anterioridad, para REEMPLAZAR el valor de alguna llave:
>>> 
>>> dias_semana.update({"Sabado":15,"Domingo":16})
>>> dias_semana
{'Martes': 10, 'Miercoles': 11, 'Jueves': 12, 'Viernes': 13, 'Sabado': 15, 'Domingo': 16}
>>> 
>>> #	P	R	A	C	T	I	C	A
>>> dias_semana
{'Martes': 10, 'Miercoles': 11, 'Jueves': 12, 'Viernes': 13, 'Sabado': 15, 'Domingo': 16}
>>> del dias_semana["Martes","Miercoles"]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    del dias_semana["Martes","Miercoles"]
KeyError: ('Martes', 'Miercoles')
>>> 
>>> # Al parecer, como vemos arriba, solo se pueden eliminar entradas de una por una
>>> 
>>> del dias_semana["Lunes"]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del dias_semana["Lunes"]
KeyError: 'Lunes'
>>> del dias_semana["Martes"]
>>> dias_semana
{'Miercoles': 11, 'Jueves': 12, 'Viernes': 13, 'Sabado': 15, 'Domingo': 16}
>>> del dias_semana{["Miercoles","Jueves"]}
SyntaxError: invalid syntax
>>> del dias_semana{["Miercoles"],["Jueves"]}
SyntaxError: invalid syntax
>>> 
>>> 
>>> # Intente borrar de 2 pero no se pudo con ninguna de las dos formas de aqui arriba
>>> del dias_semana["Miercoles"]
>>> del dias_semana["Jueves"]
>>> del dias_semana["Viernes"]
>>> del dias_semana["Sabado"]
>>> del dias_semana["Domingo"]
>>> dias_semana
{}
>>> # Se pueden borrar todos los elementos de un diccionario, y como vemos, aparece vacio al llamarlo
>>> 
>>> dias_semana.update({"Lunes":1, "Martes":2, "Miercoles":3, "Jueves":4, "Viernes":5})
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5}
>>> 
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5}
>>> del dias_semana["Viernes"]
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4}
>>> dias_semana.update({"Viernes": 5,"Sabado":6,"Domingo":7})
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sabado': 6, 'Domingo': 7}
>>> 
>>> #	B	O	R	R	A	R
>>> 
>>> del dias_semana["Sabado"]
>>> del dias_semana["Domingo"]
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5}
>>> dias_semana.update({"Sabado":6, "Domingo":7})
>>> dias_semana
{'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sabado': 6, 'Domingo': 7}
>>> 
>>> #	R	E	E	M	P	L	A	Z	A	R
>>> # Vamos a reemplazar todos los valores por decenas.
>>> 
>>> dias_semana.update({"Lunes":10, "Martes":20, "Miercoles":30, "Jueves":40, "Viernes":50, "Sabado":60, "Domingo":70})
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60, 'Domingo': 70}
>>> 
>>> del dias_semana["Domingo"]
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60}
>>> 
>>> #	A	Ñ	A	D	I	R		1		ELEMENTO
>>> 
>>> dias_semana["Domingo"] = 70
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60, 'Domingo': 70}
>>> 
>>> del dias_semana["Sabado"]
>>> del dias_semana["Domingo"]
>>> dias_semana["Sabado"] = 60
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60}
>>> dias_semana["Domingo"] = 70
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60, 'Domingo': 70}
>>> del dias_semana["Viernes"]
>>> del dias_semana["Sabado"]
>>> del dias_semana["Domingo"]
>>> dias_semana.update({"Viernes":50, "Sabado":60, "Domingo":70})
>>> dias_semana
{'Lunes': 10, 'Martes': 20, 'Miercoles': 30, 'Jueves': 40, 'Viernes': 50, 'Sabado': 60, 'Domingo': 70}
>>> 
>>> letras = {"a":1,"b":2,"c":3}
>>> letras
{'a': 1, 'b': 2, 'c': 3}
>>> letras["d"] = 4
>>> letras
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> letras["e"] = 5
>>> letras
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> letras.update({"f":6,"g":7})
>>> letras
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
>>> letras["g"]
7
>>> 

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #	D	I	C	C	I	O	N	A	R	I	O	S
>>> 
>>> #	I	N	T	R	O	D	U	C	C	I	O	N
>>> 
>>> # Ejemplo de lista. Listas MUTABLES (MODIFICABLES)
>>> 
>>> lista_calificaciones = [9,10,6,5]
>>> lista_calificaciones
[9, 10, 6, 5]
>>> 
>>> # El diccionario tiene un conjunto de LLAVES, que podemos asociar a un valor el particular
>>> # Por ejemplo, podriamos tener la llave de PABLO, con la calificaion de 9, de Luis con la segunda calificacion y asi sucesivamente.
>>> 
>>> # LOS DICCIONARIOS TAMBIEN SON MUTABLES, podemos agregar, eliminar y modificar entradas.
>>> 
>>> # A diferencia de las listas, los diccionarios NO GARANTIZAN NINGUN ORDEN!. podemos agregar una entrada justo al principio y podria despues encontrarse al final del diccionario.
>>> 
>>> 

>>> # LOS DICCIONARIOS OCUPAN LLAVES!!! {
>>> 
>>> # diccionario = {}
>>> 

>>> # Los diccionarios, al igual que las listas, ADMITEN CUALQUIER TIPO DE DATO.
>>> 
>>> # Para escribir entradas en un diccionario, se escribe la llave y seguido de 2 puntos, el valor que contendra:
>>> 
>>> diccionario_calificaciones = {"Pablo":9,"Aldo":10,"Juan":6,"Kevin":5}
>>> diccionario_calificaciones
{'Pablo': 9, 'Aldo': 10, 'Juan': 6, 'Kevin': 5}
>>> 
>>> # Para acceder a un indice de un diccionario, tenemos que ingresar el NOMBRE de esa llave.
>>> 
>>> diccionario_calificaiones["Aldo"]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    diccionario_calificaiones["Aldo"]
NameError: name 'diccionario_calificaiones' is not defined
>>> diccionario_calificaciones["Aldo"]
10
>>> 
>>> 
>>> 




>>> 

>>> 


>>> 

>>> 
>>> diccionario_calificaiones["Aldo"]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    diccionario_calificaiones["Aldo"]
NameError: name 'diccionario_calificaiones' is not defined
>>> 
>>> 
>>> 


>>> 

>>> 
>>> diccionario_calificaciones["Aldo"]
10
>>> diccionario_calificaciones["Kevin"]
5
>>> # Podemos poner CUALQUIER TIPO DE DATO PARA LAS LLAVES Y PARA LOS VALORES
>>> 
>>> diccionario_calificaciones["Andres"] = "nueve"
>>> diccionario_calificaciones
{'Pablo': 9, 'Aldo': 10, 'Juan': 6, 'Kevin': 5, 'Andres': 'nueve'}
>>> # Aqui arriba agregamos una nueva entrada al diccionario.
>>> 
>>> # En python tenemos un METODO que nos ayuda a construir diccionarios, LLAMADA DICT.
>>> # Para construir el diccionario usando la funcion DICT tenemos que poner UNA LISTA, y dentro de la lista PONER UNA SERIE DE LLAVES Y VALORES:
>>> 
>>> dict([["pepe",7],["maria",4]])
{'pepe': 7, 'maria': 4}
>>> 
>>> # Este metodo es Va entre parentesis, dentro de corchetes, y cada entrada va dentro de otro corchete que contiene la entrada, osea la llave con su valor, es un poco verboso asi que es mas usual encontrar los diccionaris simplemente entre llaves como vimos al principio :3.
>>> 

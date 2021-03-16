Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Uso de 	S	P	L	I	T
>>> # Tenemos una cadena:
>>> nombreString = 'Mi nombre es Diego'
>>> 
>>> # Usamos la funcion Split de la siguente manera:
>>> nombreLista = nombreString.split()
>>> nombreLista
['Mi', 'nombre', 'es', 'Diego']
>>> 
>>> 
>>> # Uso de 	J	O	I	N
>>> 
>>> # Tenemos una LISTA:
>>> 
>>> paises = [ 'Mexico', 'Argentina', 'Chile', 'Peru' ]
>>> 
>>> # Para convertir esta lista en cadena usamos el metodo SPLIT
>>> # de la siguiente manera:
>>> 
>>> # ‘sep‘.join(lista)
>>> # donde sep representa el o los caracteres que deseamos utilizar como delimitador.
>>> 
>>> # En concreto seria asi:
>>> 
>>> paisesString = ','.join(paises)
>>> paisesString
'Mexico,Argentina,Chile,Peru'
>>> # Si deseamos utilizar los caracteres === como separador, tendremos que hacer
>>> paisesString = '==='.join(paises)
>>> paisesString
'Mexico===Argentina===Chile===Peru'
>>> 

>>> paisesString = '#'.join(paises)
>>> paisesString
'Mexico#Argentina#Chile#Peru'
>>> 

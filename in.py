Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # IN ayuda a verificar si algo esta dentro de algo, si una letra es parte de una cadena o si un elemento
>>> # es parte de una lista. Lo podemos usar en conjunto con los condicionales IF
>>> 
>>> vocales = 'aeiou'
>>> lista_vocales = list(vocales)
>>> # Si escribimos a in vocales, verifica si el elemento especificado se encuentra en la cadena o lista
>>> "a" in vocales
True
>>> "z" in vocales
False
>>> # Como vemos, si el elemento buscado esta en la cadena o lista devuelve un booleano TRUE, si no devuelve FALSE

>>> "a" in lista_vocales
True
>>> "x" in lista_vocales
False
>>> # Como dijimos anteriormente, se puede usar el in en nuestras condicionales IF
>>> # Para que la shell nos deje escribir mas lineas, presionamos CTRL + J
>>> 
>>> if "a" in vocales:
	print('El elemento esta en la variable')

	
El elemento esta en la variable
>>> # Tambien podemos usar la palabra NOT para verificar si algo NO esta en la variable:
>>> if "z" not in vocales:
	print('El elementi NO esta en la variable')

	
El elemento NO esta en la variable
>>> 

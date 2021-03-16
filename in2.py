Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #		I	N
>>> # IN verifica si algo esta dentro de otro algo, si una letra es parte de una cadena
>>> # o si un elemento esta dentro de una lista.
>>> # Nos devuelve un booleano, asi que podemos usarlo en conjunto con nuestras condicionales IF
>>> 
>>> vocales = 'aeiou'
>>> lista_vocales = list(vocales)
>>> 
>>> # Si escribimos 'a in vocales', verificara si la letra a esta en la variable vocales, o en la lista si escribimos in lista_vocales:
>>> 
>>> a in vocales
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a in vocales
NameError: name 'a' is not defined
>>> 'a' in vocales
True
>>> # Si escribimos un elemento que NO este en la lista o cadena obviamente devolvera un error:
>>> 
>>> 'z' in vocales
False
>>> # Mas bien devolvera FALSE, ya que el elemento NO esta en la variable o cadena
>>> # Igualmente podemos buscar algun elemento en una lista:
>>> 
>>> 'a' in lista_vocales
True
>>> # Como mencionamos, podemos usar IN en nuestras condicionales IF:
>>> 
>>> if 'a' in vocales:
	print('El elemento Si esta en la variable')

	
El elemento Si esta en la variable
>>> 
>>> # Tambien podemos usar la palabra reservada NOT para verificar si algo NO esta dentro de algo:
>>> # Por ejemplo si en nuestra variable vocales buscamos la Z, el NOT devuelve true ya que en efecto no esta la z.
>>> 
>>> if 'z' not in vocales:
	print('El elemento NO esta en la variable')

	
El elemento NO esta en la variable
>>> 

>>> # Funciona igual con las listas:
>>> 
>>> if 'a' in lista_vocales:
	print('el elemento esta en la variable')

	
el elemento esta en la variable
>>> 

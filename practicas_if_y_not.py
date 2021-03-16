Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alfabeto = "abcdefghijklmnopqrstuvwxyz"
>>> alfabeto_lista = list(alfabeto)
>>> alfabeto.index("a")
0
>>> alfabeto.index("z")
25
>>> alfabeto_lista.index("a")
0
>>> alfabeto_lista.index("z")
25
>>> alfabeto.index("%")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    alfabeto.index("%")
ValueError: substring not found
>>> alfabeto_lista.index("%")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    alfabeto_lista.index("%")
ValueError: '%' is not in list
>>> alfabeto_lista[10]
'k'
>>> alfabeto[10]
'k'
>>> alfabeto_lista[-1]
'z'
>>> alfabeto[-1]
'z'
>>> alfabeto[26]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    alfabeto[26]
IndexError: string index out of range
>>> alfabeto[25]
'z'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> vocales = "aeiou"
>>> lista_vocales = list(vocales)
>>> vocales
'aeiou'
>>> lista_vocales
['a', 'e', 'i', 'o', 'u']
>>> variable_basura = "Spam and Eggs"
>>> del variable_basura
>>> varible_basura
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    varible_basura
NameError: name 'varible_basura' is not defined
>>> lista_vocales
['a', 'e', 'i', 'o', 'u']
>>> del lista_vocales[0]
>>> lista_vocales
['e', 'i', 'o', 'u']
>>> del lista_vocales[-1]
>>> lista_vocale
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lista_vocale
NameError: name 'lista_vocale' is not defined
>>> lista_vocales
['e', 'i', 'o']
>>> del vocales[0]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    del vocales[0]
TypeError: 'str' object doesn't support item deletion
>>> var = "agregar una letra: "
>>> var2 = ''.join(var)
>>> var2
'agregar una letra: '
>>> del var2
>>> var2 = var.split()
>>> var2
['agregar', 'una', 'letra:']
>>> var2.append("Z")
>>> var2
['agregar', 'una', 'letra:', 'Z']
>>> var = var2
>>> var
['agregar', 'una', 'letra:', 'Z']
>>> var = ''.join(var2)
>>> var
'agregarunaletra:Z'
>>> var = ' '.join(var2)
>>> var
'agregar una letra: Z'
>>> 
>>> 
>>> 
>>> vocales = "aeiou"
>>> lista_vocales = list(vocales)
>>> "a" in vocales
True
>>> "z" in vocales
False
>>> 
>>> 
>>> 
>>> if "a" in vocales:
	print("el elemento a buscar esta en la cadena")
else:
	print("El elemento a buscar NO esta en la cadena")

el elemento a buscar esta en la cadena
>>> if "z" not in vocales:
	print("El elemento a buscar NO esta en la cadena")

	
El elemento a buscar NO esta en la cadena
>>> if "a" in lista_vocales:
	print("El elemento a buscar esta en la cadena")

	
El elemento a buscar esta en la cadena
>>> 
>>> 
>>> 
>>> var = "aeiou"
>>> var_lista = list(var)
>>> if "a" in var:
	print("El valor está en la cadena")
else:
	print("El valor NO está en la cadena")

	
El valor está en la cadena
>>> 

>>> if "z" in var:
	print("El valor esta en la cadena")
else:
	print("El valor NO esta en la cadena")

	
El valor NO esta en la cadena
>>> if "x" not in var:
	print("El elemento buscado NO esta en la cadena")
else:
	print("El elemento buscado esta en la cadena")

	
El elemento buscado NO esta en la cadena
>>> 

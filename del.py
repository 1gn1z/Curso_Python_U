Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> vocales = 'aeiou'
>>> vocales_list = list(vocales)
>>> vocales
'aeiou'
>>> vocales_list
['a', 'e', 'i', 'o', 'u']
>>> var_basura = 'var basura'
>>> var_basura
'var basura'
>>> del var_basura
>>> var_basura
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    var_basura
NameError: name 'var_basura' is not defined
>>> # podemos borrar elementos de una lista o cadena mediante su numero de posicion:
>>> 
>>> del lista_vocales[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    del lista_vocales[0]
NameError: name 'lista_vocales' is not defined
>>> del vocales_list[0]
>>> vocales_list
['e', 'i', 'o', 'u']
>>> del vocales_list[-1]
>>> vocales_list
['e', 'i', 'o']
>>> 

>>> del vocales[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del vocales[0]
TypeError: 'str' object doesn't support item deletion
>>> # Las cadenas son INMUTABLES, no se pueden modificar sin crear o reasignar otra :)
>>> 

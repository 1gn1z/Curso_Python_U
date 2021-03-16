Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> comida = "pechuga,papitas,pizza"
>>> comida.split(",")
['pechuga', 'papitas', 'pizza']
>>> "Mi comida favorita es: " + comida.split(",")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    "Mi comida favorita es: " + comida.split(",")
TypeError: can only concatenate str (not "list") to str
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 
>>> paises = ['Mexico', 'Argentina', 'Chile', 'Bolivia',]
>>> paises_string = ','.join(paises)
>>> paises_string
'Mexico,Argentina,Chile,Bolivia'
>>> paises_string = '==='.join(paises)
>>> paises_string
'Mexico===Argentina===Chile===Bolivia'
>>> nombre_string = 'Mi nombre es Diego'
>>> nombre_lista = nombre_string.split()
>>> nombre_lista
['Mi', 'nombre', 'es', 'Diego']
>>> nombres = ['Diego', 'Luis', 'Lula', 'Bugah']
>>> nombres_cadena = ',',join(nombres)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nombres_cadena = ',',join(nombres)
NameError: name 'join' is not defined
>>> nombres = ['Diego', 'Luis', 'Lula', 'Bugah',]
>>> nombres
['Diego', 'Luis', 'Lula', 'Bugah']
>>> nombres_string = ','.join(nombres)
>>> nombres_string
'Diego,Luis,Lula,Bugah'
>>> 
>>> 
>>> 



>>> 

>>> 


>>> 
>>> 


>>> 
>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> names = ['Luis', 'Juan', 'Pedro']
>>> names_string = ','.join(names)
>>> names_string
'Luis,Juan,Pedro'
>>> names_string = '==='.join(names)
>>> names_string
'Luis===Juan===Pedro'
>>> "Mis amigos son: " + names_string = ','.join(names)
SyntaxError: can't assign to operator
>>> "Mis amigos son: " + names = ','.join(names)
SyntaxError: can't assign to operator
>>> "Mis amigos son: " + ','.join(names)
'Mis amigos son: Luis,Juan,Pedro'
>>> "Mis amigos son: " + names
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    "Mis amigos son: " + names
TypeError: can only concatenate str (not "list") to str
>>> 
>>> 



>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> caracteres = ['a','b','c','d']
>>> caracteres_string = ', '.join(caracteres)
>>> caracteres_string
'a, b, c, d'
>>> "Las primeras 4 letras del alfabeto son: " + ', '.join(caracteres)
'Las primeras 4 letras del alfabeto son: a, b, c, d'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> letras = ['x','y','z']
>>> letras_string = '==='.join(letras)
>>> "Las últimas letras del alfabeto son: " + .join(letras)
SyntaxError: invalid syntax
>>> "Las últimas letras del alfabeto son: " + '=='.join(letras)
'Las últimas letras del alfabeto son: x==y==z'
>>> 
>>> 
>>> 
>>> 
>>> "Las últimas letras del alfabeto son: " + ', '.join(letras)
'Las últimas letras del alfabeto son: x, y, z'
>>> 
>>> 
>>> 
>>> 
>>> cadena = "Quiero ser una lista"
>>> cadena_lista = cadena.split()
>>> cadena_lista
['Quiero', 'ser', 'una', 'lista']
>>> "Da error al concatenar una cadena con una lista " + cadena.split()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    "Da error al concatenar una cadena con una lista " + cadena.split()
TypeError: can only concatenate str (not "list") to str
>>> 
>>> 
>>> 
>>> 
>>> cadena = "Quiero ser una lista"
>>> cadena = cadena.split()
>>> cadena
['Quiero', 'ser', 'una', 'lista']
>>> ''.join(cadena)
'Quieroserunalista'
>>> ' '.join(cadena)
'Quiero ser una lista'
>>> 
>>> 
>>> cadena = 'Quieroserunalista'
>>> cadena2 = cadena.split( )
>>> cadena2
['Quieroserunalista']
>>> cadena2 = cadena.split(' ')
>>> cadena2
['Quieroserunalista']
>>> cadena2 = cadena.split()
>>> cadena2
['Quieroserunalista']
>>> cadena = "Quiero ser una lista"
>>> cadena2 = cadena.split()
>>> cadena2
['Quiero', 'ser', 'una', 'lista']
>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> join1 = ['quiero', 'ser', 'una', 'cadena']
>>> join2 = ' '.join(join1)
>>> join2
'quiero ser una cadena'
>>> join2 = .join(join1)
SyntaxError: invalid syntax
>>> 
>>> 



>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> lista = ['Quiero', 'ser', 'una', 'cadena']
>>> lista_cadena = ' '.join(lista)
>>> lista_cadena
'Quiero ser una cadena'
>>> 'Convertí esta lista a texto ' + ' '.join(lista)
'Convertí esta lista a texto Quiero ser una cadena'
>>> 
>>> 
>>> 
>>> lista1 = "1, 2, 3, 4, 5"
>>> lista2 = lista1.split()
>>> lista2
['1,', '2,', '3,', '4,', '5']
>>> lista1 = "1,2,3,4,5"
>>> lista2 = lista1.split( )
>>> lista2
['1,2,3,4,5']
>>> lista2 = lista1.split(' ')
>>> lista2
['1,2,3,4,5']
>>> lista2 = lista1.split(', ')
>>> lista2
['1,2,3,4,5']
>>> lista2 = lista1.split()
>>> lista2
['1,2,3,4,5']
>>> +
SyntaxError: invalid syntax
>>> 
>>> 


>>> 

>>> 


>>> 

>>> l = ['1,2,3,4,5']
>>> l2 = l.split()
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    l2 = l.split()
AttributeError: 'list' object has no attribute 'split'
>>> l = '1,2,3,4,5'
>>> l2 = l.split()
>>> l2
['1,2,3,4,5']
>>> l = '12345'
>>> l2 = l.split()
>>> l2
['12345']
>>> l2 = l.split(' ')
>>> l2
['12345']
>>> l2 = l.split(', ')
>>> l2
['12345']
>>> 
>>> 



>>> 
>>> 


>>> l_c = 'esto es una lista'
>>> l01 = l_c.split()
>>> l01
['esto', 'es', 'una', 'lista']
>>> 
>>> 
>>> lista_cadena = 'Convertir esta cadena a lista con el método split'
>>> lista_convertida = lista_cadena.split()
>>> lista_convertida
['Convertir', 'esta', 'cadena', 'a', 'lista', 'con', 'el', 'método', 'split']
>>> lista_cadema
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    lista_cadema
NameError: name 'lista_cadema' is not defined
>>> lista_cadena
'Convertir esta cadena a lista con el método split'
>>> 
>>> lista = ['Convertir esta lista a cadena']
>>> ', '.join(lista_convertida)
'Convertir, esta, cadena, a, lista, con, el, método, split'
>>> lista_convertida = ', '.join(lista_cadena)
>>> lista_convertida
'C, o, n, v, e, r, t, i, r,  , e, s, t, a,  , c, a, d, e, n, a,  , a,  , l, i, s, t, a,  , c, o, n,  , e, l,  , m, é, t, o, d, o,  , s, p, l, i, t'
>>> 
>>> 
>>> 
>>> 
>>> lista = ['Convertir esta lista a cadena']
>>> lista2 = ' '.join(lista)
>>> lista2
'Convertir esta lista a cadena'
>>> lista2 =.join(lista)
SyntaxError: invalid syntax
>>> lista2 = ','.join(lista)
>>> lista2
'Convertir esta lista a cadena'
>>> lista2 = ','.join(lista)
>>> lista2
'Convertir esta lista a cadena'
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> lista = ['Convertir, esta, lista, a, cadena']
>>> lista2 = ''.join(lista)
>>> lista2
'Convertir, esta, lista, a, cadena'
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 

>>> lista = 'Convertir esta cadena a lista'
>>> lista2 = lista.split()
>>> lista2
['Convertir', 'esta', 'cadena', 'a', 'lista']
>>> 
>>> 
>>> 
>>> lista = ['Convertir esta lista a cadena']
>>> cadena = ', '.join(lista)
>>> cadena
'Convertir esta lista a cadena'
>>> 'Metodo join ' + ''.join(lista)
'Metodo join Convertir esta lista a cadena'
>>> 
>>> 
>>> 
>>> 
>>> c  = ['pechuga', 'papitas', 'pizza']
>>> c2 = ''.join(c)
>>> 'Mi comida favorita es: ' + ''.join(c)
'Mi comida favorita es: pechugapapitaspizza'
>>> c2 = ' '.join(c)
>>> 'Mi comida favorita es: ' + ' '.join(c)
'Mi comida favorita es: pechuga papitas pizza'
>>> 
>>> c3 = 'pechuga,papitas,pizza'
>>> c4 = c3.split()
>>> c4
['pechuga,papitas,pizza']
>>> c4 = c3.split( )
>>> c4
['pechuga,papitas,pizza']
>>> c4 = c3.split(' ')
>>> c
['pechuga', 'papitas', 'pizza']
>>> c4
['pechuga,papitas,pizza']
>>> c3 = 'pechuga, papitas, pizza'
>>> c4 = c3.split()
>>> c4
['pechuga,', 'papitas,', 'pizza']
>>> c4 = c3.split( )
>>> c4
['pechuga,', 'papitas,', 'pizza']
>>> c3 = 'pechuga, papitas, pizza'
>>> c4 = c3.split()
>>> c4
['pechuga,', 'papitas,', 'pizza']
>>> c3 = 'pechuga papitas pizza'
>>> c4 = c3.split()
>>> c4
['pechuga', 'papitas', 'pizza']
>>> c3 = 'pechugapapitaspizza'
>>> c4 = c3.split()
>>> c4
['pechugapapitaspizza']
>>> c4 = c3.split(', ')
>>> c4
['pechugapapitaspizza']
>>> c4 = c3.split(' ')
>>> c4
['pechugapapitaspizza']
>>> 

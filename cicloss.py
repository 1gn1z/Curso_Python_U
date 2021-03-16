# # El ciclo WHILE permite repetir un codigo mientras una CONDICION SEA CIERTA

# manzanas = 10

# while manzanas > 0:
# 	print('Me estoy comiendo una manzana # ' + str(manzanas))
# 	manzanas -= 1

# # Escribimos STR por que queremos concatenar la primera cadena con el numero (variable manzanas)
# print('Me quede sin manzanas :(')


#El ciclo FOR tiene la palabra reservada for, luego una variable que usaremos para referirnos al elemento en ese momento
# y despues la coleccion que vamos a recorrer, en este caso num a la primera iteracion vale 1, a la segunda 2 a la tercera 3 y asi


# lista_nums = [1, 'igniz', 3, 4.0, 5, 6, 7, True, 9, '@']

# for num in lista_nums:
# 	print(num)

# Podemos tambien poner carateres, cadenas, floats y booleanos en una lista, es decir, podemos usar todos los tipos de datos
# que admite python

# En los ciclos FOR podemos usar las palabras reservadas CONTINUE y BREAK. 
# Con BREAK rompe el ciclo cuando se llega a dicha palabra, por ejemplo:

# Este codigo imprime hasta que la condicion se cumpla, y ahi se detiene ya que despues de la condicion esta el BREAK.

# lista_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in lista_nums:
# 	if num > 5:
# 		break
# 	print(num)

# Si queremos OMITIR una iteracion, por ejemplo queremos todos los numeros menos el 5, usamos la palabra continue, asi:

lista_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista_nums:
	if num == 5:
		continue
	print(num)
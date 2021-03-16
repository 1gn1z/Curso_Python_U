#Ciclo WHILE, para repetir un bloque de código mientras una condición sea cierta

manzanas = 10

while manzanas > 0:
	print('Me estoy comiendo una manzana # ' + str( manzanas))
	manzanas -= 1

print ('Me quedé sin manzanas :(')

#Ciclo FOR, para recorrer los elementos de una colección

lista_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_nums:
	if numero == 5:
		continue
	print(numero)


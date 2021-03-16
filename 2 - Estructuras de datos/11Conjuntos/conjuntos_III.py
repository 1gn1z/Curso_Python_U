# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())

conjunto_b = set(input("Conjunto B: ").split())

# Haciendo los prints asi, despues del while true, nos evitamos tener que mostrar siempre las operaciones despues de ingresar
# los conjuntos, de este modo se muestran antes de introducir los conjuntos.

print("Operaciones que puedes hacer: ")
print("1.- Union")
print("2.- Intersección")
print("3.- Diferencia")
print("4.- Diferencia simétrica")
print("5.- Ver instrucciones")
print("6.- Salir")

"""
while True:
	operacion = int(input(": "))
	if operacion == 1:
		print("La unión de los conjuntos es: ",conjunto_a | conjunto_b)
	elif operacion == 2:
		print("La intersección de los conjuntos es: ",conjunto_a & conjunto_b)
	elif operacion == 3:
		print("La diferencia de los conjuntos es: "conjunto_a - conjunto_b)
	elif operacion == 4:
		print("La diferencia simétrica de los conjuntos es: ",conjunto_a.symmetric_difference(conjunto_b))
	elif operacion == 5:
		print("Operaciones que puedes hacer: ")
		print("1.- Union")
		print("2.- Intersección")
		print("3.- Diferencia")
		print("4.- Diferencia simétrica")
		print("5.- Ver instrucciones")
		print("6.- Salir")
	else:
		break

"""

# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

"""
print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())
"""

# Haciendo los prints asi, despues del while true, nos evitamos tener que mostrar siempre las operaciones despues de ingresar
# los conjuntos, de este modo se muestran antes de introducir los conjuntos.

def ver_instrucciones():
	print("Operaciones que puedes hacer: ")
	print("1.- Union")
	print("2.- Intersección")
	print("3.- Diferencia")
	print("4.- Diferencia simétrica")
	print("5.- Ver instrucciones")
	print("6.- Salir")

print("Bienvenido a los Conjuntos")
print("Introduce los elementos de los conjuntos separados por espacios")
print("Ejemplo: 1 3 5 8 0 2")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())

ver_instrucciones() 	# Antes de entrar al while true debemos mostrar las instrucciones.
while True:
	operacion = int(input(": "))
	if operacion == 1:
		print("Unión")
	elif operacion == 2:
		print("Intersección")
	elif operacion == 3:
		print("Diferencia")
	elif operacion == 4:
		print("Diferencia Simétrica")
	elif operacion == 5:
		ver_instrucciones()
	elif operacion == 6:
		break
	else:
		print("Operación inválida, favor de verificar")

# Podemos hacer la funcion de ver instrucciones simplemente agregando todos los prints de las instrucciones en una funcion.

# La bienvenida la ponemos abajo de nuestra funcion ver_instrucciones

# Ahora, si el usuario pone 5 para ver las instrucciones simplemente llamamos a la funcion.

# Ahora vamos a hacer una funcion con todo el código de la calculadora de conjuntos:

# Definimos una funcion para la UNION DE CONJUNTOS, y lo haremos con la funcion llamada UNION
def union_conjuntos(conjunto_a, conjunto_b):
	#print()
	print("\nLa unión de A y B es:\n",conjunto_a | conjunto_b)
	#print()
# Como lo hacen en el curso con la funcion UNION:
#	print("LA unión de A y B es {}".format(conjunto_a.union(conjunto_b)))


# En el curso se usa la funcion union, pero me parece mas simple hacerlo con el equivalente pipe |
# print("La union de A y B es {}".format(conjunto_a.union(conjunto_b)))

# Vamos a borrar esos prints de la funcion union_conjuntos, simplemente usando la funcion \n, que es la funcion de salto de linea.
# La funcion de salto de linea VA DENTRO DE LAS COMILLAS DE LA CADENA ok :)

# Me le voy a adelantar al profe para ver si me sale bien la interseccion ;)
# LOGRADO :3
# Ya encarrerado le voy a seguir con las demas :)

#		T 	O 	D 	O 	S 	 	L 	O 	G 	R 	A 	D 	O 	S

def interseccion_conjuntos(conjunto_a,conjunto_b):
	print("\nLa interseccion de A y B es:\n", conjunto_a & conjunto_b)
# Como lo hacen en el curso con la funcion UNION:
#	print("LA unión de A y B es {}".format(conjunto_a.intersection(conjunto_b)))

def diferencia_conjuntos(conjunto_b,conjunto_b):
	print("\nLa diferencia de A y B es\n", conjunto_a - conjunto_b)

def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
	print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
	print("Operaciones que puedes hacer: ")
	print("1.- Union")
	print("2.- Intersección")
	print("3.- Diferencia")
	print("4.- Diferencia simétrica")
	print("5.- Ver instrucciones")
	print("6.- Salir")


def calculadora_conjuntos():		# Funcion con todo el código hasta ahora.
	print("Bienvenido a los Conjuntos")
	print("Introduce los elementos de los conjuntos separados por espacios")
	print("Ejemplo: 1 3 5 8 0 2")

	conjunto_a = set(input("Conjunto A: ").split())
	conjunto_b = set(input("Conjunto B: ").split())

	ver_instrucciones()

	while True:
		operacion = int(input(": "))
		if operacion == 1:
			union_conjuntos(conjunto_a, conjunto_b)
		elif operacion == 2:
			interseccion_conjuntos(conjunto_b,conjunto_b)
		elif operacion == 3:
			diferencia_conjuntos(conjunto_a, conjunto_b)
		elif operacion == 4:
			diferencia_simetrica_conjuntos(conjunto_a, conjunto_b)
		elif operacion == 5:
			ver_instrucciones()
		elif operacion == 6:
			break
		else:
			print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# Ahora vamos a hacer la UNION, para esto vamos a definir UNA FUNCION QUE ACEPTARA 2 PARAMETROS:
# Esta funcion quedara en la opcion 1 de nuestro ciclo while

# DIFERENCIA. La diferencia simetrica, la union y la interseccion SON CONMUTATIVAS, EL ORDEN DE LOS FACTORES NO ALTERA EL PRODUCTO.

# En la diferencia es distinto, NO ES LO MISMO TENER 4-1 que 1-4, es decir,
#
# NO ES LO MISMO CONJUNTO A - CONJUNTO B que CONJUNTO B - CONJUNTO A.

# En este caso, debemos darle al usuario la opcion de elegir cual conjunto se restara de cual.


#print("Cual conjunto deseas restar del otro?")
def diferencia_conjuntos(conjunto_a,conjunto_b):
	print("Elige la diferencia a realizar:")
opcion_1 = int(input(("1.- A - B"))
opcion_2 = int(input(("2.- B - A"))
operacion = int(input(": "))
if operacion == 1:
	print("\nLa diferencia de A - B es {}\n".format(conjunto_a.difference(conjunto_b)))
elif operacion == 2:
	print("\nLa diferencia de B - A es {}\n".format(conjunto_b.difference(conjunto_a)))
else:
	print("Opción incorrecta, favor de verificar")
	diferencia_conjuntos(conjunto_a,conjunto_b) 			# Si salta el error del else, le damos al usuario la opcion de elegir de nuevo
																										# asi que llamamos de nuevo a la funcion para que reinicie :)
# LLAVES DE FORMAT ANTES DE SALTO DE LINEA!!!
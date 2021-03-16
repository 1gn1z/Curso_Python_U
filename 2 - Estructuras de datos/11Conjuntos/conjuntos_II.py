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
		print("La unión de los conjuntos es: ",a | b)
	elif operacion == 2:
		print("La intersección de los conjuntos es: ",a & b)
	elif operacion == 3:
		print("La diferencia de los conjuntos es: "a - b)
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

		MAL
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
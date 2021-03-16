# Obtener los sets del usuario, los llamaremos A y B
# Debemos hacer funcion de union
# Debemos hacer funcion de interseccion
# Debemos hacer funcion de diferencia
# Debemos hacer funcion de diferencia simetrica

# CONJUNTOS II hacer interfaz de usuario.

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


ver_instrucciones()
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
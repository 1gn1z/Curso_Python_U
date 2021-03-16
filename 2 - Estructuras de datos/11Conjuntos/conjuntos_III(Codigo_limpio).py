def union_conjuntos(conjunto_a,conjunto_b):
	print("\nLa unión de A y B es\n",conjunto_a | conjunto_b)

def interseccion_conjuntos(conjunto_a, conjunto_b):
	print("\nLa Intersección de A y B es\n",conjunto_a & conjunto_b)

def diferencia_conjuntos(conjunto_a,conjunto_b):
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

def calculadora_conjuntos():
	print("Bienvenido a los Conjuntos")
	print("Introduce los elementos de los conjuntos separados por espacios")
	print("Ejemplo: 1 3 5 8 0 2")

	conjunto_a = set(input("Conjunto A: ").split())
	conjunto_b = set(input("Conjunto B: ").split())

	ver_instrucciones()

	while True:
		operacion = int(input(": "))
		if operacion == 1:
			union_conjuntos(conjunto_a,conjunto_b)
		elif operacion == 2:
			interseccion_conjuntos(conjunto_a,conjunto_b)
		elif operacion == 3:
			diferencia_conjuntos(conjunto_a,conjunto_b)
		elif operacion == 4:
			print(diferencia_simetrica_conjuntos(conjunto_a,conjunto_b))
		elif operacion == 5:
			ver_instrucciones()
		elif operacion == 6:
			break
		else:
			print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# Podemos usar la funcion UNION para devolver la union de los conjuntos, o podemos usar el equivalente (| símbolo PIPE)
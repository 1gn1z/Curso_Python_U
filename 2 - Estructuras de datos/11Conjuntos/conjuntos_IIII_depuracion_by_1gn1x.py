def union_conjuntos(conjunto_a,conjunto_b):
    print("\nLa unión de A y B es\n{}".format(conjunto_a.union(conjunto_b)))

def interseccion_conjuntos(conjunto_a,conjunto_b):
    print("\nLa intersección de A y B es\n{}".format(conjunto_a.intersection(conjunto_b)))


def diferencia_conjuntos(conjunto_a,conjunto_b):
	print("Elige la operación:")
	print("1.- A - B")
	print("2.- B - A")
	try:                                                                                        # Manejo de errores. LISTO :) 
		operacion = int(input(": "))
	except ValueError:
		print("Debes introducir 1 o 2")
		diferencia_conjuntos(conjunto_a, conjunto_b)    # Volvemos a llamar la funcion para que se reinicie si el usuario no eligio 1 o 2
	else:
		if operacion == 1:
			print("\nLa diferencia de A - B es{}\n".format(conjunto_a.difference(conjunto_b)))
		elif operacion == 2:
			print("\nLa diferencia de B - A es{}\n".format(conjunto_b.difference(conjunto_a)))
		else:
			print("Operación inválida, favor de verificar")
			diferencia_conjuntos(conjunto_a, conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
  	print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
    print("Operaciones que puedes realizar: ")
    print("1.- Union")
    print("2.- Intersección")
    print("3.- Diferencia")
    print("4.- Diferencia simétrica")
    print("5.- Ver instrucciones")
    print("6.- Salir")

"""
def despedida():
    print("\nGracias por usar la calculadora de conjuntos!\n")
    print("\n Vuelve pronto :)")
"""

def calculadora_conjuntos():
    print("Bienvenido a los Conjuntos")
    print("Introduce los elementos de los conjuntos separados por espacios")
    print("Ejemplo: 1 3 5 8 0 2")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())

    ver_instrucciones()

    while True:
        try:                                                                                                        # Manejo de errores. LISTO :) 
            operacion = int(input("Operación a realizar: "))
        except ValueError:
            print("Operación incorrecta, favor de verificar")
        else:
            if operacion == 1:
                union_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                print("X")
                print("Y")
                break
            else:
                print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# La ultima cosa que haremos sera darle un mensaje al usuario cuando salga de la aplicacion.
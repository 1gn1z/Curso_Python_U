# Poner 5 vidas (intentos)		# LISTO! v1.2
# Decirle al usuario si se acerca o se aleja del número 		LISTO! v1.0
# Decirle al usuario si quiere continuar, generando un número diferente

# Creamos una funcion principal llamada jugar. (v1.1)

import random		# Libreria que genera aleatoriedad (en este caso necesitamos un numero aleatorio)

def jugar():
	intentos = 0		# La variable de los intentos para el usuario, la inicializamos en 0.
	numero_aleatorio = random.randint(1,10)		# randint genera un rango de números aleatorios, que se especifican en 2 parámetros dentro
																						# del parentesis (a,b), donde a es el inicio del rango de números y b el final del rango

	print("Bievenido a Adivina el número!")
	print()
	print("Estoy pensando en un número del 1 al 10")
	print()
	print("Adivina cual es")
	print()
	print("Solamente tienes 5 intentos")

	while intentos < 5:													# Mientras intentos sea menor que 5 se ejecuta el codigo, cuando intentos es mayor
		adivinanza = int(input("El número es: "))

		if adivinanza == numero_aleatorio:				# Este bloque queda igual hasta el break, es decir, si lo adivina ahi termina.
			print("Adivinaste!!!")
			break
		else:			 																# Pero si no adivina queremos darle al usuario pistas.
			intentos += 1														# Si adivinanza no es iguala numero_aleatorio, se va a sumar 1 a la variable intentos.
			if numero_aleatorio > adivinanza: 			# Si el número aleatorio es mayor que adivinanza (El número que puso el usuario).
				print("Fallaste, mi número es mayor")	# Imprimir, fallaste, mi número es mayor.
			else:																		# Si no, es decir, si no se cumple la condicion significa que el número es menor
	 			print("Fallaste, mi número es menor") # por lo tanto le decimos al usuario que nuestro número es menor.
	print("Se te acabaron los intentos")				# Este mensaje se mostrara cuando el ciclo while se cumpla y deje de ejecutarse. 			
	print("Gracias por jugar :3")
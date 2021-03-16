# Poner 5 vidas (intentos)		# LISTO! v1.2
# Decirle al usuario si se acerca o se aleja del número 		LISTO! v1.0
# Decirle al usuario si quiere continuar, generando un número diferente, tanto si adivinaron como si no. LISTO! v1.3


# Creamos una funcion principal llamada jugar. (v1.1)
# Reducimos la cantidad de condicionales, agregando solo un if, un elif, y un else. (v1.3)

# Decirle al usuario cuantos intentos le quedan		LISTO! (v1.4)
# Manejo de errores!. Que se pongan números
"""
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
"""
"""
	while intentos < 5:									# Mientras intentos sea menor que 5 se ejecuta el codigo, cuando intentos es mayor
		adivinanza = int(input("El número es: "))

		if adivinanza == numero_aleatorio:				# Este bloque queda igual hasta el break, es decir, si lo adivina ahi termina.
			print("Adivinaste!!!")
			break
		else:			 								# Pero si no adivina queremos darle al usuario pistas.
		# Vamos a convertir este else en un elif.
			intentos += 1								# Si adivinanza no es iguala numero_aleatorio, se va a sumar 1 a la variable intentos.
			if numero_aleatorio > adivinanza: 			# Si el número aleatorio es mayor que adivinanza (El número que puso el usuario).
				print("Fallaste, mi número es mayor")	# Imprimir, fallaste, mi número es mayor.
			else:																		# Si no, es decir, si no se cumple la condicion significa que el número es menor
	 			print("Fallaste, mi número es menor") 	# por lo tanto le decimos al usuario que nuestro número es menor.
	print("Se te acabaron los intentos")				# Este mensaje se mostrara cuando el ciclo while se cumpla y deje de ejecutarse. 			
	print("Gracias por jugar :3")

	while intentos < 5:												
		adivinanza = int(input("El número es: "))

		if adivinanza == numero_aleatorio:
			print("Adivinaste!!!")							# Si gano ahi termina el juego, 
			continuar = input("Deseas continuar? si/no ")	# por eso le preguntamos si quiere continuar
			if continuar.lower() == "si":					# Si el usuario pone "si"
				jugar()										# Llamamos la funcion de jugar para que el juego se reinicie
			else:											# Si no, es decir, si no se cumple la condicion if, si NO pone si -
			break 											# Si pone cualquier otra cosa diferente se "si", el juego termina

		elif numero_aleatorio > adivinanza:				# Aqui lo que hicimos es añadir un elif en lugar de un else. 
			print("Fallaste, mi número es mayor")
			#print("Intento {}/5".format(intentos))		# Esto lo que hace es reemplazar las llaves por el intento de esa iteracion
		else:											# Ahora, si el numero no es igual ni es mayor, solo queda que sea menor.
			print("Fallaste, mi número es menor")
			#print("Intento {}/5".format(intentos))		# Exactamente igual que la linea 56
		intentos += 1									# Al final de las condicionales, ya podemos incrementar "intentos" en 1

			# Estos prints(lienas 56 y 59), tienen un error que imprime solo hasta intento 4/5. 
			# Este error pasa por que se aumenta nuestra variable de intentos hasta el final
			# Para corregirlo, tenemos que poner un print DESPUES DEL AUMENTO DE INTENTOS.
			# Para que empieze a contar desde el 1 y no desde el 0
			# El error era que estabamos imprimiendo nuestros intentos ANTES de aumentar el número de intentos.

		print("Intento {}/5".format(intentos))	


	else: 												# Este else PERTENECE AL CICLO WHILE!!!. Todo el codigo que este en el else
														# Se ejecutara cuando termine el ciclo WHILE. Solo se ejecuta SI NO SE SALIO POR
														# UN BREAK, o por una excepcion, es decir, cuando terminen los intentos.
		print("Se te acabaron los intentos :(")
		print("Gracias por jugar :3")

		continuar = input("Deseas continuar? si/no")
		if continuar.lower() == "si"							# continuar.lower() hace que aunq el usuario escriba en mayuscula lo convierte
																							# a minusculas para poder compararlo correctamente.
			jugar()

	jugar()
"""	


# M    A    N    E    J    O        D    E        E    R    R    O    R    E    S

	import random

def jugar():
  intentos = 0

  numero_aleatorio = random.randint(1,10)
  print("Bievenido a Adivina el número!")
  print()
  print("Estoy pensando en un número del 1 al 10")
  print()
  print("Adivina cual es")
  print("Solamente tienes 5 intentos")

  while intentos < 5:

  	try:
    	adivinanza = int(input("El número es: "))		# Si aqui escribimos "cinco", nos mandara un ValueError por que es una
    													# es una cadena y no un entero, debemos manejar los errores con TRY, EXCEPT, ELSE.
    except ValueError:
    	print("Ese no es un número válido, favor de verificar")
    else:

			if adivinanza == numero_aleatorio:									#	C
	      print("Adivinaste!!!")														#	O
	      continuar = input("Deseas continuar? si/no: ")		# D
	      if continuar.lower() == "si":											# I 
	        jugar()																					#	G
	      else:																							# O
	        break 																					#
	    elif numero_aleatorio > adivinanza: 			 					#	I			 
	      print("Fallaste, mi número es mayor")							# D
	    else:																								# E
	      print("Fallaste, mi número es menor")							# N
	 																												# T
	    intentos += 1																				# A
	    print("Intento {}/5".format(intentos))							# D
	    																										# O

  else:
    print("Se te acabaron los intentos :(")      
    print("Gracias por jugar :3")

    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar()

jugar()
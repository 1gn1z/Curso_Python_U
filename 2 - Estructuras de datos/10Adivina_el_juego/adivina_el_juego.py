# Poner 5 vidas (intentos)
# Decirle al usuario si se acerca o se aleja del número
# Decirle al usuario si quiere continuar, generando un número diferente

import random		# Libreria que genera aleatoriedad (en este caso necesitamos un numero aleatorio)

numero_aleatorio = random.randint(1,10)		# randint genera un rango de números aleatorios, que se especifican en 2 parámetros dentro
																					# del parentesis (a,b), donde a es el inicio del rango de números y b el final del rango

print("Bievenido a Adivina el número!")
print()
print("Estoy pensando en un número del 1 al 10")
print()
print("Adivina cual es")

while True:
	adivinanza = int(input("El número es: "))

	if adivinanza == numero_aleatorio:			
		print("Adivinaste!!!")
		break
	else:
		print("Fallaste :( Intenta de nuevo")
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

print("Operaciones que puedes hacer: ")
print("1.- Union")
print("2.- Intersección")
print("3.- Diferencia")
print("4.- Diferencia simétrica")
print("5.- Ver instrucciones")
print("6.- Salir")
while True:
	operacion = int(input(": "))
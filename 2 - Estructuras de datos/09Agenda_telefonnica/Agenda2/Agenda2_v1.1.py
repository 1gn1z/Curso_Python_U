# Agregar un contactos    LISTO! v1.0
# Remover contactos
# Actualizar contactos
# Ver un contactos    LISTO! v1.1
# Ver todos nuestros contactos	LISTO! v1.0

agenda_telefonica = dict()		# Creacion de un diccionario vacio para poner todo lo que necesitamos

print("Bienvenidos a la agenda telefónica de 1gn1z")

def agregar_contacto():
  nombre = input("Nombre del nuevo contacto: ")		# Nombre de la llave
  numero = input("Número del nuevo contacto: ")		# Valor de la llave
  agenda_telefonica[nombre] = numero	# Añadimos una nueva entrada con los corchetes, que contienen la LLAVE, el igual contendra el VALOR de esa llave
  																		# diccionario["llave a añadir"] = valor. Diccionario, entre corchetes la nueva llave
  																		# igual (=), mas el valor de la nueva llave, en este caso lo que tenga la variable número. 
def remover_contacto():
  print("Remover contacto")

def actualizar_contacto():
  print("Actualizar contacto") 

def ver_contacto():
	nombre = input("Nombre del contacto: ")  # Pedimos al usuario el nombre del contacto que quiere ver.
  print(nombre + " - " + agenda_telefonica[nombre]) # Al igual que en ver todo, imprimimos el nombre del contacto,
  # concatenamos un guion para separar, seguido de el valor de ese nombre (llave), para que se muestre llave y valor.

def ver_todo():
  print()
	print("---------------Agenda Telefónica---------------")
	for contacto in agenda_telefonica:		# Iteracion que devuelve (todas) las LLAVES de nuestro diccionario (agenda)
		print(contacto + " - " + agenda_telefonica[contacto])	# Contacto devuelve la LLAVE, mientras que 
	print("-----------------------------------------------")	# agenda_telefonica[contacto], devuelve el VALOR de la llave																											
  print()

# Lo que el ciclo for hace es iterar todas las llaves, luego, imprimimos la llave (contacto), concatenandole un guion, para separar
# y seguidamente extrayendo el VALOR de esa llave, con esta instruccion: (agenda_telefonica[contacto])																													 

while True:
  print("1.- Para agregar contacto")
  print("2.- Para remover un contacto")
  print("3.- Para actualizar un contacto")
  print("4.- Para ver un contacto")
  print("5.- Para ver todos los contactos")
  operacion = int(input("Elige la operación que deseas usar: "))

  if operacion == 1:
  	agregar_contacto()
  elif operacion == 2:
  	remover_contacto()
  elif operacion == 3:
  	actualizar_contacto()
  elif operacion == 4:
  	ver_contacto()
  elif operacion == 5:
  	ver_todo()
  else:						# Else para CUALQUIER otra opcion que NO sean las especificadas en nuestros condicionales if, elif.
  	print("Operación inválida, favor de verificar")

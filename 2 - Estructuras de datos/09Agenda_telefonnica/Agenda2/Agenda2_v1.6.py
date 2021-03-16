# Agregar un contactos    LISTO! v1.0
# Remover contactos   LISTO! v1.2
# Actualizar contactos  LISTO! v1.3
# Ver un contactos    LISTO! v1.1
# Ver todos nuestros contactos	LISTO! v1.0

# Manejo de errores, por ejemplo en las opciones al escribir "cuatro", el programa crashea (ValueError) LISTO! v1.4
# Manejo de errores, por ejemplo remover un contacto que no existe (KeyError) LISTO! v1.5
# Manejo de errores, por ejemplo, ver un contacto que no existe, es exactamente igual al de remover (KeyError) LISTO v1.6


agenda_telefonica = dict()		# Creacion de un diccionario vacio para poner todo lo que necesitamos

print("Bienvenidos a la agenda telefónica de 1gn1z")

def agregar_contacto():
  print()
  nombre = input("Nombre del nuevo contacto: ")		# Nombre de la llave
  numero = input("Número del nuevo contacto: ")		# Valor de la llave
  agenda_telefonica[nombre] = numero	# Añadimos una nueva entrada con los corchetes, que contienen la LLAVE, el igual contendra el VALOR de esa llave
  																		# diccionario["llave a añadir"] = valor. Diccionario, entre corchetes la nueva llave
  																		# igual (=), mas el valor de la nueva llave, en este caso lo que tenga la variable número. 
  print()
  print("---------------Agenda telefónica---------------")
  print()
  print("Contacto agregado correctamente")
  print()
  print("-----------------------------------------------")
  print()                 

def remover_contacto():
  print()
  nombre = input("Nombre del contacto a elimiar: ")
  try:
    del agenda_telefonica[nombre]   # Usamos la palabra reservada DEL, el nombre del diccionario y entre corchetes el elemento a borrar
  except KeyError:  # KeyError para manejar el error de intentar borrar un contacto que no existe
    print()
    print("---------------Agenda telefónica---------------")
    print("Ese contacto no existe")
    print("-----------------------------------------------")
    print()
  else:
    print("---------------Agenda telefónica---------------")
    print("Contacto eliminado correctamente")
    print()
    print("-----------------------------------------------")
    print()

def actualizar_contacto():
  print()
  nombre = input("Nombre del contacto a actualizar: ")
  numero = input("Nuevo número de este contacto: ")
  agenda_telefonica[nombre] = numero    # Aqui el nombre (llave), se actualiza, con el nuevo número (= numero) que el usuario digite
                                        # Exactamente igual que añadir un contacto nuevo (linea 14)
  print()
  print("---------------Agenda telefónica---------------")
  print("Contacto actualizado correctamente")
  print("-----------------------------------------------")
  print()

def ver_contacto():
  print()
  nombre = input("Nombre del contacto: ")  # Pedimos al usuario el nombre del contacto que quiere ver.
  print()
  print("---------------Agenda telefónica---------------")
  try: 
    print(nombre + " - " + agenda_telefonica[nombre])  # Al igual que en ver todo, imprimimos el nombre del contacto,
  # concatenamos un guion para separar, seguido de el valor de ese nombre (llave), para que se muestre llave y valor.
  # Para manejar el error en caso de que consultamos un contacto que no exista. (Igual que para borrar uno inexistente)
  except KeyError:  # El error en sí, de que no exista el contacto. Aqui NO es necesario un ELSE, ya que queremos imprimir
                    # siempre estos prints de aqui abajo del mensaje "Ese contacto no existe".
    print()
    print("Ese contacto no existe")
    print("-----------------------------------------------")
    print()

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
  print("6.- Para salir")

  # TRY, para manejar los errores que pudiera haber si el usuario escribe una cadena o caracter en las opciones (que son del 1 al 6)

  try:        
    operacion = int(input("Elige la operación que deseas usar: "))
  except ValueError:
    print()
    print("Opción inválida, selecciona una opción del 1 al 6")
    print()
  else:
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
    elif operacion == 6:  # Operacion para salir del programa con un BREAK
      break 
    else:						# Else para CUALQUIER otra opcion que NO sean las especificadas en nuestros condicionales if, elif.
    	print("Operación inválida, favor de verificar")

print()
print("Gracias por usar nuestra agenda telefónica :)")
print("Vuelve pronto ;)")
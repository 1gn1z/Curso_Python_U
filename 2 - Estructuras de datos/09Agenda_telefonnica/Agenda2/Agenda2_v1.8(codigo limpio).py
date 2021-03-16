agenda_telefonica = dict()

def imprimir_operacion(nombre_operacion):
  print()
  print("---------------Agenda telefónica---------------")
  print(nombre_operacion)
  print("-----------------------------------------------")
  print()


def agregar_contacto():
  print()
  nombre = input("Nombre del nuevo contacto: ")
  numero = input("Número del nuevo contacto: ")
  agenda_telefonica[nombre] = numero
  imprimir_operacion("Contacto agregado correctamente")


def remover_contacto():
  print()
  nombre = input("Nombre del contacto a eliminar: ")
  nombre_operacion = None

  try:    
    del agenda_telefonica[nombre]
  except KeyError:  
    nombre_operacion = "Ese contacto no existe"
  else:
    nombre_operacion = "Contacto borrado"

  imprimir_operacion(nombre_operacion)


def actualizar_contacto():
  print()
  nombre = input("Nombre del contacto que deseas actualizar: ")
  numero = input("Nuevo número de este contacto: ")
  agenda_telefonica[nombre] = numero
  print()
  print("---------------Agenda telefónica---------------")
  print("Contacto actualizado correctamente")
  print("-----------------------------------------------")
  print()


def ver_contacto():
  nombre = input("Nombre del contacto: ")
  nombre_operacion = None
  try:
    nombre_operacion = "{} - {} ".format(nombre,agenda_telefonica[nombre])
  except KeyError:
    nombre_operacion = "Ese contacto no existe"

  imprimir_operacion(nombre_operacion)


def ver_todo():
  nombre_operacion = None

  if len(agenda_telefonica) == 0:
    nombre_operacion = "No tienes ningun contacto"
  else:
    for contacto in agenda_telefonica:
      if nombre_operacion == None:
        nombre_operacion = "{} - {}".format(contacto,agenda_telefonica[contacto])
      else: 
        nombre_operacion += "\n{} - {}".format(contacto,agenda_telefonica[contacto])

  imprimir_operacion(nombre_operacion)


def iniciar_agenda():
  print("Bienvenidos a la agenda telefónica de 1gn1z")

  while  True:
    print("1.- Para agregar contacto")
    print("2.- Para remover un contacto")
    print("3.- Para actualizar un contacto")
    print("4.- Para ver un contacto")
    print("5.- Para ver todos los contactos")
    print("6.- Para salir")

    try:
      operacion = int(input("Elige la operación que deseas usar: "))
    except ValueError:
      print()
      print("Operación inválida, Selecciona una opción del 1 al 6")
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
      elif operacion == 6:
        break
      else:
        print()
        print("Operación inválida, Selecciona una opción del 1 al 6")


def despedida():
  print()
  print("Gracias por usar nuestra agenda telefónica")
  print("Vuelve pronto ;)")

iniciar_agenda()
despedida()
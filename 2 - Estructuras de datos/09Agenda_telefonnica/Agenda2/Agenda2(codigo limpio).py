agenda_telefonica = dict()

print("Bienvenidos a la agenda telefónica de 1gn1z")

def agregar_contacto():
  print()
  nombre = input("Nombre del nuevo contacto: ")
  numero = input("Número del nuevo contacto: ")
  agenda_telefonica[nombre] = numero
  print()
  print("---------------Agenda telefónica---------------")
  print()
  print("Contacto agregado correctamente")
  print()
  print("-----------------------------------------------")
  print()

def remover_contacto():
  print()
  nombre = input("Nombre del contacto a eliminar: ")

  try:    
    del agenda_telefonica[nombre]
  except KeyError:  
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
  nombre = input("Nombre del contacto que deseas actualizar: ")
  numero = input("Nuevo número de este contacto: ")
  agenda_telefonica[nombre] = numero
  print()
  print("---------------Agenda telefónica---------------")
  print("Contacto actualizado correctamente")
  print("-----------------------------------------------")
  print()

def ver_contacto():
  print()
  nombre = input("Nombre del contacto: ")
  print()
  print("---------------Agenda telefónica---------------")
  try:
    print()
    print(nombre + " - " + agenda_telefonica[nombre])
  except KeyError:
    print("Ese contacto no existe")
    print()
  print("-----------------------------------------------")
  print()

def ver_todo():
  print()
  print("---------------Agenda telefónica---------------")

  if len(agenda_telefonica) == 0:
    print("Agenda vacía")
  else:
    for contacto in agenda_telefonica:
      print(contacto + " - " + agenda_telefonica[contacto])
  print("-----------------------------------------------")
  print()

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
      print()
print()
print("Gracias por usar nuestra agenda telefónica")
print("Vuelve pronto ;)")
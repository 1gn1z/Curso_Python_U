# Agregar Contactos	LISTO!
# Remover Contactos
# Actualizar Contactos
# Ver un contacto
# Ver todos los contactos.	LISTO!

agenda_telefonica = dict()    # Funcion para crear un diccionario en blanco, para ir agregandole lo que ocupemos.

print("------------///1gn1z\\\------------")
print()
print("Bienvenidos a la agenda telefonica")

def agregar_contacto():
  nombre = input("nombre del nuevo contacto: ")
  numero = input("numero del nuevo contacto: ")
  agenda_telefonica[nombre] = numero    # Agenda telefonica tendra una nueva entrada llamada nombre, que sera la LLAVE y le agregamos tambien
                                        # el numero, que sera el valor de la llave
def remover_contacto():
  print("Remover contacto")

def actualizar_contacto():
  print("Actualizar contacto")

def ver_contacto():
  print("Ver contacto")

def ver_todo():
  print()
  print("----------Agenda Telefonica----------")
  for contacto in agenda_telefonica:    # Esto devuelve SOLO los nombres de las llaves, por eso lo imprimimos primero, luego un guion
    print(contacto + " - " + agenda_telefonica[contacto]) # Y despues el numero usando la misma llave para obtener el valor de esa llave
  print("-------------------------------------")
  print()

while True:
  print("1.- Agregar contacto")
  print("2.- Remover contacto")
  print("3.- Actualizar contacto")
  print("4.- Ver un contacto")
  print("5.- Ver todos los contactos")
  operacion = int(input("Operacion a realizar: "))
  
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
  else:
    print("Operacion invalida, favor de verificar")
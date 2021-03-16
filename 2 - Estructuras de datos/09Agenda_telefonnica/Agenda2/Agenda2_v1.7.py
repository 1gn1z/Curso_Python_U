# Agregar un contactos    LISTO! v1.0
# Remover contactos   LISTO! v1.2
# Actualizar contactos  LISTO! v1.3
# Ver un contactos    LISTO! v1.1
# Ver todos nuestros contactos	LISTO! v1.0

# Manejo de errores, por ejemplo en las opciones al escribir "cuatro", el programa crashea (ValueError) LISTO! v1.4
# Manejo de errores, por ejemplo remover un contacto que no existe (KeyError) LISTO! v1.5
# Manejo de errores, por ejemplo, ver un contacto que no existe, es exactamente igual al de remover (KeyError) 

# Ahora, si ponemos ver contactos, y no hay nada simplemente imprime las lineas, pero queremos que mande un mensaje
# como por ejemplo "No hay contactos". Haremos eso :)

# Mejoraremos mas nuestro codigo, en todas nuestras funciones tenemos los prints de nuestra agenda y los guines y otros prints
# para dejar algunos espacios para que se vea mejor, en programacion ODIAMOS repetir cosas si podemos hacerlo mediante una funcion
# Reduciremos un poco nuestra cantidad de prints. Con una nueva funcion llamada "imprimir_operacion", y que acepte un nombre
# como parametro    AGENDA v1.7!!!

# Ya para la version ultima (1.8) solo vamos a crear una funcion que contenga todo el ciclo while, es decir, una funcion
# Para que se inicie la agenda cuando la llamemos
# Y una funcion final que sea la despedida de nuestro programa, una funcion que contenga los ultimos prints donde despedimos
# al usuario.

agenda_telefonica = dict()		# Creacion de un diccionario vacio para poner todo lo que necesitamos

def imprimir_operacion(nombre_operacion): # El parametro "nombre operacion", llevara las opciones: "contacto agregado", 
                                          # "contacto borrado", "ese contacto no existe", etc.
  print()
  print("---------------Agenda telefónica---------------")
  print(nombre_operacion)
  print("-----------------------------------------------")
  print()

def agregar_contacto():
  print()
  nombre = input("Nombre del nuevo contacto: ")		# Nombre de la llave
  numero = input("Número del nuevo contacto: ")		# Valor de la llave
  agenda_telefonica[nombre] = numero	# Añadimos una nueva entrada con los corchetes, que contienen la LLAVE, el igual contendra el VALOR de esa llave
  																		# diccionario["llave a añadir"] = valor. Diccionario, entre corchetes la nueva llave
  																		# igual (=), mas el valor de la nueva llave, en este caso lo que tenga la variable número. 

  imprimir_operacion("Contacto agregado correctamente")   # Con esta línea, nos ahorramos escribir una y otra vez todos los prints                                    
"""                     
Vamos a borrar todo esto, que sera reemplazado por nuestra nueva funcion :) (imprimir_operacion) con su parametro (nombre_operacion)               
  print()
  print("---------------Agenda telefónica---------------")
  print()
  print("Contacto agregado correctamente")      # Este es el nombre de la operacion.
  print()
  print("-----------------------------------------------")
  print()                 
"""
def remover_contacto():
  print()
  nombre = input("Nombre del contacto a elimiar: ")
  nombre_operacion = None   # NONE se usa en python para inicializar una variable que no tenga nada.


  try:
    del agenda_telefonica[nombre]   # Usamos la palabra reservada DEL, el nombre del diccionario y entre corchetes el elemento a borrar
  except KeyError:  # KeyError para manejar el error de intentar borrar un contacto que no existe

    nombre_operacion = "Ese contacto no existe"   # Esta variable ahora lleva el mensaje "Ese contacto no existe".
    # Se llaman igual por que solo se ejecuta una vez, en este caso se ejecutara solo si hay un KeyError.
    # Esta linea reemplaza las lineas de la 71 a la 75
                                                  
  else:
    nombre_operacion = "Contacto eliminado correctamente"   # La misma variable tiene el mensaje "Contacto borrado". Y solo se 
                                                  # ejecuta cuando NO hay el KeyError. 
                                                  # Esta linea reemplaza las lineas de la 76 a la 81
  imprimir_operacion(nombre_operacion)
"""
    print()
    print("---------------Agenda telefónica---------------")
    print("Ese contacto no existe")             # Este es el nombre de la operacion.
    print("-----------------------------------------------")
    print()
  else:
    print("---------------Agenda telefónica---------------")
    print("Contacto eliminado correctamente")   # Este es el nombre de la operacion.
    print()
    print("-----------------------------------------------")
    print()
"""


def actualizar_contacto():
  print()
  nombre = input("Nombre del contacto a actualizar: ")
  numero = input("Nuevo número de este contacto: ")
  agenda_telefonica[nombre] = numero    # Aqui el nombre (llave), se actualiza, con el nuevo número (= numero) que el usuario digite
                                        # Exactamente igual que añadir un contacto nuevo (linea 37)
  imprimir_operacion("Contacto actualizado correctamente")                                      



"""                                      
  print()
  print("---------------Agenda telefónica---------------")
  print("Contacto actualizado correctamente")   # Este es el nombre de la operacion.
  print("-----------------------------------------------")
  print()
"""
def ver_contacto():
  print()
  nombre = input("Nombre del contacto: ")  # Pedimos al usuario el nombre del contacto que quiere ver.
  print()
  print("---------------Agenda telefónica---------------")
  try: 
    nombre_operacion = "{} - {} ".format(nombre,agenda_telefonica[nombre])

  #  print(nombre + " - " + agenda_telefonica[nombre])  # Al igual que en ver todo, imprimimos el nombre del contacto,
  # concatenamos un guion para separar, seguido de el valor de ese nombre (llave), para que se muestre llave y valor.
  # Para manejar el error en caso de que consultamos un contacto que no exista. (Igual que para borrar uno inexistente)
  #except KeyError:  # El error en sí, de que no exista el contacto. Aqui NO es necesario un ELSE, ya que queremos imprimir
                    # siempre estos prints de aqui abajo del mensaje "Ese contacto no existe".
  
  except KeyError:
    nombre_operacion = "Ese contacto no existe"

  imprimir_operacion(nombre_operacion)  

"""
    print()
    print("Ese contacto no existe")
    print("-----------------------------------------------")
    print()
"""

def ver_todo()
  nombre_operacion = None   # Inicializamos la variable en NONE para que no tenga ningun valor inicial.

  if len(agenda_telefonica) == 0:       # Si la longitud del diccionario (agenda_telefonica) es de 0
    nombre_operacion = "Agenda vacía"   # la variable contendra el mensaje "Agenda vacia"  
  else:                                 # Si la condicion IF no se cumple
    for contacto in agenda_telefonica:  # Itera el diccionario extrayendo las llaves (nombres de contactos) del mismo.
      if nombre_operacion == None:      # Volvemos a declarar la variable en NONE para que no se quede con el mensaje anterior (linea 133)
        nombre_operacion = "{} - {}}".format(contacto ,agenda_telefonica[contacto]) # Si llega aqui, el nombre de la operacion
        # Debe mostrar TODOS los contactos, que es lo que hace la funcion.
        # Las llaves {}, contienen el nombre del contacto (llave), seguido del valor de la llave (número) (agenda_telefonica[contacto])
        # FORMAR sirve para trabajar con cadenas, gracias a format podemos ordenarlas en el orden que queramos

      else: # Si la agenda ya tiene algun contacto.
        nombre_operacion += "\n{} - {}".format(contacto ,agenda_telefonica[contacto])
            # nombre_operacion = nombre_operacion + \n para poner el nuevo contacto en una nueva linea
            # e igual las llaves se remmplazan por lo que esta especificado en .format (contacto ,agenda_telefonica[contacto])
  imprimir_operacion(nombre_operacion)

"""
def ver_todo():
  print()
  print("---------------Agenda Telefónica---------------")

  if len(agenda_telefonica) == 0:   # Esta linea indica que si no hay nada (len == 0) muestre el mensaje "Agenda vacía".
    print("Agenda vacía")
  else:                             # Si no, continua normal.
    for contacto in agenda_telefonica:		# Iteracion que devuelve (todas) las LLAVES de nuestro diccionario (agenda)
  	  print(contacto + " - " + agenda_telefonica[contacto])	# Contacto devuelve la LLAVE, mientras que 
  print("-----------------------------------------------")	# agenda_telefonica[contacto], devuelve el VALOR de la llave																											
  print()
"""


# Lo que el ciclo for hace es iterar todas las llaves, luego, imprimimos la llave (contacto), concatenandole un guion, para separar
# y seguidamente extrayendo el VALOR de esa llave, con esta instruccion: (agenda_telefonica[contacto])																													 

print("Bienvenidos a la agenda telefónica de 1gn1z")

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
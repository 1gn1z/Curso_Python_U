# Lista de compras hecha por 1gn1z_el_angel

lista_articulos = list()
print()
print("----------Bienvenidos a la lista de compras----------")
print()

def agregar_articulo():
  print()
  articulo = input("Artículo a agregar: ")
  lista_articulos.append(articulo.capitalize())
  print()
  print("*** Artículo agregado satisfactoriamente ***")
  print()

def remover_articulo():
  print()
  articulo = input("Artículo a remover: ")
  lista_articulos.remove(articulo.capitalize())
  print()
  print("*** Artículo eliminado satisfactoriamente ***")
  print()

def ver_articulos():
  print()
  print("---------------LISTA DE COMPRAS---------------")
  print()
  for articulo in lista_articulos:
    print(articulo.capitalize())
  print()
  print("----------------------------------------------")
while True:
  
  print("Estas son las opciones que puedes realizar:")
  print("1.- Agregar artículo")
  print("2.- Remover artículo")
  print("3.- Ver artículos")
  print("4.- Salir")

  try:
    operacion = int(input("Selecciona una opción: "))
  except (SyntaxError,ValueError,ZeroDivisionError,NameError,TypeError,):
    print()
    print("Opción incorrecta, favor de verificar")
    print()
    continue

  if operacion == 1:
    agregar_articulo()
  elif operacion == 2:
    remover_articulo()
  elif operacion == 3:
    ver_articulos()
  elif operacion == 4:
    break
  else:
    if operacion <1 or operacion >4:
      print()
      print("Opción incorrecta, favor de verificar")
      print()
print()
print("Gracias por usar la lista de compras")
print("Vuelve pronto ;)")
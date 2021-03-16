import random
import msvcrt # Ver ultima linea
# Dificultades
# Facil: Asi como lo tenemos
# Media: Aumentar rango de numeros del 1 al 40
# Dificil: Reducir numero de intentos a 4 
# Dios: Rango del 1 al 100 con 3 intentos xD

#RETO CUMPLIDO!!! Programa hecho por 1gn1z_el_angel

def jugar_facil():
  intentos = 0

  numero_aleatorio = random.randint(1,10)
  print()
  print("BIENVENIDO A ADIVINA EL NÚMERO!!!")
  print()
  print("Estoy pensando en un número del 1 al 10...")
  print()
  print("Adivina cual es!")
  print()
  print("Solamente tienes 5 intentos!!!")
  print()
  while intentos < 5:
    try:
      adivinanza = int(input("El número es: "))
    except ValueError:
      print("Ese no es un número válido, favor de verificar")
    else:
      if adivinanza == numero_aleatorio:      
        print("Adivinaste!!!")
        continuar = input("Deseas continuar? si/no: ")
        if continuar.lower() == "si":
          jugar_facil()
        else:
          break
      elif numero_aleatorio > adivinanza:                         
        print()
        print("Fallaste, mi número es mayor") 
        print()
      else:      
        print()                           
        print("Fallaste, mi número es menor")

      intentos += 1
      print("Intento {}/5".format(intentos))
      
  else:
    print()
    print("Se te acabaron los intentos :(")   
    print("Gracias por jugar :3")
    print()
    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_facil()


def jugar_media():
  intentos = 0

  numero_aleatorio = random.randint(1,40)
  print()
  print("BIENVENIDO A ADIVINA EL NÚMERO!!!")
  print()
  print("Estoy pensando en un número del 1 al 40...")
  print()
  print("Adivina cual es!")
  print()
  print("Solamente tienes 5 intentos!!!")
  print()

  while intentos < 5:
    try:
      adivinanza = int(input("El número es: "))
    except ValueError:
      print("Ese no es un número válido, favor de verificar")
    else:
      if adivinanza == numero_aleatorio:      
        print("Adivinaste!!!")
        continuar = input("Deseas continuar? si/no: ")
        if continuar.lower() == "si":
          jugar_media()
        else:
          break
      elif numero_aleatorio > adivinanza:
        print()                          
        print("Fallaste, mi número es mayor") 
        print()
      else:       
        print()                          
        print("Fallaste, mi número es menor")
  
      intentos += 1
      print("Intento {}/5".format(intentos))
      
  else:
    print()
    print("Se te acabaron los intentos :(")      
    print("Gracias por jugar :3")
    print()

    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_media()


def jugar_dificil():
  intentos = 0

  numero_aleatorio = random.randint(1,40)
  print()
  print("BIENVENIDO A ADIVINA EL NÚMERO!!!")
  print()
  print("Estoy pensando en un número del 1 al 40...")
  print()
  print("Adivina cual es!")
  print()
  print("Solamente tienes 4 intentos!!!")
  print()

  while intentos < 4:
    try:
      adivinanza = int(input("El número es: "))
    except ValueError:
      print("Ese no es un número válido, favor de verificar")
    else:
      if adivinanza == numero_aleatorio:      
        print("Adivinaste!!!")
        continuar = input("Deseas continuar? si/no: ")
        if continuar.lower() == "si":
          jugar_dificil()
        else:
          break
      elif numero_aleatorio > adivinanza:
        print()                          
        print("Fallaste, mi número es mayor") 
        print()
      else:             
        print()                    
        print("Fallaste, mi número es menor")
  
      intentos += 1
      print("Intento {}/4".format(intentos))
      
  else:
    print()
    print("Se te acabaron los intentos :(")      
    print("Gracias por jugar :3")
    print()

    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_dificil()

def jugar_dios():
  intentos = 0

  numero_aleatorio = random.randint(1,100)
  print()
  print("BIENVENIDO A ADIVINA EL NÚMERO!!!")
  print()
  print("Estoy pensando en un número del 1 al 100...")
  print()
  print("Adivina cual es!")
  print()
  print("Solamente tienes 3 intentos!!!")
  print()

  while intentos < 3:
    try:
      adivinanza = int(input("El número es: "))
    except ValueError:
      print("Ese no es un número válido, favor de verificar")
    else:
      if adivinanza == numero_aleatorio:      
        print("Adivinaste!!!")
        continuar = input("Deseas continuar? si/no: ")
        if continuar.lower() == "si":
          jugar_dios()
        else:
          break
      elif numero_aleatorio > adivinanza:
        print()                           
        print("Fallaste, mi número es mayor") 
        print()
      else:                   
        print()              
        print("Fallaste, mi número es menor")
  
      intentos += 1
      print("Intento {}/3".format(intentos))
      
  else:
    print()
    print("Se te acabaron los intentos :(")      
    print("Gracias por jugar :3")
    print()
    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_dios()

while True:
  print("Estas son las dificultades del juego:")
  print("1.- Para Fácil")
  print("2.- Para Media")
  print("3.- Para Díficil")
  print("4.- Para Dios") 
  try:
    print()
    dificultad = int(input("Elige una dificultad: "))
  except ValueError:
    print("Opción incorrecta favor de verificar")
  else:
    if dificultad <1 or dificultad > 4:
      print("pción incorrecta favor de verificar")
    elif dificultad == 1:
      jugar_facil()
    elif dificultad == 2:
      jugar_media()
    elif dificultad == 3:
      jugar_dificil()
    elif dificultad == 4:
      jugar_dios()
  break
msvcrt.getch() # El programa se queda esperando una pulsacion de teclado para salir.
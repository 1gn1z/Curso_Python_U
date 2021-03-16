import random
import msvcrt # Ver ultima linea
# Dificultades
# Facil: Asi como lo tenemos
# Media: Aumentar rango de numeros del 1 al 40
# Dificil: Reducir numero de intentos a 4 
# Dios: Rango del 1 al 100 con 3 intentos xD

#RETO CUMPLIDO!!! Programa hecho por 1gn1z_el_angel

print(" ____ ___ _____ _   ___     _______ _   _ ___ ____   ___  _ ")
print("| __ )_ _| ____| \ | \ \   / / ____| \ | |_ _|  _ \ / _ \| |")
print("|  _ \| ||  _| |  \| |\ \ / /|  _| |  \| || || | | | | | | |")
print("| |_) | || |___| |\  | \ V / | |___| |\  || || |_| | |_| |_|")
print("|____/___|_____|_| \_|  \_/  |_____|_| \_|___|____/ \___/(_)")
print()
print("            _ _       _                    _                                        _ ")
print("   __ _  __| (_)_   _(_)_ __   __ _    ___| |  _ __  _   _ _ __ ___   ___ _ __ ___ | |")
print("  / _` |/ _` | \ \ / / | '_ \ / _` |  / _ \ | | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \| |")
print(" | (_| | (_| | |\ V /| | | | | (_| | |  __/ | | | | | |_| | | | | | |  __/ | | (_) |_|")
print("  \__,_|\__,_|_| \_/ |_|_| |_|\__,_|  \___|_| |_| |_|\__,_|_| |_| |_|\___|_|  \___/(_)")

def jugar_facil():
  intentos = 0

  numero_aleatorio = random.randint(1,10)
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
        print()      
        print("     _    ____ _____     _____ _   _    _    ____ _____ _____ _ ")
        print("    / \  |  _ \_ _\ \   / /_ _| \ | |  / \  / ___|_   _| ____| |")
        print("   / _ \ | | | | | \ \ / / | ||  \| | / _ \ \___ \ | | |  _| | |")
        print("  / ___ \| |_| | |  \ V /  | || |\  |/ ___ \ ___) || | | |___|_|")
        print(" /_/   \_\____/___|  \_/  |___|_| \_/_/   \_\____/ |_| |_____(_)")
        print()
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
    print("S  e    t  e    a  c  a  b  a  r  o  n    l  o  s    i  n  t  e  n  t  o  s    :  (")   
    print()
    print(" _____                _                                        _                        _ ")
    print("|  __ \              (_)                                      (_)                      | |")
    print("| |  \/_ __ __ _  ___ _  __ _ ___      _ __   ___  _ __        _ _   _  __ _  __ _ _ __| |")
    print("| | __| '__/ _` |/ __| |/ _` / __|    | '_ \ / _ \| '__|      | | | | |/ _` |/ _` | '__| |")
    print("| |_\ \ | | (_| | (__| | (_| \__ \    | |_) | (_) | |         | | |_| | (_| | (_| | |  |_|")
    print(" \____/_|  \__,_|\___|_|\__,_|___/    | .__/ \___/|_|         | |\__,_|\__, |\__,_|_|  (_)")
    print("                                      | |                    _/ |       __/ |             ")
    print("                                      |_|                   |__/       |___/     ")
    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_facil()


def jugar_media():
  intentos = 0

  numero_aleatorio = random.randint(1,40)
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
        print()   
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
    print()   
    print("Gracias por jugar :3")
    print()

    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_media()


def jugar_dificil():
  intentos = 0

  numero_aleatorio = random.randint(1,40)
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
        print()      
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
    print()     
    print("Gracias por jugar :3")
    print()

    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_dificil()

def jugar_dios():
  intentos = 0

  numero_aleatorio = random.randint(1,100)
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
        print()   
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
    print()     
    print("Gracias por jugar :3")
    print()
    continuar = input("Deseas continuar? si/no: ")
    if continuar.lower() == "si":
      jugar_dios()

while True:
  print(" ____________________________")
  print("|  ________________________  |")
  print("| |                        | |")
  print("| |  Elige una dificultad: | |")
  print("| |                        | |")
  print("| |    1.-Para Fácil       | |")
  print("| |                        | |")
  print("| |    2.-Para Media       | |")
  print("| |                        | |")
  print("| |    3.-Para Díficil     | |")
  print("| |                        | |")
  print("| |    4.-Para Dios        | |")
  print("| |________________________| |")
  print("|____________________________|")
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


print(" _____                _                                        _                        _ ")
print("|  __ \              (_)                                      (_)                      | |")
print("| |  \/_ __ __ _  ___ _  __ _ ___      _ __   ___  _ __        _ _   _  __ _  __ _ _ __| |")
print("| | __| '__/ _` |/ __| |/ _` / __|    | '_ \ / _ \| '__|      | | | | |/ _` |/ _` | '__| |")
print("| |_\ \ | | (_| | (__| | (_| \__ \    | |_) | (_) | |         | | |_| | (_| | (_| | |  |_|")
print(" \____/_|  \__,_|\___|_|\__,_|___/    | .__/ \___/|_|         | |\__,_|\__, |\__,_|_|  (_)")
print("                                      | |                    _/ |       __/ |             ")
print("                                      |_|                   |__/       |___/     ")  
print()
print()
print()
print("██╗  ██╗███████╗ ██████╗██╗  ██╗ ██████╗     ██████╗  ██████╗ ██████╗      ██╗ ██████╗ ███╗   ██╗ ██╗███████╗")
print("██║  ██║██╔════╝██╔════╝██║  ██║██╔═══██╗    ██╔══██╗██╔═══██╗██╔══██╗    ███║██╔════╝ ████╗  ██║███║╚══███╔╝")
print("███████║█████╗  ██║     ███████║██║   ██║    ██████╔╝██║   ██║██████╔╝    ╚██║██║  ███╗██╔██╗ ██║╚██║  ███╔╝ ")
print("██╔══██║██╔══╝  ██║     ██╔══██║██║   ██║    ██╔═══╝ ██║   ██║██╔══██╗     ██║██║   ██║██║╚██╗██║ ██║ ███╔╝  ")
print("██║  ██║███████╗╚██████╗██║  ██║╚██████╔╝    ██║     ╚██████╔╝██║  ██║     ██║╚██████╔╝██║ ╚████║ ██║███████╗")
print("╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝╚══════╝")
print()
print("Presiona una tecla para salir")
msvcrt.getch() # El programa se queda esperando una pulsacion de teclado para salir.
import random

def jugar():
    intentos = 0

    numero_aleatorio = random.randint(1,10)
    print("Bievenido a Adivina el número!")
    print()
    print("Estoy pensando en un número del 1 al 10")
    print()
    print("Adivina cual es")
    print("Solamente tienes 5 intentos")

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
                    jugar()
                else:
                    break
            elif numero_aleatorio > adivinanza:                                                                                                     
                print("Fallaste, mi número es mayor")        
            else:                                                                                                                                        
                print("Fallaste, mi número es menor")
    
            intentos += 1
            print("Intento {}/5".format(intentos))
            
    else:
        print("Se te acabaron los intentos :(")            
        print("Gracias por jugar :3")

        continuar = input("Deseas continuar? si/no: ")
        if continuar.lower() == "si":
            jugar()

jugar()
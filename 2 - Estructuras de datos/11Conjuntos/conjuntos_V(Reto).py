def union_conjuntos(conjunto_a,conjunto_b):
    print("\nLa unión de A y B es\n{}".format(conjunto_a.union(conjunto_b)))

def interseccion_conjuntos(conjunto_a,conjunto_b):
    print("\nLa intersección de A y B es\n{}".format(conjunto_a.intersection(conjunto_b)))

def diferencia_conjuntos(conjunto_a,conjunto_b):
    print("Elige la operación:")
    print("1.- A - B")
    print("2.- B - A")
    try:                                                                                                                                                                                # Manejo de errores. LISTO :) 
        operacion = int(input(": "))
    except ValueError:
        print("Debes introducir 1 o 2")
        diferencia_conjuntos(conjunto_a, conjunto_b)        # Volvemos a llamar la funcion para que se reinicie si el usuario no eligio 1 o 2
    else:
        if operacion == 1:
            print("\nLa diferencia de A - B es{}\n".format(conjunto_a.difference(conjunto_b)))
        elif operacion == 2:
            print("\nLa diferencia de B - A es{}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print("Operación inválida, favor de verificar")
            diferencia_conjuntos(conjunto_a, conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    print("\nLa diferencia simétrica de A y B es\n", conjunto_a.symmetric_difference(conjunto_b))

def ver_instrucciones():
    print("Operaciones que puedes realizar: ")
    print("1.- Union")
    print("2.- Intersección")
    print("3.- Diferencia")
    print("4.- Diferencia simétrica")
    print("5.- Ver instrucciones")
    print("6.- Insertar nuevos conjuntos")
    print("7.- Salir")

def despedida():
    print("\nGracias por usar la calculadora de conjuntos!")
    print("\nVuelve pronto :)")

#def insertar_nuevos_conjuntos(conjunto_a,conjunto_b):
#    calculadora_conjuntos()     # Lo logre por casualidad xD. Lo que pasa es que esta funcion inicia de nuevo el programa
                                # de nuevo, tomando los nuevos conjuntos introducidos y reemplazandolos :)
                                # hay un problema :(, si reemplazamos, al salir, pide la operacion a realizar, y hay que
                                # insertar 7 OTRA VEZ para que el programa termine :(
                               
#def insertar_nuevos_conjuntos(conjunto_a,conjunto_b):

def calculadora_conjuntos():
    print("Bienvenido a los Conjuntos")
    print("Introduce los elementos de los conjuntos separados por espacios")
    print("Ejemplo: 1 3 5 8 0 2")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())

    ver_instrucciones()

    while True:
        try:                                                                                                                                                                                                                # Manejo de errores. LISTO :) 
            operacion = int(input("Operación a realizar: "))
        except ValueError:
            print("Operación incorrecta, favor de verificar")
        else:
            if operacion == 1:
                union_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                calculadora_conjuntos() # Reiniciamos el programa llamando nuevamente la funcion principal. Que toma los nuevos conjuntos
                break                   # Con el break terminamos el programa, sin que se reinicie y tengamos que poner 2 veces 7 (salir)
            elif operacion == 7:
                despedida()
                break
            else:
                print("Operación inválida, favor de verificar")

calculadora_conjuntos()

# La ultima cosa que haremos sera darle un mensaje al usuario cuando salga de la aplicacion.

# RETO!!!
# Tratar de crashear el programa.
# Puede que el usuario quiera poner otros conjuntos diferentes sin salir de la aplicacion.

# Poner una nueva operacion donde le digamos al usuario algo como "insertar nuevos conjuntos"
# El profe como que no explica bien xd, lo que entendi es que hay que poder REEMPLAZAR los conjuntos por unos nuevos para experimentar

# RETO LOGRADO!!! :)
# Simplemente volvemos a llamar la funcion principal que reinicia el programa y ponemos un break para que termine
# y no vuelva a pedir una vez mas la operacion antes de salir.


# Quien sabe que pedo, al hacer todas las operaciones que NO eran UNION (interseccion, diferencia y diferencia simetrica)
# me arrojaba simplemente "set()". NO mandaba error ni nada, simplemente imprimia eso.

# Lo corregi en el archivo "conjuntos_V(Reto_2).py".
# Lo que hice fue simplemente usar sus EQUIVALENTES en lugar del codigo ofuscado con .format bla bla bla, funciona bien :)

# UNION:                    conjunto_a | conjunto_b
# INTERSECCION:             conjunto_a & conjunto_b
# DIFERENCIA:               conjunto_a - conjunto_b o conjunto_b - conjunto:a
# DIFERENCIA SIMETRICA:     conjunto_a.symmetric_difference(conjunto_b)
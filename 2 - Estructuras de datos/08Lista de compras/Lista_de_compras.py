# Para nuestra lista debemos poder:

# Agregar articulos
# Remover articulos
# Ver articulos

# lista_de_compras = list()
# Podemos crear la lista tambien asi: lista_de_compras = list()
# Esta forma es mas sencilla cuando creamos una lista vacia

lista_articulos = list()

# Definicion de las funciones:

def agregar_articulo():     #Funcion que NO espera ningun parametro
    articulo = input("Nombre del articulo a agregar: ")
    lista_articulos.append(articulo)    # Añadimos a la lista el articulo que se ingrese y guarde en la variable articulo

def remover_articulo():     #Funcion que NO espera ningun parametro
    print("Remover articulo")

def ver_articulos():        #Funcion que NO espera ningun parametro
    for articulo in lista_articulos:    # Ciclo for para recorrer la lista_articulos
        print(articulo)                 # Imprimir en pantalla el (los) articulos ingresados

print("Bienvenido a la lista de compras!")
print()
while True:
    print("Estas son las operaciones que puedes realizar: ")
    print("1.- Para agregar articulo")
    print("2.- Para remover articulo")
    print("3.- Para ver articulos")
    print("4.- Para salir")
    operacion = int(input("Elige la operacion que deseas utilizar: "))  #Convertir a entero por que la funcion
                                                                        # INPUT SIEMPRE DEVUELVE UN STRING ok :)

# Ahora vamos a hacer con CONDICIONALES, que haga determinada accion dependiendo de las opeciones que tenemos:
# Ademas, vamos a añadir las funciones para cada cosa:

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else: #operacion == 4:   Podemos asumir que la unica opcion restante es la 4, el else no lleva nada
        break   #break para salir del ciclo while.
print("Gracias por usar la lista de compras!!!")
print()
print("Vuelve pronto ;)")
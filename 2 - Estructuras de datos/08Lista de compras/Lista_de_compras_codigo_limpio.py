lista_articulos = list()



def agregar_articulo():     
    print()     
    articulo = input("Nombre del articulo a agregar: ")
    lista_articulos.append(articulo)   
    print("Articulo Agregado")         
    print()

def remover_articulo():     
    print("Remover articulo")

def ver_articulos():   
    print()
    print("----------Articulos Agregados----------")     
    for articulo in lista_articulos:    
        print(articulo)  
    print("_______________________________________")
    print()               

print("Bienvenido a la lista de compras!")
print()
while True:
    print("Estas son las operaciones que puedes realizar: ")
    print("1.- Para agregar articulo")
    print("2.- Para remover articulo")
    print("3.- Para ver articulos")
    print("4.- Para salir")
    operacion = int(input("Elige la operacion que deseas utilizar: "))  


    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else: 
        break  
print("Gracias por usar la lista de compras!!!")
print()
print("Vuelve pronto ;)")
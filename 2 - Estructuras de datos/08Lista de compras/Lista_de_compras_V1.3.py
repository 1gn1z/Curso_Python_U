lista_articulos = list()

def agregar_articulo():   
    print()    
    articulo = input("Nombre del articulo a agregar: ")
    lista_articulos.append(articulo.capitalize())   
    print("Articulo Agregado")     
    print()

def remover_articulo():    
    print()
    articulo = input("Nombre del articulo a remover: ")
    print()
    lista_articulos.remove(articulo.capitalize())
    print("Articulo removido satisfactoriamente")
    print()

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

# En este punto nuestra lista ya agrega elementos, ya remueve elementos, ya podemos ver los elementos y salir de
#nuestra lista

# Pero normalmente la aplicacion nos ayuda a que la primera letra sea MAYUSCULA, esto es una convencion y se ve un poco mejor.
# Para que la primera letra sea mayuscula, es decir capitalizada, se usa una FUNCION llamada precisamente asi, CAPITALIZE.

# Lo primero que haremos sera agregar la funcion CAPITALIZE en la siguiente linea:

#    lista_articulos.append(articulo)   

# Quedara asi:

#    lista_articulos.append(articulo.capitalize())   
# Lo hacemos aqui por que es aqui donde se guarda el articulo que el usuario va a escribir.

# Tambien tenemos que capitalizar la siguiente linea:
#lista_articulos.remove(articulo)

# Ya que si no lo hacemos, nos mandara un error, que es el siguiente:

#   ValueError: list.remove(x): x not in list

# Esto indica que la x en list.remove no existe, ya que NO esta capitalizado al iguak que en la linea donde se agrega el articulo a la lista.

# Podemos capitalizar el articulo en la linea de REMOVE o simplemente podemos dejar todo sin capitalizar.

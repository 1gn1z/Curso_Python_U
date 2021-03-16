# Vamos a implementar nuestro menu, nuestro DICCIONARIO ORDENADO

# Para desplegar los items de un diccionario ordenado, lo hacemos de forma muy similar a los diccionarios normales.

# Vamos a nuestra funcion de menu:


def menu_loop():
    """Show menu"""


# Vamos a añadir una variable, llamada "CHOICE", (opcion), y de valor tendra "NONE" (ninguno).


def menu_loop():
    """Show menu"""
    choice = "None"

# Como NO PODEMOS INICIALIZAR UNA VARIABLE SIN NINGUN VALOR, la mejor opcion es ponerle NONE, NADA.

# Despues usaremos un CICLO WHILE, que dira que MIENTRAS LA OPCION NO SEA Q (QUIT), vamos a desplegar nuestro menu

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':


# Y dentro del ciclo WHILE, vamos a añadir un CICLO FOR, que iterara las LLAVES (KEYS), y el VALOR (VALUE) de esas llaves:
# Obviamente iterara los datos (elementos) del diccionario ordenado:

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':
        for key, value in menu_items.items()    # Pero se ve repetitivo menu_items.items()|
#                                                                                         |  
#                                                                                         |
# Para acceder a los items de un diccionario ordenado, usamos el metodo ITEMS           Asi que renombraremos el diccionario       
#                                                                                       Ordenado de "menu_items", a simplemente "menu"

# Asi quedara simplemente:

        for key, value in menu.items()    

# Despues ponemos un PRINT (Justo antes del ciclo FOR), que diga "press q to quit"

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':
        print('Press "q" to quit')
        for key, value in menu.items()


# Ahora pondremos un print, que contendra la llave y el valor:


def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':
        print('Press "q" to quit')
        for key, value in menu.items()
            print(f'{key} {value}')


# Ya que tenemos nuestro menu desplegado, obtendremos la entrada del usuario: (queda al mismo nivel que el ciclo for)

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':
        print('Press "q" to quit')
        for key, value in menu.items()
            print(f'{key} {value}')
        choice = input('Action: ')


# Y al input que sera la opcion le vamos a pasar la funcion LOWER, para que todo lo que nos de el usuario
# AUTOMATICAMENTE se vuelva minuscula:        

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':
        print('Press "q" to quit')
        for key, value in menu.items()
            print(f'{key} {value}')
        choice = input('Action: ').lower().strip()      # <<<--- Lo que el usuario eliga automaticamente se volverá minusculas


# Y despues le vamos a pasar otro parametro llamado STRIP, que devuelve una copia de la cadena CON LOS ESPACIOS REMOVIDOS 
# (Tanto los espacios de antes como los espacios despues de la cadena)


# Ya tenemos la eleccion del usuario :D, Ahora vamos a ejecutarla



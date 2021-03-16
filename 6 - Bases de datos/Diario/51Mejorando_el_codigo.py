# Vamos a mejorar la interfaz de nuestro diario.

# Cuando vemos una entrada del diario, NO hay espacios ni arriba ni abajo, casi no se puede distinguir.


Action: v
15/08/2020 Saturday  12:18AM
----------------------------
Olakase :3
n) next entry
d) delete entry
q) return to menu
Action: n
14/08/2020 Friday  12:10AM
--------------------------
Olakmira
n) next entry
d) delete entry
q) return to menu
Action:
    

# Como vemos se hace un desmadre y no se entiende bien, no se distingue bien del texto y las operaciones que podemos realizar.

# Vamos a hacer unos separadores que sean del mismo tamaño que los que ya tenemos

# Despues de imprimir el contenido de la entrada, vamos a usar otro print despues de la misma (En la funcion "view_entries"):


        print('-'*len(timestamp))
        print(entry.content)
        print('-'*len(timestamp))       # <<<--- Otro separador para que se vea mejor la interfaz
        

# Y justo antres de ese print, pondremos otro que sea un espacio de distancia como separacion        




        print('-'*len(timestamp))
        print('\n')                         # <<<--- Espacios en blanco para que no se vea tan amontonado
        print(entry.content)
        print('\n')                         # <<<--- Espacios en blanco para que no se vea tan amontonado
        print('-'*len(timestamp))   
        
        

# Ahora, igual en la funcion de "view_entries", En la variable "next_action", vamos a indicarle al usuario en el input
# las opciones que puede elegir        


        next_action = input('Action: [Ndq] ').lower().strip()


# Tambien vamos a agregar unos prints para separar el texto de esta linea en 2:

    print("Enter your toughts. Press ctrl + Z on Windows or ctrl + D on Mac to finish")


# Podemos usar un caracter de escape para salto de linea (\n). Pero en esta ocacion vamos a hacer simplemente otro print.


print('Enter your toughts.')
print('Press ctrl + Z on Windows or ctrl + D on Mac to finish.')



# Ahora vamos a dejar dos espacion entre todas las funciones.
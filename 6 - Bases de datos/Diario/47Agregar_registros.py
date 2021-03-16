# Vamos a añadir una entrada a nuestro diario :D 

# Lo primero que haremos sera importar una libreria llamada SYS

import sys

# SYS contiene una utilidad muy completa para obtener una entrada del usuario, mejor que un input para datos muy grandes.


# Ahora vamos a nuestra funcion add entry:

def add_entry():
    """Add entry"""


# Primero obtendremos lo que el usuari quiera poner, primero haremos un print y le diremos un mensaje:

def add_entry():
    """Add entry"""
    print("Enter your thoughts. Press ctrl + D to finish")    
    

# Lo que usaremos de la libreria SYS es el STDIN, la ENTRADA ESTANDAR DEL SISTEMA (Teclado).

# Y dejara de grabar los datos que el usuario ingrese con su teclado, cuando REGISTRE EL EOF (END OF FILE).

# EL EOF es un caracter especial, que registra CUANDO SE TERMINO DE ESCRIBIR UN TEXTO

# Para ponerlo con nuestro teclado se tiene que poner CTRL + D ESPECIFICAMENTE, no se puede poner de ninguna otra manera.

# Todo lo que el usuario pone, incluidos espacios y todo, cuenta como su entrada.
# Cuando el usuario quiera terminar, tiene que poner ctrl + d, que es el MARCADOR DE FIN DE ARCHIVO.


# Ahora haremos una variable, llamada "data", y pondremos, despues del igual (Asignacion) SYS, por que queremos algo de sys

data = sys

# Y despues agregamos PUNTO STDIN, que es una abrevacion de STandard INput, osea, ENTRADA ESTANDAR DEL SISTEMA, osea el TECLADO.

data = sys.stdin

# Y al metodo STDIN le vamos a agregar PUNTO READ, Es decir, vamos a LEER algo, que es lo que escriba el usuario.

data = sys.stdin.read()


# Y finalmente le agregamos el metodo STRIP, para borrar todos los espacios extra, tanto adelante como atras.

data = sys.stdin.read().strip()


# Ya que tenemos la info, tenemos que decirle al usuario si esta seguro y si realmente puso info.
# No queremos entradas vacias en nuestro diario.

# Asi que primero comprobaremos que nuestra variable DATA en efecto tenga algo, lo unico que haremos sera un if.

if data:
    
# Este IF SOLO PASARA SI DATA TIENE ALGO QUE NO SEA NONE (Que no est vacia).

# Luego otro IF, que tendra un input, que sera un mensaje al usuario si desea guardar la entrada: 

if data:
    if input("Do you want to save your entry? [Yn] ")

# Ahora validaremos este if, si la RESPUESTA ES DIFERENTE DE "n", Vamos a guardar la entrada.

if data:
    if input("Do you want to save your entry? [Yn] ") != 'n':

# Recordar CONVERTIR todas las letras a minusculas y strip para eliminar los espacios antes y despues

if data:
    if input("Do you want to save your entry? [Yn] ").lower().strip() != 'n':


"""# Vamo' a intentar guardar la entrada :D.

# Lo primero que tenemos que hacer es CREAR LAS TABLAS:

db.create_tables([Entry],safe=True)


# Y luego tendriamos que guardar el registro, creando UNA NUEVA INSTANCIA DE NUESTRA CLASE (MODELO)

new_entry = Entry()


# Y tenemos que AÑADIR LOS DATOS (CAMPOS, ATRIBUTOS) dentro de la nueva instancia:

#new_entry = Entry(content=data)    MAL :("""


# Creacion con metodo abreviado (Mas facil ;) de la instancia (tabla) "Entry"

Entry.create(content=data)

# Ahora, si la entrada fue creada satisfactoriamente crearemos un PRINT:

print("Your entry was saves succesfully")



"""NOTA!!! ME REPETIA SIN PARAR LAS OPCIONES POR QUE TENIA ESE PARENTESIS EN EL MENU, CUANDO TENDRIA QUE HABER ESTADO EN LA FUNCION
DEL MENU_LOOP"""

menu = OrderedDict([
    ('a)', add_entry),
    ('v)', view_entries),
    ('d)', delete_entry)
    
"""ASI NUNCA IBA ENTRAR POR QUE TENDRIA QUE HABER PUESTO a), y solo queremos poner: a, CORRECCION!!!!!!:""" 
   
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('d', delete_entry)
    
    
# Ahora si ejecutamos el programa e ingresamos 'a', ya podemos escribir.


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos\Diario>Dear_diary.py
Press 'q' to quit
a) Add entry
v) View all entries
d) Delete an entry
Action: a
Enter your toughts. Press ctrl + D to finish
Olakase.

La entrada de datos NO se interrumpe cuando presionamos ENTER

bye.    


# PERO! si presionamos ctrl + d NO termina, simplemente muestra esto:

^D

# El problema aqui, con el EOF en windows.

# en MAC para detectar el EOF SI SE ESCRIBE CTRL + D.


# PERO PARA QUE SE DETECTE EL EOF EN WINDOWS:

# 1o- Tenemos que TERMINAR DE ESCRIBIR Y BRINCAR A UNA NUEVA LINEA COMPLETAMENTE VACIA:


Action: a
Enter your toughts. Press ctrl + D to finish
Olakmira
                        # <<<--- LINEA VACIA
                        

# 2o- PRESIONAR CTRL + Z.      


Action: a
Enter your toughts. Press ctrl + D to finish
Olakmira
^Z                  


# 3o- PRESIONAR ENTER


Action: a
Enter your toughts. Press ctrl + D to finish
Olakmira
^Z
Do you want to save your entry? [Yn]        # <<<--- Al presionar ENTER despues de ctrl + z ya devuelve lo que programamos


# **********************        EN WINDOWS EL EOF ES, EN UNA NUEVA LINEA, CTRL + Z!!!     **********************


# Guardamos una entrada de prueba y vamos a ver si de verdad se guardo en nuestra base de datos:


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos\Diario>Sqlite3 diary.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> .tables
entry
sqlite> select * from entry;
1|Olakmira|2020-08-14 00:10:51.107422       # <<<--- Entrada guardada con exito :D
sqlite>


# Si agregamos ENTERS entre el espacio de la entrada, ESTOS NO SE GUARDAN POR QUE INCLUIMOS strip() en nuestra variable "data"

# Strip quita los espacion antes y despues, ya sean espacios, tabulaciones, enters, etc. TODOS LOS ESPACION LOS QUITA ALV



"""             A   D   D       E   N   T   R   Y       C   O   M   P   L   E   T   A           """



def add_entry():
    """Add entry"""
    print("Enter your toughts. Press ctrl + Z on Windows or ctrl + D on Mac to finish")
    data = sys.stdin.read().strip()

    if data:
        if input("Do you want to save your entry? [Yn] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("Your entry was saved succesfully")
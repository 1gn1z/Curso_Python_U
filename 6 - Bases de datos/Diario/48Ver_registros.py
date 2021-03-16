# Vamos a VER las entradas de nuestro diario :3


# Ya vimos que si funciona, pero NO queremos que los usuarios entren a Sqlite, hacer un query de las tablas etc.

# Queremos dar una forma que se puedan ver desde el programa mismo.

# Vamos a nuestra funcion de view_entries()

# Lo primero que queremos hacer es obtener TODAS las entradas con un orden DESCENDENTE, con la mas actual hasta arriba.

# Asi que haremos una variable llamada "entries", y sera igual a Entry.select(), POR QUE ESTO DEVUELVE TODAS LAS ENTRADAS OK ;)

entries = Entry.select()

# Y le vamos a poner un ORDER BY. Este es un concepto de SQL, que nos ayuda a ordenar nuestros registros.


entries = Entry.select().order_by()


# Y como parametros le pondremos el atributo TIMESTAMP de nuestro modelo (clase, tabla) ENTRY, seguido de PUNTO DESC:


entries = Entry.select().order_by(Entry.timestamp.desc()) # DESC es para la mas reciente hasta arriba, la mas antigua hasta abajo


# Si queremos la mas antigua hasta arriba ponemos ASC (ASCendente), en lugar de DESC (DESCendiente)



# Ahora que ya obtuvimos las entradas, tenemos que obtener su TIMESTAMPS, es decir, la fecha en la que fueron añadidas,
# Y darles un bonito formato :3


# Lo primero que tenemos que hacer es un ciclo FOR, para iterar todas las entradas:

for entry in entries:
   
# Ahora hacemos una variable, llamada "timestamp", que contendra el Atributo TIMESTAMP de nuestra clase (Tabla, Modelo) ENTRY

timestamp = entry.timestamp         # <<<--- Recordemos que timestamp es uno de los atributos de nuestra clase Entry



# Y seguido del atributo "timestamp", vamos a agregar un STRFTIME, por que queremos darle un formato



for entry in entries:
    timestamp = entry.timestamp.strftime('%d/%m/%Y %A  %I:%M%p')    # Formato elegido. Muestra fecha 10/10/2020 DIA  AÑO CON SIGLOS


# Ahora imprimiremos la TIMESTAMP

    print(timestamp)        # Se desplegara la fecha y hora en la que fue escrita la entrada, con el formato que indicamos antes.
    

# Ahora pondremos un SEPARADOR, si recordamos, lo que haciamos era algo como un print con muchos asteriscos o lineas:


print('****************************************************************')


# Pero ahora usaremos un truco :D. Lo que haremos es esto:

print('+'*len(timestamp))   # Lo que hacemos es, con la funcion LEN, obtener el tamaño de caracteres del timestamp
                            # Y multiplicaremos el simbolo '+' por la longitud del timestamp, es decir
# IMPRIMIREMOS EL SIMBOLO + LA CANDITAD DE CARACTERES QUE TENGA EL TIMESTAMP, (si tiene 15, se imprimen 15 simbolos de +)    


for entry in entries:
    timestamp = entry.timestamp.strftime('%d/%m/%Y %A  %I:%M%p')
    print(timestamp)
    print('+'*len(timestamp))
    
    
# Ahora queremos obtener el CONTENIDO de nuestra entrada, lo unico que haremos para obtenerla es 
# IMPRIMIR EL ATRIBUTO CONTENT DE LA CLASE ENTRY    

    print(entry.content)
    
# Y vamos a poner un pequeño menu:

    print('n) next entry')
    print('q) return to menu')
    
# Y para validar estas opciones haremos un IF, pero lo vamos a separar en variables para que sea mas sencillo :D

    
    next_action = input('Action: ').lower().strip()
    
    
# Ahora si validamos con un IF, si la opcion que elige el usuario es 'q', terminamos la condicional. (con un break)

    if next_action == 'q':      # Si el usuario pone 'q' (regresar al menu), 
        break                   # rompemos la condicion, y al terminar esta condicion, regresamos al ciclo del "menu_loop" 



"""           V   E   R       R   E   G   I   S   T   R   O   S       C   O   M   P   L   E   T   O           """    

def view_entries():
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
for entry in entries:
    timestamp = entry.timestamp.strftime('%d/%m/%Y %A  %I:%M%p')
    print(timestamp)
    print('+'*len(timestamp))
    print(entry.content)
    print('n) next entry')
    print('q) return to menu')
    
    next_action = input('Action ').lower().strip()
    
    next_action == 'q':
        break
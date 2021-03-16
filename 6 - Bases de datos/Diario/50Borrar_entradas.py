# Ahora vamos a hacer una funcion para borrar una entrada:

# Ya tenemos una funcion para ello, pero ahora pondremos como PARAMETRO (entre comillas), la entrada que queremos borrar:

def delete_entry(entry):        # <<<--- Acepta un parametro que es la entrada a eliminar        
    """Delete an entry"""


# SIEMPRE que el usuario quiera borrar algo lo mas comun ES PREGUNTAR POR LA CONFIRMACION, (Estas seguro de borrarlo?).

# Asi que haremos una variable, llamada por ejemplo "action", que sera igual a un input:

    action = input('Are you sure you want to delete this entry? [Yn] ').lower().strip()# Lower para convertir todo a minusculas y no tener problemas

# Ahora vamos a hacer una condicional que, si es igual a y, proceda a borrar la entrada:
    
    if action == 'y':
        
# Y para borrar un unico registro:

    entry.delete_instance() 
    

# Esta opcion la vamos a tener en la funcion "view_entries", ira en las opciones, justo despues de NEXT ENTRY:           



def view_entries(search_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%d/%m/%Y %A  %I:%M%p')
        print(timestamp)
        print('-'*len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('d) delete entry')        # <<<--- Aqui va la opcion para borrar la entrada.
        print('q) return to menu')


# Y en este if, pondremos un ELIF, para verificar si la opcion es igual a 'd', llamaremos a la funcion "delente_entry"

        
        next_action = input('Action ').lower().strip()
    
        if next_action == 'q':          # Si la opcion es igual a q, rompemos (break) el ciclo
            break 
        elif next_action == 'd':        # Y si la opcion es igual a 'd':
            delete_entry(entry)         # llamamos a la funcion que borrara la entrada, pasando el parametro, osea la entrada en la
                                        # en la que nos encontramos        
        
                

"""           B   O   R    R    A    R        R   E   G   I   S   T   R   O   S       C   O   M   P   L   E   T   O           """    


def delete_entry(entry):
    """Delete an entry"""
    action = input('Are you sure you want to delete this entry? [Y/n] '
                   ).lower().strip()

    if action == 'y':
        entry.delete_instance()               
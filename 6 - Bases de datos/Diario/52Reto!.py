# Vamos a implementar las siguientes funciones:

# Tratar de implementar una mejor paginacion (por ejemplo mostrar una pagina con 5 entradas)

# Opcion para EDITAR nuestras entradas.

# Buscar entradas por FECHAS    LISTO!



#   #   #   -------------------------------------------------------------------


# Vamos a hacer una funcion para EDITAR nuestras entradas:

"""def edit_entry(entry):
    """Edit an Entry"""
    Entry.content = input('Editar entrada: \n')
    Entry.content.save()"""
    
    
    
    
#   #   #   -------------------------------------------------------------------

def edit_entry(entry):
    """Edit an Entry"""
    Entry.content = input('Editar entrada: \n')
    data = sys.stdin.read().strip()
    
    if data:
        if input("\nDo you want to save your entry? [Y/n] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("\nYour entry was saved succesfully\n")   

#   #   #   -------------------------------------------------------------------


    def add_entry():
    """Add entry"""
    print("\nEnter your toughts.")
    print("Press ctrl + Z on Windows or ctrl + D on Mac to finish\n")
    data = sys.stdin.read().strip()

    if data:
        if input("\nDo you want to save your entry? [Y/n] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("\nYour entry was saved succesfully\n")
            
            
            

def edit_entry(entry):
    """Edit an Entry"""
    Entry.content = input('Editar entrada: \n')
    data = sys.stdin.read().strip()
    
    if data:
        if input("\nDo you want to save your entry? [Y/n] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("\nYour entry was saved succesfully\n")        



#   #   #   -------------------------------------------------------------------

# Funcion para buscar por fechas

# Agregamos la opcion en el menu

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('x', search_dates),        #<<<--- Opcion
    ('d', delete_entry)
])

# Funcion que pide al usuario que busque por numero entero

def search_dates():
    """Search by dates"""
    search_dates = int(input('Search date: '))
    view_entries(search_dates)

# Y agregamos como parametro a la funcion view entries

def view_entries(search_dates=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
            
       
    if search_dates:  
        entries = entries.where(Entry.timestamp.contains(search_dates))    
        
        
#   #   #   -------------------------------------------------------------------



def view_entries(search_dates=None, search_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
            
            
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
        
    elif search_dates:  
        entries = entries.where(Entry.timestamp.contains(search_dates))        


# No se porque SOLO TOMA EL PRIMER ARGUMENTO :(
    
    
#   #   #   -------------------------------------------------------------------

# FUNCION PARA BUSCAR POR FECHA LOGRADO!!!

# La unica forma que lo logre fue COPIANDO LA FUNCION VIEW ENTRIES CON OTRO NOMBRE PARA QUE ACEPTARA SOLO EL PARAMETRO DE LAS FECHAS    


def view_entries_date(search_dates=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
            
 
    if search_dates:  
        entries = entries.where(Entry.timestamp.contains(search_dates))        

    for entry in entries:
        timestamp = entry.timestamp.strftime('%d/%m/%Y %A  %I:%M%p')
        print()
        print('-'*len(timestamp))
        print('\n')
        print(timestamp)
        print('\n')
        print(entry.content)
        print('\n')
        print('-'*len(timestamp))
        print()
        print('n) next entry')
        print('d) delete entry')
        print('q) return to menu')
    
        next_action = input('Action: [Ndeq] ').lower().strip()
    
        if next_action == 'q':
            break 
        elif next_action == 'd':
            delete_entry(entry)


def search_dates():
    """Search by dates"""
    search_dates = int(input('Search date: '))
    view_entries_date(search_dates)


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries and view_entries_date),      # <<<--- Vamos a agregar un AND para que lea ambas funciones y no haya pex :D
    ('s', search_entries),
    ('x', search_dates),
    ('d', delete_entry)
])


# (ver test.py)


#   #   #   -------------------------------------------------------------------
























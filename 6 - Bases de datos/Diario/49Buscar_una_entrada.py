# Vamos a ver como buscar una entrada especifica en nuestro diario,

# Lo primero que tenemos que hacer es añadir esa funcion al menu:

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('d', delete_entry)
])


# Vamo' a ponerlo antes de la opcion "delete_entry"


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),  # <<<--- nueva opcion, NO OLVIDAR PONER LA COMA
    ('d', delete_entry)
])


# Ahora vamos a definir la funcion:


def search_entries():
    
# Y hacemos una variable, llamada por ejemplo "search_query", y le pondremos un INPUT, donde pidamos que quiere buscar el usuario:


def search_entries():
    search_query = input("Search query: ")


# En este caso no es necesario poner LOWER() xq tal vez el usuario buscó algo con mayuscula, eso no queremos alterarlo, 
# solo pondremos STRIP(). Para eliminar los espacios


def search_entries():
    search_query = input("Search query: ").strip()      # <<<--- Solo ponemos strip
    
    
    
# Ya teniendo el search_query, en lugar de escribir todo el codigo para una entrada en especifico, VAMOS A REUTILIZAR
# El codigo de view_entries, para que se FILTRE SOLO LAS ENTRADAS QUE TENGAN ALGUNA PARTE DE TEXTO QUE COINCIDA con lo que ingrese el usuario

# Para hacerlo, vamos a decir que VIEW ENTRIES, ACEPTE UN PARAMETRO, que sera nuestra variable SEARCH QUERY:


def view_entries(search_query):         # <<<--- Ahora nuestra funcion admite un parametro
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())


# PERO!!! este parametro es OPCIONAL, si no lo ponen, nosotros le daremos un valor de NONE



def view_entries(search_query=None):         # Es OPCIONAL, por eso el valor NONE                           


# En nuestra funcion "search_entries", vamos a llamar a la funcion "view_entries" y le pasamos el parametro (nuestra search_query)

def search_entries():
    search_query = input("Search query: ").strip()      # <<<--- Solo ponemos strip
    view_entries(search_query)






def view_entries(search_query):         
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())    # <<<--- Como filtramos TODAS estas entradas
    
    
    
    
# para que solo contengan el texto que busque el usuario?



# Lo primero es ASEGURARNOS QUE HAYA UN SEARCH QUERY, si el usuario no quiere buscar nada, pues no tenemos que filtar nada


# Al igual que hicimos con el iF DATA:

###     ------------------------------------------------------------------------------------------------------------     ###
def add_entry():
    """Add entry"""
    print("Enter your toughts. Press ctrl + Z on Windows or ctrl + D on Mac to finish")
    data = sys.stdin.read().strip()

    if data:    # <<<--- Este if VERIFICA que haya algo en la variable data, si lo hay entrara al siguiente if
         
        if input("Do you want to save your entry? [Yn] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("Your entry was saved succesfully")      
###     ------------------------------------------------------------------------------------------------------------     ###
            
            
# Entonces aqui lo haremos igual:



def view_entries(search_query):         
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())             
    
    
    if search_query:            # Lo unico que hace este es es VERIFICAR que haya algo en el search query, es decir, si el usuario
                                # quiere buscar algo, Si hay algo entra, si no, pos no xD
                                

# Ok, entonces si entra:

def view_entries(search_query):         
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())           # <<<--- 1o.
    
    if search_query:                                                    # <<<--- 2o
        entries = entries.where(Entry.content.contains(search_query))   # <<<--- 3o                                
        

# 1o.- Ya tenemos TODAS las entradas, con el metodo SELECT obtenemos TODAS, y con order by las ordenamos
# Entry.timestamp es la FECHA de creacion de esa entrada, y DESC es el metodo DESCENDENTE, es decir, la mas nueva arriba.


# 2o.- Ya sabemos que SI nos paso una busqueda de algo especifico.         


# 3o.- Entonces, si nos pasaron algo, las entradas (entries), sera igual a las entradas (entries)
# DONDE (where), el CONTENIDO DE LA ENTRADA (Entry.content) CONTENGA (contains) la busqueda que haga el usuario (search_query)


# Eso es todo, solo nos falta PONER EL DOCSTRING a nuestra funcion llamada "search_entries"


def search_entries():
    """Search Entries"""        # Por que hay que recordar que nuestro menu toma el docstring para mostrarlo via metodo __doc__
    search_query = input("Search query: ").strip()
    view_entries(search_query)
    
    
    
"""           B   U   S    C    A    R        R   E   G   I   S   T   R   O   S       C   O   M   P   L   E   T   O           """    


# POR LETRAS

def search_entries():
    """Search entries"""
    search_query = input('Search query: ').strip()
    view_entries(search_query)


# POR FECHAS

def search_dates():
    """Search by dates"""
    search_dates = input('Search date: ')
    view_entries_date(search_dates)    
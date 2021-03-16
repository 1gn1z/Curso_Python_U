# Vamos a ver un metodo para ejecutar las funciones a partir de nuestro menu:


# Ya obtuvimos la opcion del usuario, que nos dara una a, v, d o q, pero la q ya la manejamos

# Lo que podriamos hacer con nuestra variable "choice", es hacer un IF, como lo hecho hecho anteriormente

# Si choice es igual a v, hacer esto, si choice es igual a d, hacer lo otro etc.

# Es una implementacion valida, pero python busca que todo sea facil :D, asi que debe haber otra forma mas sencilla <3


# Primero vamos a modificar nuestro diccionario ordenado:


menu = OrderedDict([
    ('a)', 'add entry'),
    ('v)', 'view entry'),
    ('d)', 'delete entry')
])

# Vamos a REEMPLAZAR LAS CADENAS ('add entry, 'view entry' y 'delete entry'), con LOS NOMBRES DE LAS FUNCIONES (como si las llamaramos
# , sin ser cadenas ok)


menu = OrderedDict([
    ('a)', add_entry),          #
    ('v)', view_entry),         # REEMPLAZAMOS LOS VALUES DEL DICTORDERED: EN LUGAR DE CADENAS AHORA SON LOS NOMBRES DE LAS FUNCIONES
    ('d)', delete_entry)        #
])


# Estando asi el codigo, YA NO FUNCIONARA, por que en el menu loop estamos desplegando una cadena, que acabamos de reemplazar
# Por nombres de funciones.

# Debe haber alguna forma de ACCEDER AL DOCSTRING, para que en lugar de poner el NOMBRE DE LA FUNCION PONGA ESE TEXTO DEL DOCSTRING

# Asi podriamos cambiar el docstring sin alterar el menu.

# Entonces vamos a agregar la funcion, donde formateamos la cadena de las opciones del menu:

def menu_loop():
    """Show menu"""
    choice = "None"
    while choice != 'q':        
        print('Press "q" to quit')          
        for key, value in menu.items():
            print(f'{key} {value.__doc__}')         # Lo agregamos aqui, JUNTO CON EL VALUE, que es reemplazado por el nombre de la
                                                    # clase, y que devuelve el Docstring de dicha clase
        choice = input('Action: ').lower().strip() 



# Este doc hace que, en la opcion a tenemos add_entry, que es una funcion, DOC lo que hace es, EN LUGAR DE EJECUTAR LA FUNCION
# DEVOLVERA EL DOCSTRING

# Si le pasamos 'a', como reemplazamos la cadena por el nombre de la funcion (que es el VALUE del diccionario ordenado), 
# buscara esa funcion, y como es el metodo DOC
# En lugar de ejecutar la funcion DEVOLVERA ESE DOC (docstring)


# Si le pasamos 'a' buscara la funcion (add_entry), y con el metodo __doc__, devolvera el DOCSTRING que tiene esa funcion

# Si le pasamos 'v' buscara la funcion (view_entry), y con el metodo __doc__, devolvera el DOCSTRING que tiene esa funcion

# Si le pasamos 'd' buscara la funcion (delete_entry), y con el metodo __doc__, devolvera el DOCSTRING que tiene esa funcion



# Ya podemos checar nuestro script, PERO!, como las funciones ahora mismo estan definidas DESPUES del menu, nos mandara error,
# Vamos a mover el menu JUSTO DESPUES DE QUE YA DEFINIMOS LAS FUNCIONES


def add_entry():
    """Add entry"""

def view_entries():
    """View all entries""" 

def delete_entry(entry):        
    """Delete an entry"""


menu = OrderedDict([
    ('a)', add_entry),
    ('v)', view_entries),
    ('d)', delete_entry)
])


# Ahora desplegamos el DOCSTRING que tienen las funciones:


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos\Diario>Dear_diary.py
Press 'q' to quit
a) Add Entry            # <<<--- Desplegamos
v) View all entries     # <<<--- Los
d) Delete an Entry      # <<<--- Docstrings :D
Action:
    
    
# Asi como lo tenemos no va a pasar na' por que aun no tienen na' xD nuestras funciones.


# Vamos a hacer un pequeño truco ;). Que sera poner la variable de nuestro menu, llamada igual "menu"
# Y con unos CORCHETES accederemos a algun elemento, en este caso CHOICE, que es nuestra LLAVE (KEY)

menu[choice]

# Con esto, si ponen "a", devolvera "Add entry", si ponen "v", devolvera "View all entries", etc.

# Y como esos son NOMBRES DE FUNCIONES, podemos simplemente poner parentesis:

menu[choice]()

# Pero! tambien queremos asegurarnos que la opcion elegida este dentro del menu, asi que usaremos un IF

if choice in menu:      # Si la opcion SI ESTA en el menu:
    menu[choice]()      # Ejecutamos esta linea de codigo



# Solo para asegurarnos que nuestras funciones funcan, vamos a añadir unos prints

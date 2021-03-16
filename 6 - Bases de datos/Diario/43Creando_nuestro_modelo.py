from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    # Content
    # Timestamp
    class Meta:
        database = db


def menu_loop():
    """Show Menu"""

def add_entry():
    """Add an Entry"""

def view_entries():
    """View all Entries"""

def delete_entry():
    """Delete an Entry"""


if __name__ == '__main__':
    menu_loop()     


# Ya sabemos que nuestra clase Entry debe tener un CONTENIDO, que es donde pondremos el texto de nuestro diario
# Y un TIMESTAMP, que es el momento en el que se introdujo la entrada.

# Vamos a crear estos campos: 

# Para el de texto podremos una variable, que sera de tipo TextField()
# Y para el timestamp podremos otra variable, que sera tipo DateField()

# No habiamos visto el tipo "TextField()", la diferencia de este con el CharField() es que el "TextField" puede
# tener CUALQUIER TIPO DE TEXTO, DE CUALQUIER LONGITUD, mientras que el CharField(), como recordaremos al abrirlo con Sqlite3
# Mencionaba que por defecto, tiene espacio para 255 Caracteres (Tiene tamaño limitado, Tiene LIMITE). TEXTFIELD NO TIENE LIMITE

content = TextField()

# Para el timestamp vamos a usar nuestra libreria de fechas, asi que hay que importar DATE de la libreria DATETIME

import datetime

timestamp = DateTimeField() # En lugar de solo DateField usamos DateTimeField por que mostrara la FECHA Y HORA que fue creada la entrada

# Y le vamos a asignar un default por si el usuario no pone nada:


timestamp = DateTimeField(default=datetime.datetime.now)    # Que nos dara la fecha y hora de ahora.


# Ahora vamos a CREAR la base de datos y a CONECTARNOS A ELLA.
# Ademas de CREAR LAS TABLAS:

# Asi que crearemos una funcion para crear la db y conectarnos:

def create_n_connect():                         # Funcion para crear la base de datos y conectarnos a ella
    db.connect()                                # Conexion de la base de datos
    db.create_tables([Entry],safe=True)         # Creacion de las tablas


# Recordemos que el "safe=True" es para que python no diga que la(s) tabla(s) ya esten creadas o ya existan y crashee


# Ahora solo llaremos a la funcion cada vez que se ejecute (no que se importe) nuestro codigo.
# Esto lo haremos dentro de nuestro NAME==MAIN:

# Comprueba si un módulo se está importando o no. 
# En otras palabras, el código dentro del bloque if se ejecutará solo cuando el código se ejecute directamente.


if __name__ == '__main__':
    create_n_connect()
    menu_loop()



# Vamos a añadir el Docstring a nuestra funcion "create_n_connect" 


def create_n_connect():           
    """Connects to the database and create the tables"""              
    db.connect()                                
    db.create_tables([Entry],safe=True)   


# Corremos nuestro codigo en la consola, SI NO MUESTRA NADA, ES DECIR, NO ARROJA NINGUN ERROR ESTA TODO BIEN :D

# Ya tenemos que tener un archivo .db creado, llamado "diary.db", vamos a asegurarnos que nuestra tabla este:

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos\Diario>Sqlite3 diary.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> .tables                     # <<<--- Consultamos las tablas de nuestra db
entry                               # <<<--- Efectivamente fue creada nuestra tabla
sqlite>
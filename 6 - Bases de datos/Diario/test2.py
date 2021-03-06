import datetime
import sys
import getpass
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('diary.db')

"""menu = OrderedDict([             TENEMOS QUE MOVER EL MENU A DONDE YA ESTEN DEFINIDAS LAS FUNCIONES:
    ('a)', add_entry),      
    ('v)', view_entries),
    ('d)', delete_entry)
])"""


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def create_n_connect():
    """Connects to the database and create the tables"""
    db.connect()
    db.create_tables([Entry],safe=True)


def menu_loop():
    """Show Menu"""
    choice = None                                       # <<<--- NONE SIN COMILLAS!
    while choice != 'q':
        print("\nPress 'q' to quit")
        for key,value in menu.items():
            print((f'{key}) {value.__doc__}'))            # El __doc__ va JUNTO CON EL VALUE
        choice = input('\nAction: ').lower().strip()
        
        if choice in menu:
            menu[choice]()
        
        
def add_entry():
    """Add entry"""
    print("\nEnter your toughts.")
    print("Press ctrl + Z on Windows or ctrl + D on Mac to finish\n")
    data = sys.stdin.read().strip()

    if data:
        if input("\nDo you want to save your entry? [Y/n] ").lower().strip() != 'n':
            Entry.create(content=data)
            print("\nYour entry was saved succesfully\n")


def view_entries(search_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
            
    #if search_query:
    #    entries = entries.where(Entry.content.contains(search_query))
        
    if search_query:  
        #entries = entries.where(Entry.timestamp.contains(search_dates))        
        entries = entries.where(Entry.timestamp == search_query).get()


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
        print('e) edit entry')
        print('q) return to menu')
    
        next_action = input('Action: [Ndeq] ').lower().strip()
    
        if next_action == 'q':
            break 
        elif next_action == 'd':
            delete_entry(entry)

"""
def search_entries():
    Search entries
    search_query = input('Search query: ').strip()
    view_entries(search_query)
"""


def search_dates():
    """Search by dates"""
    #search_query = Entry.select().where(Entry.timestamp == date).get()
    search_query = int(input('Search by date: '))
    view_entries(search_query)


def delete_entry(entry):        
    """Delete an entry"""
    action = input('Are you sure you want to delete this entry? [Y/n] ').lower().strip()
    
    if action == 'y':
        entry.delete_instance()

def validation(password):           # <<<--- Funcion para validar que la contrase??a sea correcta
    return password == 'XX531'

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
#    ('s', search_entries),
    ('x', search_dates),
    ('d', delete_entry)
])


if __name__ == '__main__':
    #password = getpass.getpass('\nWelcome to Dear_diary :)\nYou need a password to get acces :p\n\nPassword: ') 
    
    
      
#    password = getpass.getpass('Pass!!!')# <<<--- Funcion para introducir la contrase??a de forma segura (No se ve lo escrito)
                                          # <<<--- En el parentesis podemos imprimir otro texto que el default (password:)  
    
    #if validation(password):            # <<<--- Si se valida correctamente entra a las funciones princiopales
     #   print('\nWelcome!!!\nyou have acces to the diary :)')
    #else:                               # <<<--- Si NO, imprime el siguiente mensaje, y la linea 161 sale del programa        
     #   print('\nIncorrect password.\nPassword required to access diary\n')
      #  sys.exit(1)                     # <<<--- Salir del programa si la contrase??a no es correcta
    create_n_connect()
    menu_loop()


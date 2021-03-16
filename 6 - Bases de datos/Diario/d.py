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
#        print("\nPress 'q' to quit")
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
            
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
        
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
        elif next_action == 'e':
            edit_entry(entry)
            

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
        print('e) edit entry')
        print('q) return to menu')
    
        next_action = input('Action: [Ndeq] ').lower().strip()
    
        if next_action == 'q':
            break 
        
        elif next_action == 'd':
            delete_entry(entry)
        elif next_action == 'e':
            edit_entry(entry)

def search_entries():
    """Search entries"""
    search_query = input('Search query: ').strip()
    view_entries(search_query)



def search_dates():
    """Search by dates"""
    search_dates = input('Search date: ')
    view_entries_date(search_dates)


def delete_entry(entry):        
    """Delete an entry"""
    action = input('Are you sure you want to delete this entry? [Y/n] ').lower().strip()
    
    if action == 'y':
        entry.delete_instance()

def validation(password):           # <<<--- Funcion para validar que la contraseña sea correcta
    return password == 'XX531'

def quit():
    """Quit program"""
    action = input('Are you sure you want to EXIT the program? [Y/n] ').lower().strip()
    if action == 'y':
        sys.exit(1)
    else:
        print('\n\n')
        menu_loop()
        
        
        
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries and view_entries_date),
    ('s', search_entries),
    ('x', search_dates),
    ('d', delete_entry),
    ('q', quit)
])


if __name__ == '__main__':
    
    tries = 0
    while tries < 3:
        
        
        tries +=1
#        password = getpass.getpass('\nWelcome to Dear_diary :)\nYou need a password to get acces :p\n\n\nPassword: ') 
        password = getpass.getpass('\nWelcome to Dear_diary :)\n\nYou need a password to get acces :p\n\nTry #' + str(tries) + '\nPassword: ') 

#        tries +=1                                    
 
    
        if validation(password) and tries <=3:           
            print('\nWelcome!!!\n\nyou have acces to the diary :)\n')
            create_n_connect()
            menu_loop()

            
        elif tries >=3:
            print('\nIncorrect password.\nPassword required to access diary\n')
            sys.exit(1)                    
        
         



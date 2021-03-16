from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta():
        database = db  

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta():
        database = db




def init_db():
    db.connect(reuse_if_open=True)                  # <<<--- Solucion a error "peewee.OperationalError: Connection already opened."
    db.create_tables([Person, Pet],safe = True)
    db.close()


def add_person():
    name = input('Name of the member:\n').capitalize()
    birthday = date(input('[Y/m/d]:\n'))
    confirm = input('Are the data correct? [Y/n]: ').strip().lower()
    if confirm != 'y':
        add_person()
    elif confirm == 'y':    
        Person.create(
            name=name,
            birthday=date(birthday)
            
        )

if __name__ == "__main__":
    init_db()
    add_person()


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




def initialize_db():
    db.connect(reuse_if_open=True)                  # <<<--- Solucion a error "peewee.OperationalError: Connection already opened."
    db.create_tables([Person, Pet],safe = True)
    db.close()



wacha = Person(name='Wacha', birthday=date(1971,12,30))     # DATE ES AÑO,MES,DIA
wacha.save()

bugah = Pet.create(owner=wacha, name='Bugah', animal_type='Dog')


if __name__ == "__main__":
    initialize_db()
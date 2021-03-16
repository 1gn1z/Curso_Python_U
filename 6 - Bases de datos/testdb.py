from peewee import *
import sqlite3

db = SqliteDatabase('person.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta():
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta():
        database = db

def create_n_connect():
    db.connect()
    db.create_tables([Person,Pet],safe=True)


create_n_connect()




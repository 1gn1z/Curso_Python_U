from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

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

def create_family_members():
    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=True)           # Metodo 1
    uncle_tommy.save()

    grandma_lupe = Person.create(name='Lupe',birthday=date(1960,10,10),is_relative=False)   # Metodo 2


    tommys_dog = Pet.create(owner=uncle_tommy,name='Rayray',animal_type='Dog')
    lupes_bird = Pet.create(owner=grandma_lupe,name='Quetz',animal_type='Bird')

create_n_connect()
create_family_members()



# Vamos a ACTUALIZAR los registros

# Si ya tenemos una variable que contiene ese registro solo tenemos que modificar los atributos.
# Vamos a cambiarle el nombre al perro:

tommys_dog.name = "Firulais"        # Accedemos a su atributo NAME, y lo REASIGNAMOS (ACTUALIZAMOS)
tommys_dog.save()                   # Aqui si necesitamos GUARDAR para que se actualize nuestro registro


# Ahora ejecutamos de nuevo el archivo .py, y consultamos todos los registros de la tabla Pet en Sqlite3


9|14|Firulais|Dog
10|15|Quetz|Bird


# Como vemos, el registro del perro ya ha sido actualizado en su campo nombre.
"""

Model Definition
Model classes, fields and model instances all map to database concepts:

Object	Corresponds to…

Model class	    --->>>    Database table
Field instance	--->>>    Column on a table
Model instance	--->>>    Row in a database table

"""

from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta():
        database = db  # this model uses the "people.db" database


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()


def create_n_connect():     # Funcion que conecta y crea las tablas de nuestra base de datos.
    db.connect()
    db.create_tables([Person, Pet], safe=True)



#----------------------------------------------- Guardar registros METODO 1 (SAVE) ----------------------------------------------- #

tio_bob = Person(name='Bob', birthday=date(1960, 1, 15))    # Especificamos los campos de la clase, que se mapean como una FILA
                                                            # en la tabla indicada (Person), de nuestra base de datos.
tio_bob.save()      # Ahora Bob esta guardado en nuestra base de datos.
# Regresa 1, ya que cuando llamamos al metodo SAVE, retorna el numero de filas modificadas, en este caso 1.



#----------------------------------------------- Guardar registros METODO 2 (CREATE) ----------------------------------------------- #

abuelita = Person.create(name='Abue Lupe', birthday=date(1935, 3, 1))
amada_lulis = Person.create(name='Lulis', birthday=date(1950,5,9))


#----------------------------------------------- Actualizar informacion ----------------------------------------------- #

# Para actualizar datos, tenemos que REASIGNARLOS,
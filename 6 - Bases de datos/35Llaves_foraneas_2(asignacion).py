

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
    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=True)
    uncle_tommy.save()

    grandma_lupe = Person.create(name='Lupe',birthday=date(1960,10,10),is_relative=False)

create_n_connect()
create_family_members()





"""
# Tenemos una clase "Pet", que hereda de "Model", lo cual mapeara a una tabla en nuestra DB
# Pero esta clase tiene una LLAVE FORANEA, que apunta hacia una PERSONA, que es el dueño de la mascota.


# Para asignar una llave foranea, primero crearemos una funcion, llamada por ejemplo "create_family_pets():"

def create_family_pets():


# Ahora creamos una variable para el nombre de la mascota del tio tommy, por ejemplo:


def create_family_pets():
    tommys_dog = Pet.create(owner='Tommy',name='Rayray')


                                        M           A           L
"""




# Pero aqui hay un problema, NO PODEMOS USAR LA VARIBALE "uncle_tommy", por que esta DENTRO DE LA FUNCION "create_family_members"
# Recordemos que LAS VARIABLES QUE PERTENECEN A UNA FUNCION SOLO PUEDEN SER USADAS EN ESA MISMA FUNCION.


# Entonces mejor agregamos la variable de la mascota de tommy directamente en la funcion de los miembros de la familia "create_family_members"
# Ya dentro de la funcion, en lugar de pasarle como dueño la cadena 'Tommy', le pasaremos la variable "uncle_tommy"


def create_family_members():
    tommys_dog = Pet.create(owner=uncle_tommy,name='Rayray',aninal_type='Dog')


# Aqui mismo le registraremos una mascota a la abuelita Lupe :3 un canario llamado Quetz

    lupes_bird = Pet.create(owner=grandma_lupe,name='Quetz',animal_type='Bird')


# Ahora vamos a consultar todo lo que tenga nuestra tabla "Pet"    

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> select * from pet;
1|6|Rayray|Dog
2|7|Quetz|Bird

# Como vemos, tienen un NOMBRE, "Rayray" y "Quetz".
# Rayray es un PERRO, y Quetz es un AVE.

1|Tommy|2000-11-11|1
2|Tommy|2000-11-11|1
3|Lupe|1960-10-10|0
4|Tommy|2000-11-11|1
5|Lupe|1960-10-10|0
6|Tommy|2000-11-11|1
7|Lupe|1960-10-10|0
8|Tommy|2000-11-11|1
9|Lupe|1960-10-10|0

1|6|Rayray|Dog
2|7|Quetz|Bird
3|8|Rayray|Dog
4|9|Quetz|Bird

# Ahora, vemos despues de las llaves primarias de las mascotas otro numero, este otro numero MAPEA al nuestro registro de la DB

# En este caso le asigno que a RAYRAY (8), mapea a su dueño, que es Tommy (que tiene ese 8 de LLAVE PRIMARIA)
# Y en el caso de QUETZ(9), mapea tambien a su dueña, que es Lupe (que tiene la LLAVE PRIMARIA 9)

# Se asignan a nuestros 2 ultimos registros por que en este momento estamos creando una y otra vez la base de datos.



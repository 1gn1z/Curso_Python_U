from peewee import *
from datetime import date

db = SqliteDatabase('family.db')   # Creacion de una variable que contiene una base de datos en Sqlite3 llamada "persons.db"

class Person(Model):
    name = CharField()
    birthday = DateField()
    relation = CharField()

    class Meta():
        database = db

# Vamos a crear una clase para las mascotas

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta():
        database = db

# Creacion de la clase mascota lista.


def create_n_connect():
    db.connect()                            # Conexion a la base de datos (a la variable que contiene la base de datos en Sqlite3)

    db.create_tables([Person,Pet],safe=True)    # Creacion de las tablas (clases que se convierten en tablas)


def create_family_members():                    # Cada vez que llamemos esta funcion se crean los registros, por eso se duplican
    sister_mari = Person.create(name='Mari',    # Creacion de una instancia nueva, con sus datos especificos
                                birthday=date(1970,11,10),
                                relation='Sister')

    brother_wacha = Person.create(name='Wacha',
                                  birthday=date(1971,12,12),
                                  relation='Brother')

    amada_lula = Person.create(name='Obdulia <3',
                               birthday=date(1950,5,6),
                               relation='Mother')

# Vamos a crear a la mascota miel 

    wachas_dog = Pet.create(owner=brother_wacha,
                            name='Miel',
                            animal_type='Dog')

    amadas_bird = Pet.create(owner=amada_lula,
                            name='Piolin',
                            animal_type='Bird')


    amadas_bird.name = 'Quetz'      # Actualizacion de nombre (En este caso del ave de mi amada)
    amadas_bird.save()              # Guardar el nuevo registro


def get_family_members():                       # Funcion para consultar TODOS los registros de la tabla person (select extrae todos)
    for person in Person.select():
        print(f'Nombre:{person.name}.Cumpleaños:{person.birthday}. Relation:{person.relation}.')


def get_family_pets():
    for pet in Pet.select():
        print(f'Dueño: {pet.owner}. Nombre de la mascota: {pet.name}. Tipo de animal: {pet.animal_type}')



def get_family_members_birthday(name):          # Funcion que acepta un parametro "name", y muestra el cumpleaños de la persona
    family_member = Person.select().where(Person.name==name).get()
    print(f'{name} cumple el:{family_member.birthday}')

def get_family_members_relation(name):          # Funcion que acepta un parametro "name", y muestra la relacion con la persona
    family_member = Person.select().where(Person.name==name).get()
    print(f'{name}es mi: {family_member.relation} ')


def get_family_pet(name):
    family_member = Pet.select().where(Pet.name==Pet.name).get()
    print(f'La mascota de {name} es {Pet.name}')





create_n_connect()                              # Creacion y conexcion de la base de datos
create_family_members()                        # Creacion de los registros (Cada vez que se ejecuta, por eso se duplican)
get_family_members()                            # Consulta de TODOS los registros (De la tabla Person)
get_family_members_birthday('Wacha')            # Consulta del Cumpleaños de la persona que queramos consultar (Parametro entre parentesis)
get_family_members_relation('Wacha')            # Consulta de la relacion de la persona que queramos consultar (Parametro entre parentesis)

get_family_pet('Obdulia <3')







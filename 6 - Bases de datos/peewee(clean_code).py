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
    grandma_rosa = Person.create(name='Rosa',birthday=date(1960,10,10),is_relative=False)  


    tommys_dog = Pet.create(owner=uncle_tommy,name='Rayray',animal_type='Dog')
    lupes_bird = Pet.create(owner=grandma_lupe,name='Quetz',animal_type='Bird')


    tommys_dog.name = "Firulais"
    tommys_dog.save()


def get_family_members():
    for person in Person.select():
        print(f'Nombre: {person.name}. Fecha de nacimiento: {person.birthday}. Es familiar? {person.is_relative}')
        #print("Nombre: {}. Fecha de nacimiento: {}. Es pariente? {}.".format(person.name,person.birthday,person.is_relative))     


def get_family_member_birthday(name):

    #family_member = Person.select().where(Person.name==name).get() 

    family_member = Person.get(Person.name==name)       # <<<--- Metodo mucho mas facil y legible

    print(f'{name} cumple el: {family_member.birthday}')


"""def delete_pet(name):
    query = Pet.delete().where(Pet.name==name)
    deleted_entries = query.execute()
    print(f'Registros borrados: {deleted_entries}')"""


def delete_pet(name):
    rayray = Pet.get(Pet.name == 'Rayray')
    deleted_entry = rayray.delete_instance()
    print(f'{deleted_entry} Registro borrado')





create_n_connect()
#create_family_members()                Ya no queremos mas duplicados, por eso vamos a dejar de llamar este método (Una vez creado el nuevo registro (Rosa))
#get_family_members()                   Vamos a borrar estas 2 funciones, ya vimos que si funcionan
#get_family_member_birthday('Rosa')

delete_pet('Quetz')







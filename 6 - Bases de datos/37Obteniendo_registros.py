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


    tommys_dog.name = "Firulais"
    tommys_dog.save()

create_n_connect()
create_family_members()


# Ahora vamos a aprender como OBTENER 1 O VARIOS REGISTROS de nuestra DB.


# Vamos a definir un metodo que nos devuelva TODOS los registros que esten actualmente en la tabla de personas, lo vamos a llamar
# "get_family_members():"

def get_family_members():

# Asi como le haciamos para obtener todos los datos de una lista, con un ciclo FOR, en una tabla es algo muy similar.
# 
# 
    for person in Person.select():      # El nombre de la clase CON MAYUSCULA.    

# Como vemos en las consultas de Sqlite3, usamos el metodo SELECT para obtener todos los registros de esa tabla.
# Asi que haciendo esto nos devolvera TODOS los registros de nuestra tabla (Person)

# Finalmente solo llamamos un print, Y le añadimos los parametros (Nombre, Cumpleaños, y is_relative), usando la funcion FORMAT

# NOTA. Yo ya usare la otra forma de usar format, ya que la que usa el profe esta antigua


print(f'Nombre: {person.name}. Fecha de nacimiento: {person.birthday}. Es familiar? {person.is_relative}')


print("Nombre: {}. Fecha de nacimiento: {}. Es pariente? {}.".format(person.name,person.birthday,person.is_relative)) # Metodo de siempre     


# Finalmente vamos a llamar la nueva funcion:

get_family_members()


# Asi, obtenemos TODOS los registros, pero que pasa si queremos obtener solo UN registro:
# 

# Vamos a crear otro registro, copiamos el de la abuela, solo le vamos a cambiar el nombre 

grandma_rosa = Person.create(name='Rosa',birthday=date(1960,10,10),is_relative=False)  


#create_family_members()    Ya no queremos mas duplicados, por eso vamos a dejar de llamar este método (Una vez creado el nuevo registro (Rosa))


# Para llamar a UN SOLO REGISTRO en particular vamos a hacer otra funcion

def get_family_member_birthday():

# Queremos que sea, por ejemplo, la abuela Rosa:
# 
grandma_rosa = Person.select().where(Person.name == "Rosa").get() 

# Es importante llamar a GET al final, por que si NO lo llamamos nos dara una lista de resultados con TODOS los registros (select)

# Queda finalmente asi:

def get_family_member_birthday():
    grandma_rosa = Person.select().where(Person.name=='Rosa').get() 
    print(f"La abuela Rosa cumple el {grandma_rosa.birthday}")

get_family_member_birthday()


# Ahora vamos a decir que nuestra funcion va a ACEPTAR UN PARAMETRO (name), el nombre de quien queremos consultar el cumpleaños


def get_family_member_birthday(name):   # Acepta el parametro

    # grandma_rosa = Person.select().where(Person.name==name).get() # Reemplazamos el nombre por la variable "name" 
    # Y en lugar de ser la abuela pondremos la variable "family_member"

    family_member = Person.select().where(Person.name==name).get()

    # print(f"La abuela Rosa cumple el {grandma_rosa.birthday}")    Vamos a quitar el mensaje de la abuela, y reemplazar
    # la variable "grandma_rosa" por la variable "family_member"
    # Y añadimos otras llaves, que seran el NOMBRE del miembro de la familia.

    print(f'{name} cumple el: {family_member.birthday}')



get_family_member_birthday('Rosa')  # Aqui especificamos el parametro que deseamos usar.
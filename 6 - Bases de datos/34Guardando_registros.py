from peewee import *
import sqlite3

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


create_n_connect()




# Aprenderemos a guardar informacion en nuestra base de datos.

# Tenemos una clase Person, que tiene, nombre, cumpleaños y is_relative

# Ademas de una clase Pet, que tiene dueño, nombre y tipo de animal.


# Asi como lo tenemos no sirve de mucho, no sirve de nada tener tablas en nuestra DB si no tienen registros

# Para guardar info en nuestas tablas, vamos a crear una funcion, llamada por ejemplo "create_family_members"

# Esta funcion indica con el nombre que sera para crear registros en nuestra tabla Person, y sera para miembros de la familia

# Para crear un registro de, por ejemplo, un tio, añadimos una VARIABLE, seguido de "Person", por que es una persona
# Entre parentesis "name" es igual a, y el nombre de la persona.



def create_family_members():         # Creacion de INSTANCIA del modelo Person 
    uncle_tommy = Person(name="Tommy")       


# Despues vamos a pasarle el registro del cumpleaños, pero NO podemos hacerlo como normalmente lo hariamos, asi:

def create_family_members():
    uncle_tommy = Person(name="Tommy",birthday="2000-11-11")


# Por que el cumpleaños tambien es una cadena de texto, y en la consulta que hicimos Sqlite3 dice que es de tipo DATE, no VARCHAR 

# Entonces, tenemos que IMPORTAR la libreria DATE, de DATETIME.

from datetime import date


# Ahora si, a la variable (campo, atributo) "birthday" sera igual a date, y entre parentesis, con numeros enteros
# 2000,11,11

def create_family_members():
    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11))

# Despues pondremos la ultima variable "is_relative", que en este caso como es nuestro tio es TRUE:

def create_family_members():
    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=True)


# Ya tenemos lista la instancia de la clase Person, pero aun NO esta guardada en nuestra DB
# Para guardarla le decimos a peewee simplemente

uncle_tommy.save()  # Este es un METODO de la clase MODEL


def create_family_members():
    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=True)   # Creacion del registro
    uncle_tommy.save()                                                              # Guardado del registro

# Finalmente no debemos olvidar llamar a la funcion

create_family_members()



# Ahora en la consola volvemos a llamar al archivo, para que se cree (o actualize) la base de datos

# ahora vamos a ver si fue creada correctamente el registro en nuestra tabla "Person"
# Primero accedemos a la base de datos:

Sqlite3 people.db

# Y despues vamos a seleccionar todos los registros de la tabla person:

sqlite> select * from person;
1|Tommy|2000-11-11|1
sqlite>

# Como vemos, nos muestra correctamente el registro que acabamos de crear:

# Se llama Tommy, tiene fecha de cumpleaños del 2000-11-11, y en is_relative es igual a 1, es decir TRUE
# Recordemos que TRUE = 1 y FALSE = 0




# PERO!!! hay otra forma MAS SENCILLA de crear registros.
# En este caso se utiliza el METODO CREATE, este metodo pertenece a la clase MODEL

grandma_lupe = Person.create()

# Ya simplemente le pasamos los parametros de los atributos de nuestra clase person

grandma_lupe = Person.create(name='Ana',birthday=date(1960,10,10),is_relative='False')


# Como llamamos al metodo CREATE automaticamente se creara esta entrada en nuestra base de datos
# Ya no es necesario llamar al metodo SAVE


# Vamos a volver a consultar nuestra base de datos

# NOTA. para salir de la ejecucion de Sqlite3 escribimos .quit

# NOTA. No olvidar LLAMAR AL ARCHIVO .py para actualizar la base de datos


# Si aparecio el registro de la abue, pero APARECIERON 2 entradas del tio tomy, del primer registro.

# Esto pasa por que SE VOLVIO A EJECUTAR el codigo del uncle tommy, y ademas se agrego el registro de la abue

# Cada vez que ejecutamos el metodo create_family_members, creamos los 2 registros,

# Lo que tenemos que hacer es ACTUALIZAR el registro de tommy 

# Le estamos diciendo a peewee que lo que queremos es guardar o insertar un nuevo registro, por eso se duplico.


# Si volvemos a llamar el archivo .py y consultamos la base de datos ahora tendremos 3 registros de tommy y 2 de lupe

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> select * from person;
1|Tommy|2000-11-11|1
2|Tommy|2000-11-11|1
3|Lupe|1960-10-10|0
4|Tommy|2000-11-11|1
5|Lupe|1960-10-10|0

# Pero estos registros mantienen los mismos datos.

# Algo curioso es que a cada registro se le asigna automaticamente una LLAVE PRIMARIA (1,2,3,4,5)
# Estas llaves nos sirven para identificar un registro unico en nuestras tablas.

# Este concepto de las llaves primarias es un concepto de las bases de datos en general.
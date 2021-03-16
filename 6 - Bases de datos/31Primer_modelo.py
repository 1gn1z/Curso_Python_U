"""

                                    CLASES             ===         TABLAS

                                    ATRIBUTOS (CLASES) ===        COLUMNAS

                                    OBJETOS            ===         FILAS


"""

# Como ya sabemos las clases de nuestro codigo se mapean como una tabla en nuestra base de datos
# Los atributos se mapean como columnas y los objetos pasan a ser filas en nuestra tabla:


"""

Object 	            Corresponds to…

Model class 	    Database table                  # Una clase que hereda de Model         --->>>  TABLA

Field instance 	    Column on a table               # Atributos (Campos) de la clase        --->>>  COLUMNA

Model instance 	    Row in a database table         # Instancia de la clase (objeto)        --->>>  FILA

"""




# La documentacion de peewee nos muestra un codigo de ejemplo:


from peewee import *

db = SqliteDatabase('people.db')    # Variable "db", que indica que la base de datos es de Sqlite y se llama "people.db"

class Person(Model):                # Clase (Tabla). Hereda de Model, osea, se convierte en una tabla
    name = CharField()              # Atributo (Columna), Tipo CharField, Campo de Caracteres
    birthday = DateField()          # Atributo (Columna), Tipo DateField, Campo de Fecha
    is_relative = BooleanField()    # Atributo (Columna), Tipo BooleanField, Campo Booleano 

    class Meta:
        database = db               # Indicamos que este modelo usa la base de datos llamada "people.db"

#       database = db  This model uses the "people.db" database.


# Aqui la clase PERSON hereda de MODEL, es decir, SE CONVIERTE EN UNA TABLA DE LA BASE DE DATOS.

# Los CAMPOS (ATRIBUTOS) son NAME y BIRTHDAY. Cada uno de estos atributos SE CONVIERTEN EN UNA COLUMNA de nuestra tabla (Clase). 

# El Campo (Columna) NAME es de tipo CHARFIELD, osea, Campo de Caracteres 

# El Campo (Columna) BIRTHDAY es de tipo DATEFIEL, osea, Campo de tipo Fecha

# El Campo (Columna) IS_RELATIVE es tipo BOOLEANFIELD, osea, Campo Booleano

# Peewee tiene muchos tipos de datos diferentes para las tablas, estos de arriba son solo unos ejemplos.


# IMPORTANTE! Cada uno de los modelos (Clase que hereda de Model y se convierte en una table).

# Tiene una clase META, que es una clase dentro de nuestra clase, que contiene detalles de la conexion a la base de datos,
# Como se indexa la tabla, etc.

# Pero lo mas importante es que en esta clase (Tabla) podemos señalar que la base de datos de esta clase (tabla) que es un modelo
# 
# Va a ser "db", que como vemos mas arriba es una variable, que nos dice que es una base de datos de Sqlite, que se llama people.db


# Como vemos (Ver diagrama.jpg), tenemos una tabla, llamada "Person", que contiene 3 filas (Atributos de la clase)
# Que son "name", "birthday" y  "is_relative". 

# Cada vez que creemos una instancia nueva, y le agreguemos valores a los atributos, Seria una nueva Fila en nuestra base de datos


class Person(Model):                # Clase (Tabla). Hereda de Model, osea, se convierte en una tabla
    name = CharField()              #
    birthday = DateField()          # Los ATRIBUTIS de la instancia se convierten en FILAS.
    is_relative = BooleanField()    # Pero los VALORES de esos atributos se convierten en COLUMNAS

    class Meta:
        database = db        




db = SqliteDatabase('people.db')    # La variable "db", contiene una base de datos de Sqlite, llamada "people.db"

class Person(Model):                # La clase "Person", hereda de "Model", se convierte en una tabla en nuestra DB

# El nombre de la tabla se escribe en MINUSCULA (Aunq con la primera letra mayuscula), y en SINGULAR, "Person" y no "Persons"    

class Person(Model):
    name = CharField()              # El VALOR de este atributo (campo), es de tipo CAMPO DE CARACTER
    birthday = DateField()          # El VALOR de este atributo (campo), es de tipo CAMPO DE FECHA
    is_relative = BooleanField()    # El VALOR de este atributo (campo), es de tipo CAMPO BOOLEANO


# Ejecutamos el codigo y si no manda ningun error esta todo correcto :D

# Pero notamos que NO se crea ninguna base de datos ni tabla ni nada, esto pasa por que no hay ningun archivo .db
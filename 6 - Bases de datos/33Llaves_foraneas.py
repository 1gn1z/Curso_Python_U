
# Vamos a crear otro modelo para nuestra base de datos, llamada "pet", para las mascotas :3

from peewee import *


db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta():
        database = db

class Pet(Model):
    owner = ForeignKeyField()
    name = CharField()
    animal_type = CharField()


def create_n_connect():
    db.connect()
    db.create_tables([Person],safe=True)


create_n_connect()


# Vamos a agregar un atributo a la clase "Pet", llamada "owner". Y fijemonos en el tipo de dato "ForeignkeyField()"
# Tambien tiene un nombre, que  sera tipo CharField()
# Y finalmente añadimos que tipo de animal es animal_type, que sera tambien tipo CharField()

# El owner tiene tipo de dato LLAVE FORANEA, "ForeignKeyField". 

# Una llave foranea es un campo en una tabla que representa a una fila de otra tabla.

owner = ForeignKeyField(Person, related_name='pets')

# En nuestro caso, la llave foranea representa a una fila de la tabla "Person", que esa misma persona es la dueña de la mascota
# Por ejemplo bob, ana, etc.

# La llave foranea apunta a nuestra tabla de "Person", 


owner = ForeignKeyField(Person, related_name='pets') # El campo "owner", apunta hacia una fila de la tabla "Person", que es el dueño

# Y tambien tenemos que AÑADIR LA NUEVA TABLA:

    db.create_tables([Person,Pet],safe=True)


# Al correr me daba error, le añadi el class meta al nuevo modelo y ya no me mando error.

# Para ver que todo ha sido creado SIN HACER CONSULTAS aun.

# Simplemente, en la consola, escribimos "Sqlite3", espacio, y el nombre de la base de datos que queremos ver


# TUVE QUE INSTALAR SQLITE3 Y AÑADIR LA RUTA (C:sqlite) A LAS VARIABLES DE ENTORNO

# Los archivos se bajan de: https://www.sqlite.org/download.html

# Los archivos son:

"""
Precompiled Binaries for Windows
	sqlite-dll-win32-x86-3320300.zip
(486.71 KiB) 		32-bit DLL (x86) for SQLite version 3.32.3.

sqlite-tools-win32-x86-3320300.zip
(1.75 MiB) 		A bundle of command-line tools for managing SQLite database files, including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program.
"""

# Los descomprimi en C:\sqlite

# Y contiene:

# -sqlite3.exe
# -sqlite3.def
# -sqldiff.exe
# -sqlite3.def
# -sqlite3.dll

# Tutorial que segui:
# http://www.w3big.com/es/sqlite/sqlite-installation.html

# Ahora si, escribimos "Sqlite3", espacio, y el nombre de la base de datos, en este caso "people.db" (EN LA CONSOLA)

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite>

# Ya estando en la consola, podemos PONER COMANDOS para CONSULTAR NUESTRA DB, por ejemplo, Vamos a consultar las TABLAS

# Usando el comando PUNTO.TABLES, nos mostrará TODAS LAS TABLAS que tenemos en nuestra base de datos:

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.

sqlite> .tables     # Comando para consultar las tablas.
person  pet         # Las tablas existenten en nuestra DB

sqlite>


# Ahora vamos a ver las COLUMNAS de nuestra DB, es decir, queremos saber que CAMPOS tienen.
# Simplemente escribimos PUNTO SCHEMA, seguido del NOMBRE DE CLASE (TABLA).

.schema person


sqlite> .schema person
CREATE TABLE IF NOT EXISTS "person" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL
, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL);
sqlite>

# NOTA. No se por que dice que crea la tabla "person" si no existe.

# Indica que tiene un "id" como Primary key, 

# Tiene el nombre "name" que es de tipo "VARCHAR", osea variable de caracteres. Como vemos entre parentesis, si no se le asigna
# un maximo de caracteres, se le asigna un maximo de 255 caracteres.

# Tiene un "birthday", que es de tipo "DATE"

# Y un "is_relativa", que es de tipo "INTEGER"


# Ahora vamos a consultar las COLUMNAS de la CLASE (TABLA) "Pet".

sqlite> .schema pet
CREATE TABLE IF NOT EXISTS "pet" ("id" INTEGER NOT NULL PRIMARY KEY, "owner_id" INTEGER NOT NULL, "n
ame" VARCHAR(255) NOT NULL, "animal_type" VARCHAR(255) NOT NULL, FOREIGN KEY ("owner_id") REFERENCES
 "person" ("id"));
CREATE INDEX "pet_owner_id" ON "pet" ("owner_id");
sqlite>


# Igual tiene un "id"

# Tiene un "owner_id", que es de tipo "INTEGER"
# Pero ademas, mas abajo, indica que es tambien una "FOREIGN KEY" (Llave foranea).
# Y tambien indica que hace REFERENCIA al "ID" de la tabla "PERSON"

# Tiene un "name", que es de tipo "VARCHAR", con maximo de 255 caracteres (por default), ya que no le asignamos limite de caracteres

# Tiene un "animal_type", igual de tipo "VARCHAR", con maximo de 255 caracteres (por default), ya que no le asignamos limite de caracteres



>Sqlite3 people.db                                  # Consultamos con Sqlite3 la base de datos (people.db)

SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.

sqlite> .tables                                     # Consultamos las TABLAS que tiene la base de datos (people.db)
person  pet


sqlite> . schema person                             # Consultamos las COLUMNAS que tiene la TABLA (person)


CREATE TABLE IF NOT EXISTS "person" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL
, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL);


sqlite> .schema pet                                 # Consultamos las COLUMNAS que tiene la TABLA (pet)


CREATE TABLE IF NOT EXISTS "pet" ("id" INTEGER NOT NULL PRIMARY KEY, "owner_id" INTEGER NOT NULL, "n
ame" VARCHAR(255) NOT NULL, "animal_type" VARCHAR(255) NOT NULL, FOREIGN KEY ("owner_id") REFERENCES
 "person" ("id"));
CREATE INDEX "pet_owner_id" ON "pet" ("owner_id");

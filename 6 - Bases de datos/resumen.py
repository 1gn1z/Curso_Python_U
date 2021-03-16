"""
Object 	            Corresponds to…

Model class 	    Database table                  # Una clase que hereda de Model         --->>>  TABLA

Field instance 	    Column on a table               # Atributos (Campos) de la clase        --->>>  COLUMNA

Model instance 	    Row in a database table         # Instancia de la clase (objeto)        --->>>  FILA






class Person(Model):                    --->>> MODELO DE CLASE                              ==      TABLA


    name = CharField()                  --->>> ATRIBUTOS                                    ==      COLUMNAS                     
    birthday = DateField()              
    is_relative = BooleanField()        #### name, birthdat, is_relative


    name = CharField()                  -->>> INSTANCIAS (Tipo de dato del atributo)        ==      FILAS
    birthday = DateField()              
    is_relative = BooleanField()        #### CharField(), DateField(), BooleanField()
    
    
"""




#-------------------------------------------------IMPORTACION DE PEEWEE-------------------------------------------------

from peewee import *        # Primero que nada importar peewee

#____________________________________________________________________________________________________________





#-------------------------------------------------CREACION DE LA BASE DE DATOS-------------------------------------------------

db = SqliteDatabase('basededatos.db')   # Creacion de base de datos con Sqlite3, guardada en una variable

#____________________________________________________________________________________________________________





#-------------------------------------------------CREACION DE MODELOS-------------------------------------------------

class Person(Model):                    # Creacion de un MODELO (CLASE)             --> TABLA
    name = CharField()                  #
    birthday = DateField()              # ATRIBUTOS (CAMPOS) del MODELO (CLASE)     --> COLUMNAS
    is_relative = BooleanField()        #

    class Meta():                       # Todos los modelos deben tener esta clase
        database = db                   # Indicamos que este modelo usa la base de datos "basededatos.db"


class Pet(Model):                       # Creacion de un MODELO (CLASE)             --> TABLA
    owner = ForeignKeyField()           #
    name = CharField()                  # ATRIBUTOS (CAMPOS) del MODELO (CLASE)     --> COLUMNAS
    animal_type = CharField()           #

    class Meta():                       # Todos los modelos deben tener esta clase
        database = db                   # Indicamos que este modelo usa la base de datos "basededatos.db"


"""
class Person(Model):
    name = CharField()              # El VALOR de este atributo (campo), es de tipo CAMPO DE CARACTER
    birthday = DateField()          # El VALOR de este atributo (campo), es de tipo CAMPO DE FECHA
    is_relative = BooleanField()    # El VALOR de este atributo (campo), es de tipo CAMPO BOOLEANO  
"""      
#____________________________________________________________________________________________________________





#---------------------------------------------CREACION Y CONEXION DE LA BASE DE DATOS---------------------------------------------


def create_n_connect():     
    db.connect()  

#____________________________________________________________________________________________________________




#---------------------------------------------CREACION DE TABLAS---------------------------------------------

def create_n_connect():
    db.connect()
    db.create_tables([Person],safe=True)       # Creacion de las TABLAS



    db.create_tables([Person,Pet],safe=True)    # No olvidar AÑADIR las nuevas tablas.


#____________________________________________________________________________________________________________




#-------------------------------------------------LLAVES FORANEAS-------------------------------------------------


# Una llave foranea es un campo en una tabla que representa a una fila de otra tabla. (Ver linea 43)

owner = ForeignKeyField()


# La llave foranea apunta a otra tabla, en este caso llamada "Person"
# En nuestro caso, la llave foranea representa a una fila de la tabla "Person", que es la misma persona es dueña de la mascota


owner = ForeignKeyField(Person, related_name='pets')

#____________________________________________________________________________________________________________






#---------------------------------------------CONSULTA DE TABLAS CON SQLITE3---------------------------------------------


# En consola llamamos al ARCHIVO .py.

# Si NO marca error, podemos seguir con la consulta.

# En consola escribimos "Sqlite3 nombre_de_la_base_de_datos.db"


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db    <<<--- Archivo .db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.

sqlite> .tables     <<<--- Comando para consultar las tablas.
person  pet         <<<--- Las tablas existenten en nuestra DB

#____________________________________________________________________________________________________________




#---------------------------------------------CONSULTA DE COLUMNAS CON SQLITE3---------------------------------------------

# Dentro del Sqlite3 escribimos:

.schema person      # <<<--- .SCHEMA, ESPACIO, NOMBRE DE LA TABLA


sqlite> .schema person
CREATE TABLE IF NOT EXISTS "person" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL
, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL);
sqlite>


# Voy a ordenar los datos para que sea mas legible:


sqlite> .schema person
CREATE TABLE IF NOT EXISTS                       # Crear la tabla si no existe    
"person" ("id" INTEGER NOT NULL PRIMARY KEY,     # "PERSON", con un "ID" (IDentificador) INT (Entero), como "PRIMARY KEY" (Llave primaria)
"name" VARCHAR(255) NOT NULL,                    # "NAME", *1er ATRIBUTO (CAMPO)*. VARiable de CHARacter, 255 caracteres maximo por default
"birthday" DATE NOT NULL,                        # "BIRTHDAY" *2o ATRIBUTO (CAMPO)*. Tipo de dato "DATE" (FECHA)           
"is_relative" INTEGER NOT NULL);                 # "IS_RELATIVE" *3er ATRIBUTO (CAMPO)*. Tipo de dato "INTEGER" (ENTERO)
sqlite>

#____________________________________________________________________________________________________________





#---------------------------------------------GUARDANDO REGISTROS---------------------------------------------

# Creamos una FUNCION, llamada por ejemplo "create_family_members"

def create_family_members():

# Esta funcion indica con el nombre que sera para crear registros en nuestra tabla Person, y sera para miembros de la familia


# Vamos a crear una VARIABLE de la person que queramos registrar, por ejemplo un tio llamado Tommy

# Creamos una nueva INSTANCIA DE LA CLASE PERSON, llamada "uncle_tommy"



uncle_tommy = Person()



# Dentro de los parentesis le vamos a pasar los ATRIBUTOS (CAMPOS), que se convierten en COLUMNAS.


uncle_tommy = Person(name='Tommy')


# Le vamos a pasar ahora la fecha de nacimiento, pero NO podemos hacerlo asi:


    uncle_tommy = Person(name="Tommy",birthday="2000-11-11")
# Por que el cumpleaños tambien es una cadena de texto, y en la consulta que hicimos Sqlite3 dice que es de tipo DATE, no VARCHAR 


# Asi que tenemos que IMPORTAR la funcion DATE de DATETIME:


from datetime import date


# Ahora si podemos pasarle el cumpleaños, como una fecha, que como nos dice Sqlite3 es tipo DATE.


    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11))


# Ahora si podemos agregar el ultimo campo "is_relative", que como es de tipo BOOLEANO, de valor tendra TRUE o FALSE.


    uncle_tommy = Person(name="Tommy",birthday=date(2000,11,11),is_relative=TRUE)


# SIEMPRE, debemos llamar a las funciones:


create_family_members()


                ########## OTRA FORMA (MAS SENCILLA) DE CREAR REGISTROS, CON EL METODO "CREATE" ##########


grandma_lupe = Person.create()      <<<--- Create (Metodo de la clase MODEL)


# Ya simplemente le pasamos los parametros de los atributos de nuestra clase person

grandma_lupe = Person.create(name='Ana',birthday=date(1960,10,10),is_relative='False')

#____________________________________________________________________________________________________________





#---------------------------------------------CONSULTANDO REGISTROS---------------------------------------------

# Como siempre primero tenemos que ejecutar el archivo .py


# Si no hay errores, significa que esta todo correcto.


# A continuacion vamos a consultar nuestra base de datos con Sqlite3


Sqlite3 people.db


# Y vamos a SELECCIONAR TODOS LOS REGISTROS DE UNA TABLA (Person):

sqlite> select * from person;       # <<<--- Seleccionamos (select) TODO (*) de (from) la tabla "person", PUNTO Y COMA AL FINAL
1|Tommy|2000-11-11|1                # <<<--- Vemos el registro que tenemos actualmente en la tabla:
sqlite>


1               |   Tommy   |       2000-11-11       |         1  

LLAVE PRIMARIA      NOMBRE          CUMPLEAÑOS          Campo "is_relative"
(PRIMARY KEY)    Campo "name"     Campo "birthday"      1=TRUE | 0=FALSE





#-------------------------------------------------LLAVES FORANEAS 2 ASIGNACION-------------------------------------------------


# Creamos por ejemplo una instancia para una mascota de, por ejemplo, el tio tommy



def create_family_members():
    tommys_dog = Pet.create(owner=uncle_tommy,name='Rayray',aninal_type='Dog')


# Como vemos, la variable del "owner" (dueño), APUNTA A LA VARIABLE DEL TIO TOMMY "uncly_tommy"


# Aqui mismo le registraremos una mascota a la abuelita Lupe :3 un canario llamado Quetz


    lupes_bird = Pet.create(owner=grandma_lupe,name='Quetz',animal_type='Bird')



# Consultamos la tabla Pet con Sqlite3


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> select * from pet;      <<<--- Seleccionamos TODO de la tabla "Pet"
1|6|Rayray|Dog                  <<<--- Nombre: Rayray, Tipo de animal: Perro
2|7|Quetz|Bird                  <<<--- Nombre: Quetz, Tipo de animal: Ave


# Como vemos, al principio INDICA LA LLAVE PRIMARIA de cada instancia.
# Y despues indica LA LLAVE FORANEA, que como vemos apunta a UNA INSTANCIA DE OTRA TABLA (De la tabla Person)




# ************************************************TABLA PERSON**************************************************



        6           |       Tommy               |           2000-11-11                          |       1
        7           |       Lupe                |           1960-10-10                          |       0 

  LLAVE PRIMARIA           NOMBRE                            CUMPLEAÑOS                            Campo "is_relative"        
    LLAVE KEY       Campo "name" de la tabla PERSON     Campo "birthday" de la tabla PERSON        TRUE=1 | FALSE=0 





# ************************************************TABLA PET***********************************************


        1           |       6           |       Rayray                      |       Dog      

        2           |       7           |       Quetz                       |       Bird 

LLAVE PRIMARIA       LLAVE FORANEA              NOMBRE                          TIPO DE ANIMAL
PRIMARY KEY           FOREING KEY        Campo "name" de la tabla PET       "animal_type" de la tabla PET




1|Tommy|2000-11-11|1        # REGISTROS DUPLICADOS
2|Tommy|2000-11-11|1
3|Lupe|1960-10-10|0 
4|Tommy|2000-11-11|1
5|Lupe|1960-10-10|0


6|Tommy|2000-11-11|1        # LLAVE PRIMARIA 6, QUE ES LA LLAVE FORANEA 6 DE LA TABLA PET, es decir, "Tommy" es dueño de "Rayray"
7|Lupe|1960-10-10|0         # LLAVE PRIMARIA 7, QUE ES LA LLAVE FORANEA 7 DE LA TABLA PET, es decir, "Lupe" es dueña de "Quetz"

 #____________________________________________________________________________________________________________






#-------------------------------------------------ACTUALIZANDO REGISTROS-------------------------------------------------


# Solo tenemos que REASIGNAR el CAMPO (ATRIBUTO) que queramos modificar:


tommys_dog.name = "Firulais"        # Accedemos a su atributo NAME, y lo REASIGNAMOS (ACTUALIZAMOS)
tommys_dog.save()                   # Aqui si necesitamos GUARDAR para que se actualize nuestro registro


# Como vemos, aqui SI TENEMOS QUE GUARDAR 

# Ahora ejecutamos de nuevo el archivo .py, y consultamos todos los registros de la tabla Pet en Sqlite3


9|14|Firulais|Dog
10|15|Quetz|Bird


# Como vemos, el registro del perro ya ha sido actualizado en su campo nombre.

 #____________________________________________________________________________________________________________





#-------------------------------------------------OBTENIENDO REGISTROS-------------------------------------------------

# Para obtener TODOS los registros, lo haremos como con las listas, CON UN CICLO FOR:

# Vamos a definir una funcion que devuelva TODOS los registros, llamada por ejemplo "get_family_members".


def get_family_members():


# Y como ya dijimos, usaremos un ciclo FOR que itere todos los registros:


def get_family_members():
    for person in Person.select():      # El nombre de la clase CON MAYUSCULA.    


# Como vemos en las consultas de Sqlite3, usamos el metodo SELECT para obtener todos los registros de esa tabla.
# Asi que haciendo esto nos devolvera TODOS los registros de nuestra tabla (Person)

# Finalmente solo llamamos un print, Y le añadimos los parametros (Nombre, Cumpleaños, y is_relative), usando la funcion FORMAT



print(f'Nombre: {person.name}. Fecha de nacimiento: {person.birthday}. Es familiar? {person.is_relative}')


# NO OLVIDAR LLAMAR LAS FUNCIONES!


get_family_members()

 #____________________________________________________________________________________________________________





#-------------------------------------------------OBTENIENDO UN SOLO REGISTRO-------------------------------------------------


# Para llamar a UN SOLO REGISTRO en particular vamos a hacer otra funcion

def get_family_member_birthday():   # Puede ser cualquier parametro, no necesariamente el cumpleaños


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



get_family_member_birthday('Rosa')  # Aqui especificamos el parametro que deseamos usar (en este caso el nombre)


def get_family_member_birthday(name):   # Acepta el parametro
    family_member = Person.select().where(Person.name==name).get()
    print(f'{name} cumple el: {family_member.birthday}')

get_family_member_birthday('Rosa')

 #____________________________________________________________________________________________________________








#-------------------------------------------------OBTENIENDO UN SOLO REGISTRO II-------------------------------------------------


# Vamos a ver una forma ABREVIADA de obtener un UNICO REGISTRO de nuestras tablas, en lugar de hacer esto:


def get_family_member_birthday(name):
    family_member = Person.select().where(Person.name==name).get()      #<<<--- Esto es muy largo y poco legible
    print(f'{name} cumple el: {family_member.birthday}')


# Como ya sabemos que es un unico registro, lo unico que debemos hacer es:


def get_family_member_birthday(name):

#    family_member = Person.select().where(Person.name==name).get()      #<<<--- Esto es muy largo y poco legible

# Este metodo es mejor para obtener UN SOLO REGISTRO, poniendo como parametro de la funcion el nombre que deseamos consultar

    family_member = Person.get(Person.name==name)       # Esto devuelve un solo registro, el que corresponda a los parametros
                                                        # que le pusimos, en este caso el NOMBRE

    print(f'{name} cumple el: {family_member.birthday}')


# El resultado final queda asi:


def get_family_member_birthday(name):                    # <<<--- Acepta un Parametro.

    family_member = Person.get(Person.name==name)        # <<<--- Mas sencillo usar el metodo GET y que el nombre sea igual (Person.name==name)
    print(f'{name} cumple el: {family_member.birthday}') # <<<--- Simplemente imprimir el nombre y el cumpleaños con format.


 #____________________________________________________________________________________________________________




#-------------------------------------------------BORRANDO (VARIOS) REGISTROS-------------------------------------------------


# Vamos a crear una FUNCION que ACEPTE UN PARAMETRO, por ejemplo "delete_pet(name)"


def delete_pet(name):


# Ahora hacemos una VARIABLE, que contenga el metodo DELETE de la clase PET (Metodo DELETE para eliminar varios registros).

query = Pet.delete()


# Tambien le vamos a pasar un where, donde le diremos los parametros que tiene que cumplir para que sean borrados:

query = Pet.delete().where(Pet.name=="")

# Y como queremos que se borren los "Firulais", le pasamos la variable que contiene el nombre

query = Pet.delete().where(Pet.name==name)


# Si lo dejamos asi no pasa nada, con las querys tipo DELETE, tenemos que decir EXPLICITAMENTE que queremos borrarlas,
# Esto lo hacemos con la funcion EXECUTE:

query = Pet.delete().where(Petn.name==name)     # Se pone la variable nombre, por que al llamar la funcion
query.execute()                                 # indicamos el nombre como tal



# Tenemos que ser cuidadosos por que puede BORRAR TODOS LOS REGISTROS, SI NO PONEMOS NINGUN PARAMETRO.

# Ya finalmente mandamos llamar a la funcion:


delete_pet('Firulais')


# Queremos saber cuantos registros fueron borrados, asi que vamos a MOSTRAR cuantos se eliminaron.


# Asi que vamos a guardar la ejecucion del query en una variable llamada "deletes_entries" (entradas borradas)

deletes_entries = query.execute()


# Y podemos mostrarlos con un print:

print(f'{deleted_entries} Registros borrados ')



# Tenemos 3 'Firulais', asi que nuestra funcion tiene que decir algo como "3 registros borrados"


C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>"peewee(clean_code).py"
Registros borrados: 3

# Correcto! :D

# Vamos a Sqlite3 para asegurarnos:

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> select * from pet;
1|6|Rayray|Dog
2|7|Quetz|Bird
3|8|Rayray|Dog
4|9|Quetz|Bird
5|10|Rayray|Dog
6|11|Quetz|Bird
7|12|Rayray|Dog
8|13|Quetz|Bird
10|15|Quetz|Bird
12|17|Quetz|Bird
14|19|Quetz|Bird

# Efectivamente ya se borraron los registros de Firulais ;D


def delete_pet(name):
    query = Pet.delete().where(Pet.name==name)
    deleted_entries = query.execute()
    print(f'Registros borrados: {deleted_entries}')



# Para borrar otros registros, simplemente volvemos a llamar la funcion, pero con el parametro "name", que queremos borrar


delete_pet('Quetz')

 #____________________________________________________________________________________________________________









#-------------------------------------------------BORRANDO UN SOLO REGISTRO-------------------------------------------------



# Para borrar un unico registro podemos usar el mismo metodo exactamente, reemplazando el nombre

# Pero si solo queremos BORRAR UN REGISTRO Y SOLAMENTE UN REGISTRO, asi nos aseguramos de no borrar nada mas.

def delete_pet(name):

    rayray = Pet.get(Pet.name == 'Rayray')          # <<<--- Usamos el metodo GET, para que se borre SOLO el registro que coincida 
                                                    # <<<--- con el nombre especificado "Rayray"

    deleted_entry = rayray.delete_instance()        # <<<--- Usamos una variable diferente (en singular)


    print(f'{deleted_entry} Registros borrados')


delete_pet('Quetz')


# Yo tuve que ejecutar el programa .py como 4 veces, ya que ELIMINABA DE UNO POR UNO.

 #____________________________________________________________________________________________________________

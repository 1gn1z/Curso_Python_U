# Si exploramos nuestras tablas, veremos MUCHOS registros duplicados, que no nos sirven de absolutamente nada:

"""
sqlite> .tables
person  pet
sqlite>
sqlite>
sqlite> select * from person;
1|Tommy|2000-11-11|1
2|Tommy|2000-11-11|1
3|Lupe|1960-10-10|0
4|Tommy|2000-11-11|1
5|Lupe|1960-10-10|0
6|Tommy|2000-11-11|1
7|Lupe|1960-10-10|0
8|Tommy|2000-11-11|1
9|Lupe|1960-10-10|0
10|Tommy|2000-11-11|1
11|Lupe|1960-10-10|0
12|Tommy|2000-11-11|1
13|Lupe|1960-10-10|0
14|Tommy|2000-11-11|1
15|Lupe|1960-10-10|0
16|Tommy|2000-11-11|1
17|Lupe|1960-10-10|0
18|Tommy|2000-11-11|1
19|Lupe|1960-10-10|0
20|Rosa|1960-10-10|0
sqlite>
sqlite>
sqlite> select * from pet;
1|6|Rayray|Dog
2|7|Quetz|Bird
3|8|Rayray|Dog
4|9|Quetz|Bird
5|10|Rayray|Dog
6|11|Quetz|Bird
7|12|Rayray|Dog
8|13|Quetz|Bird
9|14|Firulais|Dog
10|15|Quetz|Bird
11|16|Firulais|Dog
12|17|Quetz|Bird
13|18|Firulais|Dog
14|19|Quetz|Bird
sqlite>
"""


# Vamos a BORRAR VARIOS REGISTROS a la vez. Por ejemplo vamos a borrar los 3 registros de 'Firulais'

# Para hacerlo vamos a crear una funcion, llamada, por ejemplo: "delete_pet"

def delete_pet():

# Y aceptará un parametro, que sera el nombre:

def delete_pet(name):

# Ahora vamos a usar el METODO DELETE, por que queremos borrar varios registros.
# Vamos a declarar una variable que contenga el Metodo Delete de la Clase Pet.

query = Pet.delete()

# Tambien le vamos a pasar un where, donde le diremos los parametros que tiene que cumplir para que sean borrados:

query = Pet.delete().where(Pet.name=="")

# Y como queremos que se borren los "Firulais", le pasamos la variable que contiene el nombre

query = Pet.delete().where(Petn.name==name)


# Si lo dejamos asi no pasa nada, con las querys tipo DELETE, tenemos que decir EXPLICITAMENTE que queremos borrarlas,
# Esto lo hacemos con la funcion EXECUTE:

query = Pet.delete().where(Petn.name==name)     # Se pone la variable nombre, por que al llamar la funcion
query.execute()                                 # indicamos el nombre como tal


# Tenemos que ser cuidadosos por que puede BORRAR TODOS LOS REGISTROS, SI NO PONEMOS NINGUN PARAMETRO.

# Ya finalmente mandamos llamar a la funcion:

delete_pet('Firulais')


# Al ejecutar el query nos va a decir CUANTOS REGISTROS FUERON BORRADOS de nuestra DB.
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

# Vamos a borrar ahora a Quetz, simplemente reemplazamos su nombre en la llamada a la funcion

delete_pet('Quetz')


# Todo correcto :D

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>"peewee(clean_code).py"
Registros borrados: 7

C:\Users\1gn1z\Documents\CDPpythonU\6 - Bases de datos>Sqlite3 people.db
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> select * from pet;
1|6|Rayray|Dog
3|8|Rayray|Dog
5|10|Rayray|Dog
7|12|Rayray|Dog

# Vamo a borrar de una vez a Rayray

# Para borrar un unico registro podemos usar el mismo metodo exactamente, reemplazando el nombre

# Pero si solo queremos BORRAR UN REGISTRO Y SOLAMENTE UN REGISTRO, asi nos aseguramos de no borrar nada mas.


rayray = Pet.get(Pet.name == 'Rayray')
deleted_entry = rayray.delete_instance()
print(f'{deleted_entry} Registros borrados')


# Yo tuve que ejecutar el programa .py como 4 veces, ya que ELIMINABA DE UNO POR UNO.

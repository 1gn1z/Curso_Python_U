# Vamos a crear y conectarnos a nuestra base de datos.

# Ya tenemos el archivo donde la clase Person, que es un modelo, tendra los atributos (campos) que indican el nombre
# El cumpleños y si es pariente.

# Ademas, en la clase meta especificamos que nos conectaremos a la base de datos "db", que es de Sqlite, y se llama "peole.db"

# Pero al correr nuestro archivo NO se creo nada :(

# No se creo por que es necesario decirle a peewee que queremos crear esta base de datos.

# Para hacerlo creamos un metodo, y le decimos que nos conecte a la base de datos:

def create_n_connect():     # Metodo creado para, como indica su nombre, crear la base de datos y conectarnos a ella
    db.connect()            # Especificamos que nos conecte a nuestra base de datos,
    # esta es una variable, pero contiene la base de datos.

# Este metodo automaticamente, si detecta que no tenemos el archivo de base de datos (people.db), CREARA automaticamente la 
# base de datos por nosotros :D.
# 
# PERO! tenemos que decirle a la base de datos que queremos CREAR LAS TABLAS (Clases), de nuestros modelos.
# 
#

def create_n_connect():
    db.connect()
    db.createTables()      # Creacion de tablas (clases que se convierten en tablas) de nuestros modelos (en este caso Clase "Person")


# Y a esta funcion de "createTables()", le vamos a pasar una lista que contendra los modelos que queremos crear,
# En este caso queremos crear la tabla "Person" (Que es nuestra clase "Person", que se convierte en una tabla y hereda de Model)

def create_n_connect():
    db.connect()
    db.createTables([Person])


# Ya creada la funcion simplemente nos falta llamarla

create_n_connect()

# En nuestros archivos, vemos un nuevo archivo de BASES DE DATOS ya creado :D
# IMPORTANTE CORRER EL PROGRAMA CON LA CONSOLA DE WINDOWS

# Ya nos creo un archivo de base de datos llamado como le especificamos "people.db". Que contiene una tabla llamada "Person"


# Al profe le sale un error si intentamos correr el programa nuevamente, que dice que la base de datos ya existe.
# A mi no me sale el error y tampoco crea otro archivo de base de datos.

# Vamos a acceder a la ayuda de la base de datos Sqlite con la consola de python.

"""
>>> from peewee import *
>>> help(SqliteDatabase)
Help on class SqliteDatabase in module peewee:

class SqliteDatabase(Database)
 |  Method resolution order:
 |      SqliteDatabase
 |      Database
 |      _callable_context_manager
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, database, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate
 |
 |  aggregate(self, name=None, num_params=-1)
 |
 |  attach(self, filename, name)
 |
 |  begin(self, lock_type=None)
 |
 |  collation(self, name=None)
 |
 |  conflict_statement(self, on_conflict, query)
 |
 |  conflict_update(self, oc, query)
 |
 |  detach(self, name)
 |
 |  extract_date(self, date_part, date_field)
 |
 |  from_timestamp(self, date_field)
 |
 |  func(self, name=None, num_params=-1)
 |
 |  get_binary_type(self)
 |
 |  get_columns(self, table, schema=None)
 |
 |  get_foreign_keys(self, table, schema=None)
 |
 |  get_indexes(self, table, schema=None)
 |
 |  get_primary_keys(self, table, schema=None)
 |
 |  get_tables(self, schema=None)
 |
 |  get_views(self, schema=None)
 |
 |  init(self, database, pragmas=None, timeout=5, **kwargs)
 |
 |  load_extension(self, extension)
 |
 |  pragma(self, key, value=<object object at 0x0124B950>,
 |
 |  register_aggregate(self, klass, name=None, num_params=-
 |
 |  register_collation(self, fn, name=None)
 |
 |  register_function(self, fn, name=None, num_params=-1)
 |
 |  register_table_function(self, klass, name=None)
 |
 |  register_window_function(self, klass, name=None, num_pa
 |
 |  table_function(self, name=None)
 |
 |  to_timestamp(self, date_field)
 |
 |  truncate_date(self, date_part, date_field)
 |
 |  unload_extension(self, extension)
 |
 |  unregister_aggregate(self, name)
 |
 |  unregister_collation(self, name)
 |
 |  unregister_function(self, name)
 |
 |  unregister_table_function(self, name)
 |
 |  unregister_window_function(self, name)
 |
 |  window_function(self, name=None, num_params=-1)
 |
 |  -------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  cache_size
 |
 |  foreign_keys
 |
 |  journal_mode
 |
 |  journal_size_limit
 |
 |  mmap_size
 |
 |  page_size
 |
 |  read_uncommitted
 |
 |  synchronous
 |
 |  timeout
 |
 |  wal_autocheckpoint
 |
 |  -------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  field_types = {'BIGAUTO': 'INTEGER', 'BIGINT': 'INTEGER
 |
 |  index_schema_prefix = True
 |
 |  limit_max = -1
 |
 |  operations = {'ILIKE': 'LIKE', 'LIKE': 'GLOB'}
 |
 |  server_version = (3, 14, 2)
 |
 |  truncate_table = False
 |
 |  -------------------------------------------------------
 |  Methods inherited from Database:
 |
 |  __enter__(self)
 |
 |  __exit__(self, exc_type, exc_val, exc_tb)
 |
 |  atomic(self, *args, **kwargs)
 |
 |  batch_commit(self, it, n)
 |
 |  bind(self, models, bind_refs=True, bind_backrefs=True)
 |
 |  bind_ctx(self, models, bind_refs=True, bind_backrefs=Tr
 |
 |  close(self)
 |
 |  commit(self)
 |
 |  connect(self, reuse_if_open=False)
 |
 |  connection(self)
 |
 |  connection_context(self)
 |
 |  create_tables(self, models, **options)
 |
 |  cursor(self, commit=None)
 |
 |  default_values_insert(self, ctx)
 |
 |  drop_tables(self, models, **kwargs)
 |
 |  execute(self, query, commit=<object object at 0x0124B95
 |
 |  execute_sql(self, sql, params=None, commit=<object obje
 |
 |  get_context_options(self)
 |
 |  get_noop_select(self, ctx)
 |
 |  get_sql_context(self, **context_options)
 |
 |  in_transaction(self)
 |
 |  is_closed(self)
 |
 |  is_connection_usable(self)
 |
 |  last_insert_id(self, cursor, query_type=None)
 |
 |  manual_commit(self)
 |
 |  pop_transaction(self)
 |
 |  push_transaction(self, transaction)
 |
 |  random(self)
 |
 |  rollback(self)
 |
 |  rows_affected(self, cursor)
 |
 |  savepoint(self)
 |
 |  sequence_exists(self, seq)
 |
 |  session_commit(self)
 |
 |  session_rollback(self)
 |
 |  session_start(self)
 |
 |  table_exists(self, table_name, schema=None)
 |
 |  top_transaction(self)
 |
 |  transaction(self, *args, **kwargs)
 |
 |  transaction_depth(self)
 |
 |  -------------------------------------------------------
 |  Data and other attributes inherited from Database:
 |
 |  commit_select = False
 |
 |  compound_select_parentheses = 0
 |
 |  context_class = <class 'peewee.Context'>
 |
 |
 |  for_update = False
 |
 |  nulls_ordering = False
 |
 |  param = '?'
 |
 |  quote = '""'
 |
 |  returning_clause = False
 |
 |  safe_create_index = True
 |
 |  safe_drop_index = True
 |
 |  sequences = False
 |
 |  -------------------------------------------------------
 |  Methods inherited from _callable_context_manager:
 |
 |  __call__(self, fn)
 |      Call self as a function.
 |
 |  -------------------------------------------------------
 |  Data descriptors inherited from _callable_context_manag
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 """

 # Como vemos nos da una lista gigante de la ayuda de todos los metodos de SqliteDatabase
 # Vemos algunos metodos que ya usamos como "connect" (linea 197) y "create_tables" (linea 203)

 # Es una forma sencilla para buscar algo rapido.

 # El error que le salia al profe es que, al parecer en una version anterior de peewee, la funcion "create_tables"
 # tomaba 3 parametros (self, models, safe=False)

 # Ese safe=False esta activado asi por defecto, si peewee detecta que la tabla ya existe va a crashear

 # Para evitar eso tenemos que pasar un segundo parametro indicando que es True:

 db.create_tables([Person],safe=True)

 # En mi caso ese safe NO viene, la ayuda de peewee en la version que yo ocupo es:


create_tables(self, models, **options)

# Al añadirle el safe=True TAMPOCO da ningun error asi que lo dejare asi.
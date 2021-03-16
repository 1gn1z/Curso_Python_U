

# Aprenderemos una nueva forma de inicializar instancias de las clases

# Si necesitamos ayuda de alguna clase podemos escribir "help" y el nombre de la clase (Desde la consola:)
"""
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
"""

# Como vemos, tenemos muchos metodos, vamos a centrarnos en este:

# |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
# |      in the keyword argument list.  For example:  dict(one=1, two=2)

# Tenemos una forma mas de inicializar diccionarios.

# Dice que DICT(**kwargs) (LINEA 128) Inicializa un nuevo diccionario a partir de pares de nombre y valor en la lista de argumentos
# Por ejemplo (Linea 129) dict(uno=1, dos=2)

# Hasta este momento conociamos 2 formas de hacer un diccionario:

# Uno creando una lista separada por coma de pares "KEY:VALUE," entre LLAVES {}

diccionario = {"uno":1,"dos":2,"tres":3}

# La otra forma es con la funcion DICT:
# SIN COMILLAS el texto, y poniendo simbolo igual = para asignar el valor

# Por alguna razon el IDLE de python me manda "TypeError: 'dict' object is not callable"
# Lo hice directo desde el cmd y ningun problema

>>> dias = dict(lunes=1,martes=2,miercoles=3,jueves=4,viernes=6)
>>> dias
{'lunes': 1, 'martes': 2, 'miercoles': 3, 'jueves': 4, 'viernes': 6}

# Igual tenemos pares de llave y valor. llave(lunes):(=)valor1, llave(martes):(=)valor2, etc.

# Como vemos, las llaves seran GENERADAS COMO CADENAS ('lunes' 'martes' etc.)

# LOS VALORES los podemos poner de todo tipo, int,str,float,boolean, etc. LOS VALORES SI PUEDEN SER OTRO TIPO DE DATO.
# PERO! con la funcion DICT TENEMOS QUE PONER LAS LLAVES SIN COMILLAS NI NADA ok. Si no, nos arroja un error:

>>> nums = dict("tres"=4,)
SyntaxError: keyword can't be an expression

# Dice que una palabra no puede ser una expresion. Tenemos que poner las llaves SIN COMILLAS:

>>> nums = dict("tres"=4,)                          # MAL! CON COMILLAS MAL
SyntaxError: keyword can't be an expression

>>> nums = dict(tres=3,cuatro=4)                    # BIEN! SIN COMILLAS BIEN!
>>> nums
{'tres': 3, 'cuatro': 4}
>>>


# PERO para poder acceder a un elemento del diccionario SI TENEMOS QUE PONER LAS COMILLAS.

>>> dias = dict(lunes=1,martes=2,miercoles=3,jueves=4,viernes=6)
>>> dias["lunes"]
1

# A este metodo se le conoce como DESEMPAQUETAR DICCIONARIOS (Dictionary unpacking)

# Y tambien los podemos usar para crear instancias de nuestras clases.

# Como vemos en nuestra clase Player, tenemos varios atributos como hit_points, mana, vocation, etc.

class Player:

    def __init__(self,hit_points,mana,vocation,hechizo):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo


# Y cuando los escribimos en el main tenemos que recordar que signifca cada uno de los parametros de la instancia:

sorcerer = Player(40,80,"Sorcerer","Igne fulgur")

# Tenemos que recordar que el 1er parametro en la instancia "sorcerer" es "hit_points", el segundo "mana", el 3o "vocation", etc.

# No podemos cambiar el orden xq podemos poner el hechizo donde va la vcacion, el mana donde va la vida etc.

# Para usar el DESEMPAQUETAMIENTO de los diccionarios con las clases, si recordamos como lo representan con *kwargs:

dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

# borramos todo de nuestro metodo init, EXCEPTO SELF, y escribimos **kwargs

    def __init__(self,**kwargs):

# Esto indica que podemos usar en desempaquetamiento de diccionario como argumentos.

# Ahora para los atributos podemos poner, en el valor de un atributo, kwargs.get("hit_points")

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points")

# Esta linea indica (216), que buscara en el diccionario que le pasemos (kwargs), el nombre del atributo, en este caso hit_points

# Si NO lo encuentra va a devolver NONE, pero no queremos que se asigne NONE, queremos poner un valor por defecto.

# Para poner un valor por defecto, el que queramos, simplemente ponemos una COMA y el valor que queramos que tenga:

# Igual podemos hacerlo para otros parametros:

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)   # En la asignacion de la llave SI SE USAN COMILLAS
        self.mana = kwargs.get("maná",50)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo", "Puff")

# OK, ahora si mandamos a imprimir a una instancia:

sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"')

print("\nEl Sorcerer tiene:\n")
print("Vida:",sorcerer.hit_points)
print("Maná:",sorcerer.mana)
print("Vocación:",sorcerer.vocation)
print("Hechizo:",sorcerer.lanzar_hechizo())


# Nos manda este error que dice:

TypeError: __init__() takes 1 positional argument but 5 were given

# Esto nos indica que estamos pasandole 5 argumentos, cuando solo podemos pasarle un diccionario.

# Tal vez no recordemos que significa cada uno de esos argumentos, asi que vamos a codificarlo con el nuevo metodo de los diccionarios
sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"')

# En lugar de pasarle SOLO LOS ARGUMENTOS, podemos pasarle un diccionario, asi sabremos en todo momentos que corresponde a que :)
# Sabremos mas facilmente que los hit_points valen 50, el mana vale 50, la vocatios es igual a No vocation, etc.

# RECORDAR QUE LAS LLAVES DE LOS DICCIONARIOS CON EL METODO DICT VAN SIN COMILLAS ok.

sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",hechizo='"Igne Fulgur"')

# Haciendo esto queda mas claro por que ya esta especificado a que atributo corresponde cada valor :D
# Ya podemos borrar esta asignacion anterior:
sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"')

# Hacemos lo mismo con el knight

knight = Player(hit_points=80,mana=20,vocation="knight",hechizo="Impetu")

#
#
#
#
class Player:

    def __init__(self,**kwargs):    # Llamamos a un diccionario con el metodo **kwargs
        # ESPECIFICAMOS LOS VALORES POR DEFECTO PARA TODAS LAS INSTANCIAS DE LA CLASE PLAYER
        # self.atributo = kwargs.get("llave",coma,"valor")
        self.hit_points = kwargs.get("hit_points",50)   # EN INIT SI SE PONEN LAS COMILLAS EN EL DICCIONARIO
        self.mana = kwargs.get("maná", 50)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo","Puff")

    def lanzar_hechizo(self):
        return self.hechizo 

# sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"') Esto lo eliminamos 

# por que ahora necesitamos especificar un diccionario en lugar de solamente los atributos    
# Asi con el diccionario en lugar de solo los atributos queda mucho mas claro :D xq ya sabemos
# que los hit_points valen 40, el mana 80, su vocation es Sorcerer, etc. 

# MODIFICACION DE LOS ATRIBUTOS DE LA INSTANCIA SORCERER ESPECIFICAMENTE

sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",hechizo="Igne fulgur")  # EN LA INSTANCIA NO SE PONEN LAS COMILLAS

print("\nEl Sorcerer tiene:\n")
print("Vida:",sorcerer.hit_points)
print("Maná:",sorcerer.mana)
print("Vocación:",sorcerer.vocation)
print("Hechizo:",sorcerer.lanzar_hechizo())

knight = Player(hit_points=80,mana=20,vocation="knight",hechizo="Impetu") # Recordar que con la funcion dict() NO SE USAN COMILLAS
     
print("\nEl Knight tiene:\n")
print("Vida:",knight.hit_points)
print("Maná:",knight.mana)
print("Vocación:",knight.vocation)
print("Hechizo:",knight.lanzar_hechizo())  


paladin = Player(hit_points=60,mana=40,vocation="Paladín",hechizo="Fortis magica")

print("\nEl Paladín tiene:\n")
print("Vida:",paladin.hit_points)
print("Maná:",paladin.mana)
print("Vocación:",paladin.vocation)
print("Hechizo:",paladin.lanzar_hechizo())  

druid = Player(hit_points=50,mana=80,vocation="Druida",hechizo="Anima mea")

print("\nEl Paladín tiene:\n")
print("Vida:",druid.hit_points)
print("Maná:",druid.mana)
print("Vocación:",druid.vocation)
print("Hechizo:",druid.lanzar_hechizo()) 

 # Si no especificamos algun atributo, SE PONE POR DEFECTO el que este en el diccionario (INIT)

 druid = Player(hit_points=50,mana=80,vocation="Druida"#hechizo no especificado)

 El Paladín tiene:

Vida: 50
Maná: 80
Vocación: Druida
Hechizo: Puff

# Otra ventaja es que ahora NO TIENEN QUE ESTAR EN ORDEN ESPECIFICO LOS ATRIBUTOS :)

class Player:

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)   # ATRIBUTOS CON COMILLAS,SEPARADOS POR COMAS
        self.mana = kwargs.get("mana",50)

druid = Player(hit_points=100,mana=100)                 # ATRIBUTOS EN LA INSTANCIA SIN COMILLAS, IGUAL SEPARADOS POR COMAS

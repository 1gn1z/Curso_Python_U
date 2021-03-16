# Cuando una clase hereda de otra, NO SOLO PUEDE SOBREESCRIBIR LOS ATRIBUTOS, TAMBIEN PUEDE SOBREESCRIBIR LOS METODOS 
# Y AGREGAR LOS PROPIOS

# Los sorcerer y druids, puedes curarse a si mismos, cuando escribimos cast_spell, devuelve la cadena del hechizo de la 
# instancia correspondiente.

# Para estas 2 clases, queremos que ademas del hechizo de esa, se imprima OTRO hechizo, le vamos a poner curacion.


# Para sobreescribir un metodo en python, en la clase que queramos modificar escribimos el metodo a sobreescribir:
# Queremos sobreescribir el metodo cast_spell es las clases del sorcerer y del druid, empezemos con el sorcerr

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Hechizo del Sorcerer"
    movement_speed = "20"

# Para sobreescribir metodos es tan sencillo como volver a escribir el metodo que queramos sobreescribir (no olvidar el SELF)
# y LA NUEVA DEFINICION DEL METODO

# En este caso como este metodo tiene el mismo nombre que el metodo de la clase padre (Player), de la que estamos heredando,
# SE LE DA PRIORIDAD a la nueva definicion que tenemos en la nueva clase.

# Simplemente agregamos unas llaves {} al inicio, para el metodo original, y como cadena el nuevo hechizo "curacion".
# Pero primero va el RETURN que indica que devuelve la funcion y cuando termina, y finalmente agregaremos, despues de las comillas
# .format(self.spell), que nos va a colocar en las llaves el primer hechizo, el de la clase original Player

def cast_spell(self):
    return "{} y Curación".format(self.spell)

# Este metodo lo copiamos y lo pegamos tambien en la clase del druida, que es donde la queremos :D    

# OBVIAMENTE! va con una indentacion en la clase donde lo queramos xq es parte de la clase ok :3

# Gracias a las llaves pusimos el hechizo original de esta clase "sorcerer" (Hechizo del Sorcerer), 
# 
# ademas del otro hechizo "Curación",

# PODEMOS HEREDAR DE MAS DE UNA CLASE, SIMPLEMENTE PONEMOS LAS CLASES SEPARADAS POR COMAS DENTRO DEL PARENTESIS:

class Troll_Champion(Troll,Player):
                    #clase1 clase2
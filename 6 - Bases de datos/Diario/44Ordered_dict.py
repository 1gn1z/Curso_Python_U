# Vamos a aprender sobre los DICCIONARIOS ORDENADOS

# Si recordamos, los DICCIONARIOS NO CONSERVAN EL ORDEN DADO POR NOSOTROS.

# No podemos saber en que forma se devolveran los elementos cuando lo llamemos o ejecutemos.

# Pero a veces necesitamos CONSERVAR EL ORDEN DE LOS DICCIONARIOS.


# En python existe una libreria para tener un diccionario ordenado.
# Tendremos que IMPORTAR, de una libreria llamada COLLECTIONS, la funcion llamada "ORDERERDICT":

from collections import OrderedDict


# Usaremos el orderedDict para almacenar los elementos de nuestro menu

# Justo abajo de nuestra base de datos haremos nuestro Diccionario Ordenado, para crearlo simplemente ponemos OrderedDict()


menu_items = OrderedDict()

# Para que conserve el orden de los datos, le pondremos UNA LISTA:

menu_items = OrderedDict([])

# Y la lista a su vez, tomara una serie de TUPLAS, que tendran LA LLAVE Y EL VALOR DE ESA LLAVE:


# Como vemos, ya no usamos opciones numericas (1 para x cosa, 2 para otra cosa), si no que usamos una LETRA.
# Y usamos una letra equitativa a lo que hara esa opcion, a para add entry, v de view, y d de delete:

menu_items = OrderedDict([
    ('a', 'add entry'),
    ('v', 'view entry'),
    ('d', 'delete entry')
])


# Esta es la forma en que creamos un diccionario ordenado :D
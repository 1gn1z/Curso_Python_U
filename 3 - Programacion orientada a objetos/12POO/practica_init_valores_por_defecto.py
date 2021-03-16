class Player:
  
    def __init__(self,hit_points=50,mana=50,vocation="No vocation",hechizo="Puff"):  # VALORES POR DEFECTO PARA TODAS LAS INSTANCIAS 
        self.hit_points = hit_points                                        # CREADAS EN ESTA CLASE
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo

    def lanzar_hechizo(self):
        return self.hechizo 

sorcerer = Player() # Aqui NO especificamos los atributos para que tome los que trae por defecto del metodo INIT
print()
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.hechizo)    # Si llamamos al atributo "hechizo", en lugar del metodo "lanzar_hechizo", devuelve el valor de hechizo por defecto

knight = Player(80,20,"knight","Impetu")    # Aqui SI podemos especificar los ATRIBUTOS MODIFICADOS QUE QUERAMOS
                                            # para esta instancia en particular
print()
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())


# RETO!!! Crear una nueva variable que sea otra instancia de player que sea un Paladin, que tenga 60 de vida
# 40 de mana, un hechizo diferente y de vocacion paladin obviamente xD.
class Player:

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)   # EN INIT SI SE PONEN LAS COMILLAS EN EL DICCIONARIO
        self.mana = kwargs.get("mana", 50)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo","Puff")

    def lanzar_hechizo(self):
        return self.hechizo 

# sorcerer = Player(40,80,"Sorcerer",'"Igne fulgur"') Esto lo eliminamos por que ahora necesitamos especificar

# un diccionario en lugar de solamente los atributos    
# Asi con el diccionario en lugar de solo los atributos queda mucho mas claro :D xq ya sabemos
# que los hit_points valen 40, el mana 80, su vocation es Sorcerer, etc. 
# MODIFICACION DE LOS ATRIBUTOS DE LA INSTANCIA SORCERER ESPECIFICAMENTE

sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",hechizo="Igne fulgur")  # EN LA INSTANCIA NO SE PONEN LAS COMILLAS

print("\nEl Sorcerer tiene:\n")
print("Vida:",sorcerer.hit_points)
print("Maná:",sorcerer.mana)
print("Vocación:",sorcerer.vocation)
print("Hechizo:",sorcerer.lanzar_hechizo())

knight = Player(hit_points=80,mana=20,vocation="knight",hechizo="Impetu")
     
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
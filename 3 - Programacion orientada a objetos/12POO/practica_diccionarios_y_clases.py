class Jugador:

    def __init__(self,**kwargs):
        self.vida = kwargs.get("vida",50)
        self.mana = kwargs.get("mana",50)
        self.vocacion = kwargs.get("vocacion","Sin vocación")
        self.magia = kwargs.get("magia","Puff")
        self.invocacion = kwargs.get("invocacion","None")
        self.ataque = kwargs.get("ataque","None")


mago = Jugador(vida=100,mana=200,vocacion="Mago",magia="Nube oscura",invocacion="Obesmuth",ataque="Golpe con bastón")

print("\nEL Mago tiene:\n")
print("Vida:",mago.vida)
print("Maná:",mago.mana)
print("Vocación:",mago.vocacion)
print("Magia:",mago.magia)
print("Invocación:",mago.invocacion)
print("Ataque:",mago.ataque)

caballero = Jugador(vida=200,mana=50,vocacion="Caballero",magia="Hechizo del rey Arturo",invocacion="Caballeros Templarios",ataque="Espadazo")

print("\nEl Caballero tiene:\n")
print("Vida:",caballero.vida)
print("Maná:",caballero.mana)
print("Vocación:",caballero.vocacion)
print("Magia:",caballero.magia)
print("Invocación:",caballero.invocacion)
print("Ataque:",caballero.ataque)

gnomo = Jugador(vida=100,mana=100,vocacion="Gnomo",magia="Poder mistico",invocacion="Angelus",ataque="Golpe con mazo")

print("\nEl Gnomo tiene:\n")
print("Vida:",gnomo.vida)
print("Maná:",gnomo.mana)
print("Vocación:",gnomo.vocacion)
print("Magia:",gnomo.magia)
print("Invocación:",gnomo.invocacion)
print("Ataque:",gnomo.ataque)


class Player:
    def __init__(self,**kwargs):
        self.ataque1 = kwargs.get("ataque1","None")
        self.ataque2 = kwargs.get("ataque2","None")
        self.magia1 = kwargs.get("magia1","Puff")
        self.magia2 = kwargs.get("magia2","Puff")
        self.huida = kwargs.get("huida","Huir")

jugador1 = Player(ataque1="Ráfaga",ataque2="Golpe múltiple",magia1="Rayo",magia2="Fuego",huida="Huyendo")

print(jugador1.ataque1)

class Jugador:
    def __init__(self,**kwargs):
        self.vida = kwargs.get("vida",50)
        self.mana = kwargs.get("mana",50)
        self.defensa = kwargs.get("defensa",50)
        self.vocacion = kwargs.get("vocacion","None")

mago = Jugador(vida=100,mana=200,defensa=100,vocacion="Mago")

print("\nEl mago tiene:\n")
print("Vida:",mago.vida)
print("Maná:",mago.mana)
print("Defensa:",mago.defensa)
print("Vocación:",mago.vocacion)



class Player:
    def __init__(self,**kwargs):
        self.vida = kwargs.get("vida",0)
        self.defensa = kwargs.get("defensa",0)
        self.hechizo = kwargs.get("hechizo","Puff")

knight = Player(vida=80,defensa=40,hechizo="Rayo")

print("\nEl Knights tiene:\n")
print("Vida:",knight.vida)
print("Maná:",knight.defensa)
print("Defensa:",knight.hechizo)


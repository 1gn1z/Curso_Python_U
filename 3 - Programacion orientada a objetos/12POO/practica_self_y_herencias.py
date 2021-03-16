class Animales():
    def moverse(self):
        print("moviéndose")
    def comer(self):
        print("comiendo")

class Reptiles(Animales):
    def sangre_fria(self):
        print("tienen sangre fría")

class Tortugas(Reptiles):
    def ponen_huevos(self):
        print("poniendo huevos")

    def irse(self):
        print("Ya me voy :)")

    def encontrar_comida(self):
        self.moverse()
        print("Encontré comida!!!")
        self.comer()
        self.irse()

donatello = Tortugas()      # Creacion de una instancia de la clase tortugas.

print(donatello.encontrar_comida())
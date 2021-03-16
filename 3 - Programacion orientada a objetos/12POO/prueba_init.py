class animal:
    def __init__(self,nombre):
        self.nombre = nombre
        self.patas = 4
        self.tipo = "Can"

perro = animal("Kei")
gato = animal("Igna")

print(perro.nombre,perro.patas,perro.tipo)
print(gato.nombre,gato.patas,gato.tipo)
class Animal:
    def __init__(self,nome):
        self.nome=nome
    
    def som(self):
        return " Grunido "
    
    def bebe(self):
        return "Agua"
    
class Cao(Animal):
    def __init__ (self,nome,tutor):
        super().__init__(nome)
        self.tutor=tutor
    
    def exibir(self):
        return f"Tutor: {self.tutor} do {self.nome}"

class Gato(Animal):
    def som(self):
        return "Miau"

animal1=Animal("T-rex")
animal2=Cao("Pingo","Richard")
animal3=Gato("Tina")

print(f"ANimais: \n {animal1.som()}\n  {animal2.exibir()}\n  {animal3.som()}")
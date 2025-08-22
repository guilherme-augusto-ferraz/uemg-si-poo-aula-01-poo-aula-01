# Programação Orientada a Objetos

class Cachorro:
    
    def __init__(self, nome, fome, sono):
        self.nome = nome
        self.fome = fome
        self.sono = sono

    def comer(self):
        self.fome = self.fome - 1

    def dormir(self):
        self.sono = False

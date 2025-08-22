# Programação Orientada a Objetos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto)

p = Produto("Camiseta", 50.0)
p.aplicar_desconto(0.1)
print(p.nome, p.preco)
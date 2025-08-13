class Produto:          
    def __init__(self, nome = "",preco = 0.0):
        self.nome = nome
        self.preco = preco


    @classmethod
    def somente_nome(cls, nome):
        return cls(nome=nome)
        

    def exibir(self):
        return f"Produto (Nome: {self.nome}, preço: {self.preco:.2f})"
    
p1= Produto("Maça", 2.50)

p2 = Produto.somente_nome("Banana")

print(p1.exibir())
print(p2.exibir())  

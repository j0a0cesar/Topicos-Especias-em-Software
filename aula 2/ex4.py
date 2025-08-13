class Funcionario:          
    def __init__(self, nome = "",salario = 0.0):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome = "", salario = 0.0, departamento = ""):
        
    #chamada de construtor da classe mãe
     super().__init__(nome, salario)
     self.departamento = departamento # atributo específico da classe Gerente

    def ler(self):
        self.nome = input("Digite o nome: ")
        self.salario = float(input("Digite o salário: "))
        self.departamento = input("Digite o cargo: ")    

    def exibir(self):
        return f"Funicorio (Nome: {self.nome}, salário: {self.salario:.2f}, Departamento: {self.departamento})"
    
g = Gerente()
g.ler()
print(g.exibir())

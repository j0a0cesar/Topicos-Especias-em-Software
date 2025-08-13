'''
Classe Básica: Crie uma classe Pessoa com atributos nome e idade. Adicione um construtor para
inicializar esses valores e um método para exibir as informações da pessoa
'''
class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def ler(self):
        self.nome = input("Digite o seu nome: ")
        self.idade = int(input("Digite a sua idade: "))

        return f"Pessoa(nome: {self.nome}, idade: {self.idade})"
    
p = Pessoa()
print(p.ler())  

'''
Métodos e Atributos: Crie uma classe Carro com os atributos marca, modelo e ano. Adicione
métodos para alterar e obter esses valores. Inclua também um método para exibir as informações do
carro.
'''
class Carro:
    def __init__(self, marca = "", ano = 0, modelo = ""):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo    

    def ler(self):
        self.marca = input("Digite a marca do seu carro: ")
        self.ano= int(input("Digite o ano do seu carro: "))
        self.modelo = input("Digite o modelo do seu carro: ")


    def exibir(self):
        return f"Carro (modelo: {self.modelo}, ano: {self.ano}, marca: {self.marca})"
    
c = Carro()
c.ler()
print(c.exibir())
  

class Carro:
    def __init__(self, marca = "", ano = 0, modelo = ""):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo    

    def ler(self):
        self.marca = input("Digite a marca do seu carro: ")
        self.ano= int(input("Digite o ano do seu carro: "))
        self.modelo = input("Digite o modelo do seu carro: ")

        return f"Carro (modelo: {self.modelo}, ano: {self.ano}, marca: {self.marca})"
    
c = Carro()
print(c.ler())

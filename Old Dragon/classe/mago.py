from classe import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__()
        self.armadura = "não pode usar armaduara"
        self.armas = "pode usar apenas as armas pequenas"
        self.intensMagigos = "pode usar todos os tipos de itens mágicos"

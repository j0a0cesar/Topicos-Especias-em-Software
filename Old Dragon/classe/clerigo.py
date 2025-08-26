from classe import Classe

class Clerigo(Classe):
    def __init__(self):
        super().__init__(vida=8, ataque=1, protecao=5)
        self.armadura = "Pode usar todas as armaduras"
        self.armas = "Apenas armas de impacto"
        self.itens_magicos = "Pode usar todos os itens mágicos ordeiros"
        self.habilidades_classe = {
            1: ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"]
        }

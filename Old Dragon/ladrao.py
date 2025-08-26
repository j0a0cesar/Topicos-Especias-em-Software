

from classe import Classe


class Ladrao(Classe):
    def __init__(self):
        super().__init__(vida=6, ataque=1, protecao=5)
        self.armadura = "Apenas armaduras leves"
        self.armas = "Apenas armas pequenas ou médias"
        self.itens_magicos = "Não pode usar cajados, varinhas e pergaminhos (exceto os de proteção)"
        self.habilidades_classe = {
            1: ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]
        }

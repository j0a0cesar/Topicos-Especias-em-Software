from raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__()
        self.alinhamento = "Qualquer"
        self.infravisao = "Não possui"
        self.movimento = 9
        self.habilidades_raca = [
            "Aprendizado: Bônus de 10% sobre toda experiência (XP) recebida.",
            "Adaptabilidade: Bônus de +1 em uma única Jogada de Proteção à sua escolha."
        ]
        self.peso_base = 80.0

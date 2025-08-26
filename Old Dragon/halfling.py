from raca import Raca
class Halfling(Raca):
    def __init__(self):
        super().__init__()

        self.alinhamento = "Neutro"
        self.infravisao = "Não possui"
        self.movimento = 6
        self.habilidades_raca = [
            "Furtivos: Bônus para se esconder.",
            "Destemidos: Bônus de +1 em qualquer teste de JPS (Jogada de Proteção de Sabedoria).",
            "Bons de Mira: Ataques fáceis com armas de arremesso.",
            "Pequenos: Ataques de criaturas grandes são difíceis para acertá-los.",
            "Restrições: Apenas armaduras de couro e armas pequenas ou médias."
        ]
        self.peso_base = 35.0

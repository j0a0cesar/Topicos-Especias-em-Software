from raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__()

        self.alinhamento = "Qualquer"
        self.infravisao = "Não"
        self.movimento = 9

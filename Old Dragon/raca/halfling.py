from raca import Raca
class Halfling(Raca):
    def __init__(self):
        super().__init__()

        self.alinhamento = "Neutro"
        self.infravisao = "Não"
        self.movimento = 6

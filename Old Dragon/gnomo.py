from raca import Raca
class Gnomo(Raca):
    def __init__(self):
        super().__init__()
        self.alinhamento = "Neutro"
        self.infravisao = "18 metros"
        self.movimento = 6

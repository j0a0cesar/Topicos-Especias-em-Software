

from classe import Classe


class Ladrao(Classe):
    def __init__(self):
        super().__init__()
        self.armadura = "pode usar apenas as armaduras leves"
        self.armas = "pode usar apenas as armas pequenas ou médias"
        self.intensMagigos = "não pode usar cajados, não pode varinhas e pergaminhos com exceçao dos pergaminhos de proteção"

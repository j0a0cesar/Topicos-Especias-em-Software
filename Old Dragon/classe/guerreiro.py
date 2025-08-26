from classe import Classe


class Guerreiro(Classe):
    def __init__(self):
        super().__init__(vida = 10, ataque = 1, protecao = 5)
        self.armadura = "pode usar todas as armaduras"
        self.armas = "pode usar todas as armas"
        self.intensMagigos = "não pode usar cajados, não pode varinhas e pergaminhos com exceçao dos pergaminhos de proteção"
        self.habilidades_classe = ['Aparar', 'Ataque Extra','Maestria em Arma', ]

class Jogador:

    def __init__(self, nome: str, cor: bool):
        self.nome = nome
        self.cor = cor

    def getcor(self):
        return self.cor

    def getnome(self):
        return self.nome

from xadrex_esqueleto import *
from tabuleiro import *

class Jogador:
    def __init__(self,cor : bool):
        self.cor = cor

    def solicitar_movimento(self,tabuleiro):
        origem = input("Digite a origem Da Peça: ")
        destino = input("Digite o Destina da Peça: ")

        origem = tabuleiro.posicao_para_coordenadas(origem)
        destino = tabuleiro.posicao_para_coordenadas(destino)

        if origem is None or destino is None:
            print("Posição invalida use letras A-H e numeros 1-8")
            return

        numeros_origem, letras_origem = origem
        numeros_destino, letras_destino = destino

        tabuleiro.mover_peca(numeros_origem,letras_origem,numeros_destino,letras_destino,self.cor)
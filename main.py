from xadrex_esqueleto import *
from tabuleiro import *
from jogador import *

tabuleiro = Tabuleiro()
tabuleiro.posicionar_pecas()

jogador_branco = Jogador(True)
jogador_preto = Jogador(False)

tabuleiro.mostrar()
print("\n")

jogador_branco.solicitar_movimento(tabuleiro)
print("\n")
tabuleiro.mostrar()
print("\n")
jogador_branco.solicitar_movimento(tabuleiro)
tabuleiro.mostrar()
print("\n")
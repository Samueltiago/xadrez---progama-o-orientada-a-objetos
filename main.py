from xadrex_esqueleto import *
from tabuleiro import *

tabuleiro = Tabuleiro()

tabuleiro.posicionar_peoes()

tabuleiro.mover_peca(6,4,4,4)
tabuleiro.mover_peca(1,3,2,3)

tabuleiro.mostrar()

#teste
tabuleiro.colocar_peca(Peao(3,3,False))
tabuleiro.mostrar
tabuleiro.mover_peca(4,4,3,3)
tabuleiro.mostrar()

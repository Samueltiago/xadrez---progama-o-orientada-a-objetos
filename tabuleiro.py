
from xadrex_esqueleto import *


class Tabuleiro:

    def __init__(self):
        self.casas = [[None for _ in range(8)] for _ in range(8)]

        self.ultima_jogada = None

        self.turno_branco = True

    def trocar_turno(self):
        self.turno_branco = not self.turno_branco

    def colocar_peca(self, peca):
        numeros, letras = peca.getposicao()

        if numeros < 0 or numeros > 7 or letras < 0 or letras > 7:
            raise ValueError("Posição da peça inválida.")

        if self.casas[numeros][letras] is not None:
            raise ValueError("Já existe uma peça nessa posição.")

        self.casas[numeros][letras] = peca

    def posicionar_pecas(self):

        # Peças pretas
        self.colocar_peca(Torre(0, 0, False))
        self.colocar_peca(Cavalo(0, 1, False))
        self.colocar_peca(Bispo(0, 2, False))
        self.colocar_peca(Rainha(0, 3, False))
        self.colocar_peca(Rei(0, 4, False))
        self.colocar_peca(Bispo(0, 5, False))
        self.colocar_peca(Cavalo(0, 6, False))
        self.colocar_peca(Torre(0, 7, False))

        # Peças brancas
        self.colocar_peca(Torre(7, 0, True))
        self.colocar_peca(Cavalo(7, 1, True))
        self.colocar_peca(Bispo(7, 2, True))
        self.colocar_peca(Rainha(7, 3, True))
        self.colocar_peca(Rei(7, 4, True))
        self.colocar_peca(Bispo(7, 5, True))
        self.colocar_peca(Cavalo(7, 6, True))
        self.colocar_peca(Torre(7, 7, True))

        # Peões
        for coluna in range(8):
            self.colocar_peca(Peao(1, coluna, False))
            self.colocar_peca(Peao(6, coluna, True))

    def mover_peca(self, numeros_origem, letras_origem,
                   numeros_destino, letras_destino):

        # Verifica se as coordenadas estão dentro do tabuleiro
        if not (0 <= numeros_origem < 8 and 0 <= letras_origem < 8 and 0 <= numeros_destino < 8 and 0 <= letras_destino < 8):
            raise ValueError("Posição fora do tabuleiro.")

        peca = self.casas[numeros_origem][letras_origem]

        # Verifica se existe uma peça na origem
        if peca is None:
            raise ValueError("Não existe peça nessa posição.")

        # Verifica se a peça pertence ao jogador da vez
        if peca.getcor() != self.turno_branco:
            raise ValueError("Essa peça não pertence ao jogador da vez.")

        movimentos_possiveis = peca.movimento(self)

        if (numeros_destino, letras_destino) not in movimentos_possiveis:
            raise ValueError("Movimento inválido.")

       
        #confirmando se a casa que o rei esta indo esta atacada
        peca_destino_original = self.casas[numeros_destino][letras_destino]

        pos_antiga_numeros, pos_antiga_letras = peca.getposicao()

        self.casas[numeros_origem][letras_origem] = None
        self.casas[numeros_destino][letras_destino] = peca

        peca.setposicao(numeros_destino, letras_destino)

        proprio_rei_em_xeque = self.esta_em_xeque(peca.getcor())

    
        peca.setposicao(pos_antiga_numeros, pos_antiga_letras)

        self.casas[numeros_origem][letras_origem] = peca
        self.casas[numeros_destino][letras_destino] = peca_destino_original

        if proprio_rei_em_xeque:
            raise ValueError("Esse movimento deixa seu Rei em xeque.")

        # --------------------------------------------------
        # ROQUE
        # --------------------------------------------------

        if type(peca).__name__ == "Rei" and abs(letras_destino - letras_origem) == 2:

            coluna_torre_origem = 7 if letras_destino > letras_origem else 0

            coluna_torre_destino = (
                letras_destino - 1
                if letras_destino > letras_origem
                else letras_destino + 1
            )

            torre = self.casas[numeros_origem][coluna_torre_origem]

            self.casas[numeros_origem][coluna_torre_origem] = None
            self.casas[numeros_origem][coluna_torre_destino] = torre

            if torre:
                torre.setposicao(numeros_origem, coluna_torre_destino)
                torre.foi_movida = True

        # --------------------------------------------------
        # EN PASSANT
        # --------------------------------------------------

        if (type(peca).__name__ == "Peao" and
                letras_origem != letras_destino and
                self.casas[numeros_destino][letras_destino] is None):

            self.casas[numeros_origem][letras_destino] = None

        self.casas[numeros_origem][letras_origem] = None
        self.casas[numeros_destino][letras_destino] = peca

        peca.setposicao(numeros_destino, letras_destino)

        if hasattr(peca, "foi_movida"):
            peca.foi_movida = True

        self.ultima_jogada = (
            numeros_origem,
            letras_origem,
            numeros_destino,
            letras_destino,
            peca
        )

        self.trocar_turno()

    def encontrar_rei(self, cor):

        for numeros in range(8):
            for letras in range(8):

                peca = self.casas[numeros][letras]

                if (peca and
                        type(peca).__name__ == "Rei" and
                        peca.getcor() == cor):

                    return numeros, letras

        raise ValueError("Rei não encontrado no tabuleiro.")

    def casa_esta_atacada(self, linha_alvo, coluna_alvo, cor_atacante):

        for numeros in range(8):
            for letras in range(8):

                peca = self.casas[numeros][letras]

                if peca and peca.getcor() == cor_atacante:

                    # Ataque do Rei
                    if type(peca).__name__ == "Rei":

                        if max(
                            abs(numeros - linha_alvo),
                            abs(letras - coluna_alvo)
                        ) == 1:

                            return True

 
                    elif type(peca).__name__ == "Peao":

                        direcao = -1 if peca.getcor() else 1

                        if (linha_alvo == numeros + direcao and
                                abs(coluna_alvo - letras) == 1):

                            return True

                    # Ataque das outras peças
                    else:

                        if (linha_alvo, coluna_alvo) in peca.movimento(self):
                            return True

        return False


    def esta_em_xeque(self, cor):

        pos_rei = self.encontrar_rei(cor)

        return self.casa_esta_atacada(
            pos_rei[0],
            pos_rei[1],
            not cor
        )

    def simular_movimento_salva_xeque(
            self, numeros_origem, letras_origem,
            numeros_destino, letras_destino, cor):

        peca_origem = self.casas[numeros_origem][letras_origem]
        peca_destino = self.casas[numeros_destino][letras_destino]

        pos_antiga = peca_origem.getposicao()

        self.casas[numeros_origem][letras_origem] = None
        self.casas[numeros_destino][letras_destino] = peca_origem

        peca_origem.setposicao(numeros_destino, letras_destino)

        xeque = self.esta_em_xeque(cor)

        # Restaura o tabuleiro
        peca_origem.setposicao(pos_antiga[0], pos_antiga[1])

        self.casas[numeros_origem][letras_origem] = peca_origem
        self.casas[numeros_destino][letras_destino] = peca_destino

        return not xeque

    def esta_em_xeque_mate(self, cor):

        if not self.esta_em_xeque(cor):
            return False

        for numeros_origem in range(8):
            for letras_origem in range(8):

                peca = self.casas[numeros_origem][letras_origem]

                if peca and peca.getcor() == cor:

                    for numeros_destino, letras_destino in peca.movimento(self):

                        if self.simular_movimento_salva_xeque(
                                numeros_origem,
                                letras_origem,
                                numeros_destino,
                                letras_destino,
                                cor):

                            return False

        return True

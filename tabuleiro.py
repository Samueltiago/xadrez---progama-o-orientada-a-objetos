from xadrex_esqueleto import *

class Tabuleiro:

    def __init__(self):
        self.casas = []

        for linha in range(8):
            casas_linha = []
            for coluna in range(8):
                casas_linha.append(None)
            self.casas.append(casas_linha)

    def colocar_peca(self, Peca):
            x,y = Peca.getposicao()
            if x < 0 or x > 7 or y < 0 or y > 7:
                print("Posição invalido")
                return
   
            if self.casas[x][y] is not None:
                print("Casa ja oculpada")
                return    
   
            self.casas[x][y] = Peca
   
    def posicionar_peoes(self):
        for coluna in range(8):
            self.colocar_peca(Peao(1,coluna,False)) #Preto colocando todos os 8 Peoes
            self.colocar_peca(Peao(6,coluna,True)) #Branco colocando todos os 8 Peoes

    def mover_peao(self, x_origem, y_origem, x_destino, y_destino):
        peca = self.casas[x_origem][y_origem]

        if peca is None:
            print("Não há peça nessa casa")
            return

        if (x_destino, y_destino) not in peca.movimento(self):
            print("Movimento inválido")
            return

        self.casas[x_origem][y_origem] = None
        self.casas[x_destino][y_destino] = peca
        peca.setposicao(x_destino, y_destino)

    def mostrar(self):
        for linha in self.casas:
            for casa in linha:
                if casa is None:
                    print("..", end=" ")
                elif casa.getcor():
                    print("PB", end=" ")
                else:
                    print("PP", end=" ")
            print()

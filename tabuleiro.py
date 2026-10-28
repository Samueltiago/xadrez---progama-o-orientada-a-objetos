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
            numeros,letras = Peca.getposicao()
            if numeros < 0 or numeros > 7 or letras < 0 or letras > 7:
                print("Posição invalido")
                return
   
            if self.casas[numeros][letras] is not None:
                print("Casa ja oculpada")
                return    
   
            self.casas[numeros][letras] = Peca
   
    
    def posicionar_pecas(self):
        # Peças pretas: linha 0
        self.colocar_peca(Torre(0, 0, False))
        self.colocar_peca(Cavalo(0, 1, False))
        self.colocar_peca(Bispo(0, 2, False))
        self.colocar_peca(Rainha(0, 3, False))
        self.colocar_peca(Rei(0, 4, False))
        self.colocar_peca(Bispo(0, 5, False))
        self.colocar_peca(Cavalo(0, 6, False))
        self.colocar_peca(Torre(0, 7, False))

        # Peças brancas: linha 7
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



    def mover_peca(self, numeros_origem, letras_origem, numeros_destino, letras_destino,cor_jogador):
        peca = self.casas[numeros_origem][letras_origem]

        if peca is None:
            print("Não há peça nessa casa")
            return

        if (numeros_destino, letras_destino) not in peca.movimento(self):
            print("Movimento inválido")
            return

        if cor_jogador is not None and peca.getcor() != cor_jogador:
            print("Essa peça não pertence a você")
            return

        self.casas[numeros_origem][letras_origem] = None
        self.casas[numeros_destino][letras_destino] = peca
        
        peca.setposicao(numeros_destino, letras_destino)


    def posicao_para_coordenadas(self, posicao):
        posicao = posicao.strip().upper()

        if len(posicao) != 2:
            return None

        coluna = posicao[0]
        linha = posicao[1]

        if coluna not in "ABCDEFGH" or linha not in "12345678":
            return None

        letras = ord(coluna) - ord("A")
        numeros = 8 - int(linha)

        return numeros,letras

        
    
    def mostrar(self):
        print("   A  B  C  D  E  F  G  H")

        numero = 8

        for linha in self.casas:
            print(numero, end="  ")

            for casa in linha:
                if casa is None:
                    print("..", end=" ")
                else:
                
                    nome_peca = type(casa).__name__

                    siglas = {
                        "Peao": "P",
                        "Cavalo": "C",
                        "Bispo": "B",
                        "Torre": "T",
                        "Rainha": "R",
                        "Rei": "K"
                    }

                
                    letra = siglas.get(nome_peca, "?")

                
                    if casa.getcor():
                        cor = "B" 
                    else:
                        cor = "P"  

                    print(letra + cor, end=" ")

            print(" ", numero)
            numero -= 1

        print("   A  B  C  D  E  F  G  H")
from tabuleiro import Tabuleiro
from jogador import Jogador


class XadrezTerminal:
    # (nome da classe, é branca?) -> símbolo
    SIMBOLOS = {
        ("Rei", True): "\u2654",    ("Rei", False): "\u265A",
        ("Rainha", True): "\u2655", ("Rainha", False): "\u265B",
        ("Torre", True): "\u2656",  ("Torre", False): "\u265C",
        ("Bispo", True): "\u2657",  ("Bispo", False): "\u265D",
        ("Cavalo", True): "\u2658", ("Cavalo", False): "\u265E",
        ("Peao", True): "\u2659",   ("Peao", False): "\u265F",
    }

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.posicionar_pecas()

        self.jogador_branco = Jogador("Jogador 1", True)
        self.jogador_preto = Jogador("Jogador 2", False)

    def jogador_da_vez(self):
        if self.tabuleiro.turno_branco:
            return self.jogador_branco
        return self.jogador_preto

    def posicao_para_coordenadas(self, posicao):
        
        posicao = posicao.strip().upper()

        if len(posicao) != 2:
            raise ValueError("Posição inválida. Use letras A-H e números 1-8 (ex.: E2).")

        coluna, linha = posicao[0], posicao[1]

        if coluna not in "ABCDEFGH" or linha not in "12345678":
            raise ValueError("Posição inválida. Use letras A-H e números 1-8 (ex.: E2).")

        return 8 - int(linha), ord(coluna) - ord("A")

    def pedir_promocao(self):
        opcoes = {
            str(numero): nome
            for numero, nome in enumerate(self.tabuleiro.PECAS_PROMOCAO, start=1)
        }

        print("\nPROMOÇÃO DO PEÃO!")
        for numero, nome in opcoes.items():
            print(f"{numero} - {nome}")

        while self.tabuleiro.aguardando_promocao:
            escolha = input("Escolha a nova peça: ").strip()

            try:
                self.tabuleiro.promover_peao(opcoes.get(escolha, ""))
            except ValueError as erro:
                print(f"\n {erro}")

    def mostrar(self):
        print("\n    A  B  C  D  E  F  G  H")

        for indice, linha in enumerate(self.tabuleiro.casas):
            numero = 8 - indice
            print(numero, end="   ")

            for peca in linha:
                if peca is None:
                    print("·", end="  ")
                else:
                    simbolo = self.SIMBOLOS[(type(peca).__name__, peca.getcor())]
                    print(simbolo, end="  ")

            print(" ", numero)

        print("    A  B  C  D  E  F  G  H\n")

    def solicitar_movimento(self):
        origem = input("Digite a origem da peça (ou 'sair'): ")
        if origem.strip().lower() == "sair":
            return False

        destino = input("Digite o destino da peça: ")

        n_origem, l_origem = self.posicao_para_coordenadas(origem)
        n_destino, l_destino = self.posicao_para_coordenadas(destino)

        self.tabuleiro.mover_peca(n_origem, l_origem, n_destino, l_destino)
        
        if self.tabuleiro.aguardando_promocao:
            self.pedir_promocao()
        
        return True

    def jogar(self):
        while True:
            self.mostrar()

            jogador = self.jogador_da_vez()
            cor = jogador.getcor()

            if self.tabuleiro.esta_em_xeque(cor):
                print("XEQUE!")

            print(f"Vez de {jogador.getnome()} ({'Brancas' if cor else 'Pretas'})")

            try:
                continuar = self.solicitar_movimento()
            except ValueError as erro:
                print(f"\n {erro}")
                continue

            if not continuar:
                print("Partida encerrada.")
                return

            # após o movimento, o turno já passou para o adversário
            cor_adversario = self.tabuleiro.turno_branco

            if self.tabuleiro.esta_em_xeque_mate(cor_adversario):
                self.mostrar()
                vencedor = "Pretas" if cor_adversario else "Brancas"
                print(f"XEQUE-MATE! Vitória das {vencedor}!")
                return

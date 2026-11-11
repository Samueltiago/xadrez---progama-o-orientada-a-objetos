from interface import *
from xadrez_terminal import *

def escolher_modo():
    while True:
        print("=== XADREZ ===")

        print("1 - Interface gráfica")
        print("2 - Terminal")

        escolha = input("Escolha a versão (1 ou 2): ").strip()

        if escolha in ("1", "2"):
            return escolha

        print("Opção inválida.\n")


if __name__ == "__main__":
    modo = escolher_modo()

    if modo == "1":
        janela = tk.Tk()
        app = XadrezInterface(janela)
        janela.mainloop()
    else:
        XadrezTerminal().jogar()
import tkinter as tk
from tkinter import messagebox
from tabuleiro import Tabuleiro
from jogador import Jogador


class XadrezInterface:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Xadrez dos cria")

    
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.posicionar_pecas()

        self.jogador_branco = Jogador("Jogador 1", True)
        self.jogador_preto = Jogador("Jogador 2", False)

        
        self.casa_selecionada = None

      
        self.cor_clara = "#f0d9b5"
        self.cor_escura = "#b58863"
        self.cor_selecao = "#7a9a60"
        self.cor_borda = "#d18b47"

        self.imagens_pecas = {
            ("Peao", True): tk.PhotoImage(file="imagens/wp.png", master=self.raiz).subsample(2, 2),
            ("Peao", False): tk.PhotoImage(file="imagens/bp.png", master=self.raiz).subsample(2, 2),

            ("Torre", True): tk.PhotoImage(file="imagens/wr.png", master=self.raiz).subsample(2, 2),
            ("Torre", False): tk.PhotoImage(file="imagens/br.png", master=self.raiz).subsample(2, 2),

            ("Cavalo", True): tk.PhotoImage(file="imagens/wn.png", master=self.raiz).subsample(2, 2),
            ("Cavalo", False): tk.PhotoImage(file="imagens/bn.png", master=self.raiz).subsample(2, 2),

            ("Bispo", True): tk.PhotoImage(file="imagens/wb.png", master=self.raiz).subsample(2, 2),
            ("Bispo", False): tk.PhotoImage(file="imagens/bb.png", master=self.raiz).subsample(2, 2),

            ("Rainha", True): tk.PhotoImage(file="imagens/wq.png", master=self.raiz).subsample(2, 2),
            ("Rainha", False): tk.PhotoImage(file="imagens/bq.png", master=self.raiz).subsample(2, 2),

            ("Rei", True): tk.PhotoImage(file="imagens/wk.png", master=self.raiz).subsample(2, 2),
            ("Rei", False): tk.PhotoImage(file="imagens/bk.png", master=self.raiz).subsample(2, 2),
        }

        
        exemplo_img = self.imagens_pecas[("Peao", True)]

        self.imagem_vazia = tk.PhotoImage(
            width=exemplo_img.width(),
            height=exemplo_img.height(),
            master=self.raiz
        )

       
        self.botoes = [[None for _ in range(8)] for _ in range(8)]

        self.criar_tabuleiro_visual()
        self.atualizar_tabuleiro_visual()

    def criar_tabuleiro_visual(self):
        letras_colunas = ["A", "B", "C", "D", "E", "F", "G", "H"]

        # --- 1. Adicionar números APENAS na lateral esquerda (coluna 0) ---
        for linha in range(8):
            numero = str(8 - linha)
            lbl_esq = tk.Label(self.raiz, text=numero, bg=self.cor_borda, fg="white", font=("Arial", 9, "bold"))
            lbl_esq.grid(row=linha, column=0, sticky="nsew")

        # --- 2. Adicionar letras APENAS embaixo (linha 8) ---
        for col_idx, letra in enumerate(letras_colunas):
            lbl = tk.Label(self.raiz, text=letra, bg=self.cor_borda, fg="white", font=("Arial", 9, "bold"))
            lbl.grid(row=8, column=col_idx + 1, sticky="nsew")

        # canto inferior esquerdo para preencher a quina (linha 8, coluna 0)
        lbl_canto = tk.Label(self.raiz, text="", bg=self.cor_borda)
        lbl_canto.grid(row=8, column=0, sticky="nsew")

        # --- 3. Criar as casas do tabuleiro ---
        for letras in range(8):
            for numeros in range(8):

                cor_fundo = (
                    self.cor_clara
                    if (letras + numeros) % 2 == 0
                    else self.cor_escura
                )

                botao = tk.Button(
                    self.raiz,
                    bg=cor_fundo,
                    activebackground=self.cor_selecao,
                    relief="flat",
                    bd=0,
                    highlightthickness=0,
                    padx=0,
                    pady=0,
                    command=lambda l=letras, n=numeros: self.clique_casa(l, n)
                )

                # Tabuleiro alinhado: linhas 0-7 e colunas 1-8
                botao.grid(row=letras, column=numeros + 1, sticky="nsew")

                self.botoes[letras][numeros] = botao

        # Configurar proporção do grid (9 linhas x 9 colunas)
        for i in range(9):
            self.raiz.grid_rowconfigure(i, weight=1)
            self.raiz.grid_columnconfigure(i, weight=1)


    def atualizar_tabuleiro_visual(self):

        for linha in range(8):
            for coluna in range(8):

                peca = self.tabuleiro.casas[linha][coluna]
                botao = self.botoes[linha][coluna]

                cor_padrao = (
                    self.cor_clara
                    if (linha + coluna) % 2 == 0
                    else self.cor_escura
                )

                botao.config(bg=cor_padrao)

                if peca is not None:

                    nome_peca = type(peca).__name__
                    cor_peca = peca.getcor()

                    img = self.imagens_pecas.get(
                        (nome_peca, cor_peca)
                    )

                    if img:
                        botao.config(image=img, text="")
                        botao.image = img

                    else:
                        botao.config(image="", text=nome_peca[0])

                else:

                    botao.config(
                        image=self.imagem_vazia,
                        text=""
                    )

                    botao.image = self.imagem_vazia

    def clique_casa(self, linha, coluna):


        if self.casa_selecionada is None:

            peca = self.tabuleiro.casas[linha][coluna]

            # Casa vazia
            if peca is None:
                return

            if peca.getcor() != self.tabuleiro.turno_branco:
                return

            # Seleciona a peça
            self.casa_selecionada = (linha, coluna)

            self.botoes[linha][coluna].config(
                bg=self.cor_selecao
            )


        else:

            letras_origem, numeros_origem = self.casa_selecionada

            if letras_origem == linha and numeros_origem == coluna:

                self.casa_selecionada = None
                self.atualizar_tabuleiro_visual()
                return

            try:


                self.tabuleiro.mover_peca(
                    letras_origem,
                    numeros_origem,
                    linha,
                    coluna
                )

    
                self.atualizar_tabuleiro_visual()

                self.raiz.update_idletasks()

                # Verifica se o peão precisa ser promovido na interface
                if self.tabuleiro.aguardando_promocao:
                    self.pedir_promocao_interface()
                    self.atualizar_tabuleiro_visual()

                # Verifica se o adversário está em xeque-mate
                cor_adversario = self.tabuleiro.turno_branco

                if self.tabuleiro.esta_em_xeque_mate(cor_adversario):


                    cor_vencedor = not cor_adversario

                    vencedor = (
                        "Brancas"
                        if cor_vencedor
                        else "Pretas"
                    )

                    reiniciar = messagebox.askyesno(
                        "FIM DE JOGO",
                        f"XEQUE-MATE! Vitória das {vencedor}!\n"
                        "Deseja iniciar uma nova partida?"
                    )

                    if reiniciar:

                        self.tabuleiro = Tabuleiro()
                        self.tabuleiro.posicionar_pecas()

                        self.casa_selecionada = None

                        self.atualizar_tabuleiro_visual()

            except ValueError as erro:

                messagebox.showwarning(
                    "Movimento inválido",
                    str(erro)
                )

            finally:

                self.casa_selecionada = None

                self.atualizar_tabuleiro_visual()

    def pedir_promocao_interface(self):
        linha, coluna = self.tabuleiro.casa_promocao
        peca_atual = self.tabuleiro.casas[linha][coluna]
        cor_peca = peca_atual.getcor() if peca_atual else True

        janela_promocao = tk.Toplevel(self.raiz)
        janela_promocao.title("Promoção do Peão")
        janela_promocao.transient(self.raiz)
        janela_promocao.grab_set()

        tk.Label(
            janela_promocao,
            text="Escolha a nova peça:",
            font=("Arial", 11, "bold")
        ).pack(pady=10)

        frame_botoes = tk.Frame(janela_promocao)
        frame_botoes.pack(padx=20, pady=10)

        opcoes = ["Rainha", "Torre", "Bispo", "Cavalo"]

        def selecionar(nome_peca):
            try:
                self.tabuleiro.promover_peao(nome_peca)
                janela_promocao.destroy()
            except ValueError as erro:
                messagebox.showwarning("Erro", str(erro), parent=janela_promocao)

        for nome in opcoes:
            img = self.imagens_pecas.get((nome, cor_peca))
            
            btn = tk.Button(
                frame_botoes,
                image=img,
                command=lambda n=nome: selecionar(n),
                relief="raised",
                bd=2,
                padx=5,
                pady=5
            )
            if img:
                btn.image = img
            else:
                btn.config(text=nome)
                
            btn.pack(side="left", padx=5)

        self.raiz.wait_window(janela_promocao)
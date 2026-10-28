from abc import ABC, abstractmethod

class Peca(ABC):
    __numeros: int
    __letras : int
    __cor : bool

    def __init__(self,numeros : int,letras : int ,cor : bool):
        self.__numeros = numeros
        self.__letras = letras
        self.__cor = cor

    @abstractmethod
    def movimento(self):
        pass

    def getposicao(self):
        return self.__numeros,self.__letras

    def getcor(self):
        #meu pensamento se for true é branco se for false é preto acho que seria mais facil para verificar quem começa
        return self.__cor
       
    def setposicao(self, novo_numero : int, nova_letra : int):
        self.__numeros = novo_numero
        self.__letras = nova_letra
        return self.__numeros,self.__letras
       
   

class Peao(Peca):
   
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
    
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []

        if self.getcor():
            direcao = -1
            linha_inicial = 6
        else:
            direcao = 1
            linha_inicial = 1

        novo_numeros = numeros + direcao
        if novo_numeros < 0 or novo_numeros > 7:
            return movimentos

        if tabuleiro.casas[novo_numeros][letras] is None:
            movimentos.append((novo_numeros, letras))
            if numeros == linha_inicial and tabuleiro.casas[novo_numeros + direcao][letras] is None:
                movimentos.append((novo_numeros + direcao, letras))

        for nova_letras in (letras - 1, letras + 1):
            if 0 <= nova_letras <= 7:
                alvo = tabuleiro.casas[novo_numeros][nova_letras]
                if alvo is not None and alvo.getcor() != self.getcor():
                    movimentos.append((novo_numeros, nova_letras))

        return movimentos    


    
   
class Cavalo(Peca):
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
       
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []
        
        pulos = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        
        for delta_numeros, delta_letras in pulos:
            nova_numeros = numeros + delta_numeros
            nova_letras = letras + delta_letras
            
            if 0 <= nova_numeros <= 7 and 0 <= nova_letras <= 7:
                alvo = tabuleiro.casas[nova_numeros][nova_letras]
                
                if alvo is None or alvo.getcor() != self.getcor():
                    movimentos.append((nova_numeros, nova_letras))
                    
        return movimentos
   
class Bispo(Peca):
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
       
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []
        
        direcoes = [
            (-1, -1), (-1, 1),
            (1, -1),  (1, 1)
        ]
        
        for delta_numeros, delta_letras in direcoes:
            nova_numeros, nova_letras = numeros, letras
            
            while True:
                nova_numeros += delta_numeros
                nova_letras += delta_letras
                
                if not (0 <= nova_numeros <= 7 and 0 <= nova_letras <= 7):
                    break
                
                alvo = tabuleiro.casas[nova_numeros][nova_letras]
                
                if alvo is None:
                    movimentos.append((nova_numeros, nova_letras))
                else:
                    if alvo.getcor() != self.getcor():
                        movimentos.append((nova_numeros, nova_letras))
                    break
                    
        return movimentos
   

class Torre(Peca):
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
       
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []
        
        direcoes = [
            (-1, 0), (1, 0),   
            (0, -1), (0, 1)    
        ]
        
        for delta_numeros, delta_letras in direcoes:
            nova_numeros, nova_letras = numeros, letras

            while True:
                nova_numeros += delta_numeros
                nova_letras += delta_letras
                
                if not (0 <= nova_numeros <= 7 and 0 <= nova_letras <= 7):
                    break
                
                alvo = tabuleiro.casas[nova_numeros][nova_letras]
                
                if alvo is None:
                    movimentos.append((nova_numeros, nova_letras))
                else:
                    if alvo.getcor() != self.getcor():
                        movimentos.append((nova_numeros, nova_letras))
                    break
                    
        return movimentos

class Rainha(Peca):
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
       
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []
        
        direcoes = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   
            (-1, -1), (-1, 1), (1, -1), (1, 1)  
        ]
        
        for delta_numeros, delta_letras in direcoes:
            nova_numeros, nova_letras = numeros, letras
            
            while True:
                nova_numeros += delta_numeros
                nova_letras += delta_letras
                
                if not (0 <= nova_numeros <= 7 and 0 <= nova_letras <= 7):
                    break
                
                alvo = tabuleiro.casas[nova_numeros][nova_letras]
                
                if alvo is None:
                    movimentos.append((nova_numeros, nova_letras))
                else:
                    if alvo.getcor() != self.getcor():
                        movimentos.append((nova_numeros, nova_letras))
                    break
                    
        return movimentos
    
class Rei(Peca):
    def __init__(self, numeros, letras, cor):
        super().__init__(numeros, letras, cor)
       
    def movimento(self, tabuleiro):
        numeros, letras = self.getposicao()
        movimentos = []
        
        direcoes = [
            (-1, 0), (1, 0),  
            (0, -1), (0, 1),  
            (-1, -1), (-1, 1), 
            (1, -1), (1, 1)    
        ]
        
        cor_adversaria = not self.getcor()
        
        for delta_numeros, delta_letras in direcoes:
            nova_numeros = numeros + delta_numeros
            nova_letras = letras + delta_letras
            
            if 0 <= nova_numeros <= 7 and 0 <= nova_letras <= 7:
                alvo = tabuleiro.casas[nova_numeros][nova_letras]
                
                if alvo is None or alvo.getcor() != self.getcor():
                    
                    if not tabuleiro.casa_esta_atacada(nova_numeros, nova_letras, cor_adversaria):
                        movimentos.append((nova_numeros, nova_letras))
                        
        return movimentos
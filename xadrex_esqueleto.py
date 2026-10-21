from abc import ABC, abstractmethod

class Peca(ABC):
    __x: int
    __y : int
    __cor : bool

    def __init__(self,x : int,y : int ,cor : bool):
        self.__x = x
        self.__y = y
        self.__cor = cor

    @abstractmethod
    def movimento(self):
        pass

    def getposicao(self):
        return self.__x,self.__y

    def getcor(self):
        #meu pensamento se for true é branco se for false é preto acho que seria mais facil para verificar quem começa
        return self.__cor
       
    def setposicao(self, novoX : int, novoY : int):
        self.__x = novoX
        self.__y = novoY
        return self.__x,self.__y
       
   

class Peao(Peca):
   
    def __init__(self, x, y, cor):
        super().__init__(x, y, cor)
    
    def movimento(self, tabuleiro):
        x, y = self.getposicao()
        movimentos = []

        if self.getcor():
            direcao = -1
            linha_inicial = 6
        else:
            direcao = 1
            linha_inicial = 1

        nova_x = x + direcao
        if nova_x < 0 or nova_x > 7:
            return movimentos

        if tabuleiro.casas[nova_x][y] is None:
            movimentos.append((nova_x, y))
            if x == linha_inicial and tabuleiro.casas[nova_x + direcao][y] is None:
                movimentos.append((nova_x + direcao, y))

        for nova_y in (y - 1, y + 1):
            if 0 <= nova_y <= 7:
                alvo = tabuleiro.casas[nova_x][nova_y]
                if alvo is not None and alvo.getcor() != self.getcor():
                    movimentos.append((nova_x, nova_y))

        return movimentos    


    
   
class Cavalo(Peca):
    def __init__(self, x, y, cor):
        super().__init__(x, y, cor)
       
    def movimento(self):
        pass
   
class Bispo(Peca):
    def __init__(self, x, y, cor):
        super().__init__(x, y, cor)
       
    def movimento(self):
        pass
   

class Torre(Peca):
    def __init__(self, x, y, cor):
        super().__init__(x, y, cor)
       
    def movimento(self):
        pass

class Rainha(Peca):
    def __init__(self, x, y, cor):
        super().__init__(x, y, cor)
       
    def movimento(self):
        pass

    

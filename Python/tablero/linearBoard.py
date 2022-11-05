from settings import BOARD_SIZE

class LinearBoard:
    '''
    Representa un tablero con una sola columna.
    X representa jugador 1, o al 2 y None al espacio vacio
    '''
    
    def __init__(self):
        '''
        Inicializa tablero en vacio
        '''
        self._column = [None] * BOARD_SIZE


    def add(self,char):
        '''
        colocs una ficha en la columna
        '''
        
        if not self.is_full():
            i = self._column.index(None)
            self._column[i] = char

    def is_full(self):
        if self._column[-1] == None:
            return False
        else:
            return True


    def is_victory(self, char):
        pass

    def is_tie(self, char1,char2):
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False):
            return True
        else:
            return False


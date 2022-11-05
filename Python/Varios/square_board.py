from tkinter.tix import COLUMN
from Varios.linear_board import LinearBoard
from settings import BOARD_SIZE


class SquareBoard():
    """
    Clase que representa un tablero Cuadrado
    
    Métodos para:

    1. Añadir un carácter (jugar en una columna)
    2. Detectar la victoria de un jugador
    3. Detectar el empate de 2 jugadores
    4. Detectar que el tablero está lleno
    
    """
    @classmethod
    def fromList(cls,list_of_list):
        columns = []
        for element in list_of_list:
            columns.append(LinearBoard.fromList(element))
        board = cls()
        board._columns = columns
        return board


    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_SIZE -1)]

    def is_full(self):
        all_full = True
        for element in self._columns:
            all_full = all_full and element.is_full()
        return all_full

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def as_list(self):
        '''
        devuelve la representacion dek tablero como una lista
        '''
        return self._columns


    def add(self, char, index):
        self._columns[index].add(char)

    def as_matrix(self):
        '''
        devuelve su representacion como matriz
        '''

        matrix = []
        for linear_board in self._columns:
            matrix.append(linear_board.as_list())
        return matrix
    
    def _any_vertical_victory(self, char):
        victory = False
        for linear_board in self._columns:
            victory = victory or linear_board.is_victory(char)
        return victory

    def _any_horizontal_victory(self, char):
        '''
        Averiguar si en el tablero hay una victoria horizontal, 
        rotando el tablero y al tablero resultante preguntandole si tiene
        una victoria vertical'''

        #obtengo la matriz q representa al tablero ACTUAL(self)
        #transpongo esa matriz
        #creo un tablero temporl a partir de esa matriz
        # le pregunto si tiene alguna victoria vertical
        # devuelvo ese valor

        
        pass

    def _any_rising_victory(self,char):
        pass

    def _any_sinking_victory(self, char):
        pass
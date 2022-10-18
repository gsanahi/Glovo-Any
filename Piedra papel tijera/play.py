
from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2


class Play(object):
    '''
    Representa una jugada
    '''
    def description(self):   #Es comun a todas las subclases, pero en cada subclase se pisa/re escribe.
        pass
    
    def compare(self,otherPlay):
        '''
        Se compara con la otra jugada y devuelve un Result de la comaaracion
        '''
        pass


class Paper(Play):
    def description(self):
        return "Paper"

    def compare(self,otherPlay):
        '''
        Compara papel con otras jugadas y devuelve un Result
        '''
        result = None
        if type(otherPlay) == Paper:  #Se comparan las clases
            result = Result.EQUAL
        elif type(otherPlay) == Scissors:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result

class Scissors(Play):
    def description(self):
        return "Scissors"

    def compare(self,otherPlay):
        '''
        Compara tijera con otras jugadas y devuelve un Result
        '''
        result = None
        if type(otherPlay) == Scissors:
            result = Result.EQUAL
        elif type(otherPlay) == Rock:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result


class Rock(Play):
    def description(self):
        return "Rock"

    def compare(self,otherPlay):
        '''
        Compara roca con otras jugadas y devuelve un Result
        '''
        result = None
        if type(otherPlay) == Rock:
            result = Result.EQUAL
        elif type(otherPlay) == Paper:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result
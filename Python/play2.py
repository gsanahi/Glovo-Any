from enum import Enum

class Result(Enum):
        EQUAL = 0
        WINS = 1
        LOSES = 2

class Play(object):
    """
    Representa un ajugada
    """

    def description(self):
        pass

    def compare(self, otherPlay):
        """
        Se compara con la otra jugada y devuelve un Result
        de la comparación
        """
        pass

class Paper(Play):
    def description(self):
        return "Paper"
    
    def compare(self, otherPlay):
        """
        Compara papel con otras jugadas y devuelve un Result
        """
        result = None
        if type(otherPlay) == Paper:
            result = Result.EQUAL
        elif type(otherPlay) == Scissors:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result

class Scissors(Play):
    def description(self):
        return "Scissors"

    def compare(self, otherPlay):
        if self.__class__ == otherPlay.__class__:
            return Result.EQUAL
        elif type(otherPlay) == Paper :
            return Result.WINS
        else:
            return Result.LOSES


class Rock(Play):

    def description(self):
        return "Rock"

    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Paper:
            result = Result.LOSES
        elif type(otherPlay) == Scissors:
            result = Result.WINS
        else:
            result = Result.EQUAL
        return result



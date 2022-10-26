
from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2


class Play(object):
    '''
    Representa una jugada
    '''
    def beats(self):
        pass

    def description(self):   #Es comun a todas las subclases, pero en cada subclase se pisa/re escribe.
        pass
    
    def compare(self,otherPlay):
        '''
        Compara papel con otras jugadas y devuelve un Result
        '''
        #Si self y otherPlay son iguales hay empate
        if self == otherPlay:
            return Result.EQUAL
        #Si otherPlay esta en mi beats, le gano yo
        elif otherPlay in self.beats():
            return Result.WINS
        #Sino, gana OtherPlay y yo pierdo
        else:
            return Result.LOSES

    #Dunders  --> estos dos van siempre siempre juntos
    def __eq__(self,other):
        '''
        Devuelve True si self y other son equivalentes
        '''
        if isinstance(self, other.__class__):
            #talvez seamos iguales, comprermos propiedades
            return self.description() == other.description()
        else:
            # no podemos ser iguales
            return False

    def __hash__(self):
        '''
        Devuelve un hash que represente al atributo de self que lo hace diferente
        '''
        return hash(self.description())

        __lt__ 
        __gt__ 


class Paper(Play):
    def beats(self):
        return {Rock(),Spock()}

    def description(self):
        return "Paper"

   

class Scissors(Play):
    def beats(self):
        return {Paper(), Lizard()}

    def description(self):
        return "Scissors"

    

class Rock(Play):
    def beats(self):
        return {Scissors(),Lizard()}

    def description(self):
        return "Rock"


class Lizard(Play):
    def beats(self):
        return {Spock(),Paper()}

    def description(Self):
        return "Lizard"


class Spock(Play):
    def beats(self):
        return {Scissors(), Rock()}

    def description(Self):
        return "Spock"
    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Spock:
            result = Result.EQUAL
        elif type(otherPlay) == Paper or type(otherPlay) == Lizard:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result
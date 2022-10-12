from enum import Enum

class Affiliation(Enum):
    REBEL_ALLIANCE = 0
    GALATIC_EMPIRE = 1
    UNKNOWN = 2 

class StarWarsCharacter:   # Clase base / padre
    def __init__ (self, name, alias, affiliacion):
        self.name = name
        self.alias = alias
        self.affiliacion = affiliacion

    def __repr__(self):
        return 'f < {self.__class__} {self.name} {self.alias} > '

class ForceSensitive(StarWarsCharacter):
    def __init__(self, name, alias, affiliation, midiclorians):
        super().__init__(name, alias, affiliation)
        self.midiclorians = midiclorians
    
    def unsheath(self):
        return ' ▍░▐░░▣░▒░▒░▒▕' + "█" * 40

chewi = StarWarsCharacter('Chewbacca',' Chewi',Affiliation.REBEL_ALLIANCE)
jabba = StarWarsCharacter('Jabba Dassilic Tiure',' Jabba The Hutt', Affiliation.UNKNOWN)

class Jedi(ForceSensitive): #Clase heredara del padre - ForceSensitive-
    def __init__(self, name, alias, midiclorians):
        super().__init__(name,alias, Affiliation.REBEL_ALLIANCE, midiclorians)        # lo agarro de la clase padre
        
         

class Sith(ForceSensitive):
    def __init__ (self, name, alias, midiclorians):
        super().__init__(name, alias, Affiliation.GALATIC_EMPIRE,midiclorians)


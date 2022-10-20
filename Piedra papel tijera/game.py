from multiprocessing.sharedctypes import Value
from random import choice
from play import Paper,Rock, Scissors, Lizard, Spock

def run_game():
    """
    Arranca el juego
    """
    display_game()
    while True:
        #Nueva partida
        user_play = get_user_play_dict() #Jugada del usurio
        comp_play = random_play()  #Jugada del ordenador
        display_match(user_play, comp_play) #muestro jugada
        winner = get_winner(user_play, comp_play) #averiguo vencedor
        if winner == None: # empate
            display_tie(user_play, comp_play)
        else:
            display_victory(winner)
            #Pregunto al usuario y si quiere salir uso un break
        resp = another_match()
        if resp == False:
            break
    print(choice(["What's wrong with you?" , "Eres un Cobarde", "buuuuu", "Gallina!" ]))
    
def display_match(play1, play2):
    print(f'{play1.description()} vs {play2.description()}   FIGHT!\n')
    
def display_game():
    """
    Muestra el nombre del juego
    """
    print('\n\n\t\tRock Paper Scissors Lizard Spock\n\n')

def get_user_play():
    """
    Le pregunta al usuario qué quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    elif res == 3:
        return Scissors()
    elif res == 4:
        return Lizard()
    else:
        return Spock()
    
def get_user_play_dict():
    choice = get_user_response()
    options = {
        1 : Rock(),
        2 : Paper(),
        3 : Scissors(),
        4 : Lizard(),
        5 : Spock()
    }
    return options[choice]


def get_user_response():
    """
    Presenta un menu de opciones y pide que seleccione una.
    Devuelve una cadena que indica lo que ha elegido
    """
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock ")
        print("2. Paper ")
        print("3. Scissors ")
        print("4. Lizard ")
        print("5. Spock")
    
        raw = input("Enter 1, 2, 3, 4 or 5 \n")
        # validar raw
        raw = raw.strip()
        if raw == "1":
            response = 1
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3":
            response = 3
            break
        elif raw == "4":
            response = 4
            break
        elif raw == "5":
            response = 5
            break

    return response

def random_play():
    """
    Selecciona una jugada al azar para competir con el usuario
    """
    return choice([Paper(), Rock(), Scissors(), Lizard(), Spock()])

def get_winner(play1, play2):
    """
    Obtiene el ganador o None si hay empate.
    """
    
    result = play1.compare(play2)
    winner = ""
    if result == result.WINS:
        winner = play1
    elif result == result.EQUAL:
        winner = None
    else: winner = play2
    return winner


def display_tie(play1, play2):
    """
    Imprime que ha habido un empate
    """
    print(f'Empate entre dos {play1.description()}')

def display_victory(winner):
    """
    Muestra que winner ha ganado
    """
    print(f'Ha ganado {winner.description()}')

def another_match():
    new_match = (input("Do you want to play another match? S/N  ")).upper()
    play_again = None
    if new_match == "S":
        play_again = True
    elif new_match == "N":
        play_again = False
    else:
        print("Invalid option.")
    return play_again


if __name__ == '__main__':
    run_game()



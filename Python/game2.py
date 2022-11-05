from random import choice
from play2 import Paper, Rock, Scissors

def run_game():
    """
    Arranca el juego
    """
    display_game()
    user_play = get_user_play()
    comp_play = random_play()
    display_match(user_play, comp_play)
    winner = get_winner(user_play, comp_play)
    if winner == None: # empate
        display_tie(user_play, comp_play)
    else:
        display_victory(winner)
    
def display_match(play1, play2):
    print(f'{play1.description()} vs {play2.description()}   FIGHT!\n')
    
def display_game():
    """
    Muestra el nombre del juego
    """
    print('\n\n\t\tRock Paper Scissors\n\n')

def get_user_play():
    """
    Le pregunta al usuario qué quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    else:
        return Scissors()
    

def get_user_response():
    """
    Presenta un menu de opciones y pide que seleccione una.
    Devuelve una cadena que indica lo que ha elegido
    """
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock 🪨")
        print("2. Paper 🧻")
        print("3. Scissors ✂️")
    
        raw = input("Enter 1, 2 or 3\n")
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
        else:
            continue
            
    return response

def random_play():
    """
    Selecciona una jugada al azar para competir con el usuario
    """
    return choice([Paper(), Rock(), Scissors()])

def get_winner(play1, play2):
    """
    Obtiene el vencedor o None si hay empate
    """
    return play1


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


if __name__ == '__main__':
    run_game()
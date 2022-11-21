from random import choice
from play import Paper, Scissors, Rock, Result, Lizard, CaptainSpock

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
    while another_match():
        run_game()
    print(choice(["What's wrong with you?", "¿Eres un gallina, McFly?", "¡Cobarde!"]))
    

def display_match(play1, play2):
    print(f"\n{play1.description()} vs {play2.description()} FIGHT!\n")

def display_game():
    """
    Muestra el nombre del juego
    """

    print("Rock, paper, scissors, lizard, CaptainSpock")

def get_user_play():
    """
    Le pregunta al usuario qué quiere jugar y lo devuelve.
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
        return CaptainSpock()

def get_user_response():
    """
    Presenta un menú de opciones y pide que selecione una.
    Devuelve una cadena que indica lo que ha elegido.
    """
    response = None
    while True:
        print("\nChose your play: \n")
        print("1. Rock ")
        print("2. Paper ")
        print("3. Scissors ")
        print("4. Lizard ")
        print("5. CaptainSpock")

        raw = input("\nEnter 1, 2, 3, 4 or 5  ")

        raw = raw.strip() # Para quitar espacios en blanco delante o detrás.
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
    Seleccion una jugada al azar para competir con el usuario.
    Utilizamos el choice importado de Python para que nos devuelva un aleatorio.
    """
    return choice([Paper(), Rock(), Scissors(), Lizard(), CaptainSpock()])
    
def get_winner(play1, play2):
    """
    Obtiene el ganador o None si hay empate.
    """
    
    result = play1.compare(play2)
    winner = ""
    if result == Result.WINS:
        winner = play1
    elif result == Result.EQUAL:
        winner = None
    else: winner = play2
    return winner
        
def display_tie(play1, play2):
    """
    Imprime que ha habido un empate.
    """
    print(f"Empate entre dos {play1.description()} \n")

def display_victory(winner):
    """
    Muestra que winner ha ganado.
    """
    print(f"The winner is {winner.description()} \n")

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

if __name__ == "__main__":
    run_game()
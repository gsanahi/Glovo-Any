def run_game():
    '''
    arranca el juego
    '''
    display_game():
    user_play = get_user_play()
    comp_play = random_play()
    winner = get_winner(user_play,comp_play)
    if winner == None: #empate
        display_tie(user_play, comp_play)
    else:
        display_victory(winner)

def display_game():
    ''' 
    Muestra el nombre del juego
    '''
    pass

def get_user_play():
    '''
    Le pregunta al usuario que quiere jugar y lo devuelve
    '''
    pass

def get_user_play():
    '''
    Selecciona una jugada al azar para competir con el usuario
    '''
    pass

def get_winner():
    
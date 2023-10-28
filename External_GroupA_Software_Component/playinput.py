# File for player input things only 



def decide_name(player):
    """
    Players can input name
    Return: Players inputted name (to be used as argument for player objective)
    """
    name = input(f'What do you want to be named {player}? ')
    return name

def choose_slot():
    """
    Players input a slot
    Return: The chosen slot
    """
    slot = input('Please input where you want to place your piece on an empty slot:')
    return slot

def choose_piece():
    """
    Player inserts a slot nr that is occupied by the piece they want to chose
    """
    slot = input('Please input the slot nr containing piece')
    #Here make a check on board so that slot is not empty! 
    #Find the piece, return the piece etc.
    return slot #for now
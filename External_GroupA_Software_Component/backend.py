import playinput
import player #as playerclass



def display_winner(player1, player2):
    """ 
    Function displays who has won the game
    Parameters: player1 and player2 objectives
    Precon: Only allowed to be called inside/after a function that beforehand checks all draw cons
    """
    if player1.pieces_remaining > player2.pieces_remaining:
        print(f'The winner is {player1.name}!')
    elif player1.pieces_remaining < player2.pieces_remaining:
        print(f'The winner is {player2.name}!')


def draw_condition_checker(counter):
    """
    Checks all draw conditions
    PArameters: Counter - a counter that keeps track of how many rounds have been played
    Return: True - Its a draw. False - Its not a draw
    """
    if counter > 200:
        return True
#TODO: Im not sure of all draws that can happen, but we just add more elif for each condition and more parameters


def check_turn(player1, player2):
    """
    Function that tells which players turn it is.
    Parameters: player1 and player2 objectives
    """
    if player1.current_turn:
        print(f'Its {player1.name} turn')
        return player1
    elif player2.current_turn:
        print(f'Its {player2.name} turn')
        return player2
    else:
        print('BUG OCCURED')        # TODO: Handle when its no players turn (Error handling)


# This function should be used AFTER a turn has been done, and we want to change it so its the next players turn
def change_turn(player1, player2):
    """
    Changes whos turn it is to play
    Paremeters: player1 and player2 objects
    """
    if player1.current_turn:
        player1.make_not_players_turn()
        player2.make_players_turn()
        return player2
    elif player2.current_turn:
        player1.make_players_turn()
        player2.make_not_players_turn()
        return player1


def move_a_piece(player1, player2, move_from, move_to):
    """ 
    Makes players list of placed pieces be correct
    Parameters: player - object of player that moves piece. move_from - Where piece was. move_to - Where piece should be placed
    Precon: Must check if legal move beforehand
    Return: True - the move went trough. False - The move could not be made (either because the piece didnt exist, or the new spot was not avalible)
    """
    if move_from in player1.players_pieces and move_to not in player2.players_piece and move_to not in player1.players_piece:
        player.remove_placed_piece(move_from)
        player.add_placed_piece(move_to)
        return True
    else:
        print("Faulty move") #TODO: Add better error message
        return False


def end_game(player1, player2):
    """ 
    Checks if a player has lost and displays winner.
    parameters: players, both players.
    Precon: end of turn
    return: True if someone has lost, else false.
    """
    if player1.have_player_lost() or player2.have_player_lost():
        display_winner(player1, player2)
        return True                                 # If someone has lost, the game should end. (This True will be used in other func to end game)
    else:
        return False
    
# Should be called after a turn (and move_a_piece has been done) to see if player has created a new mill,. This function checks so that it is not a mill that has been created earlier in the game.
def check_for_mills(player):
    """"
    Checks if a player has created a new mill
    Parameters: player object
    Return: True - player has created a mill turn. False - player has not created a new mill this turn.
    """
    mills = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R'],['S','T','U'],['V','W','X'],['A','J','V'],['D','K','S'],['G','L','P'],['B','E','H'],['Q','T','W'],['I','M','R'],['F','N','U'],['F','N','U'],['C','O','X'],['A','D','G'],['F','I','C'],['R','U','X'],['P','S','V']]
    i = 0
    while i < len(mills):
        if all(elem in player.players_pieces for elem in mills[i]):     
            if mills[i] not in player.mill_combos_cr:
                player.mill_combos_cr.append(mills[i])
                return True
            i += 1
        else:
            i += 1

    return False
# Class that handels player

class Player:
    def __init__(self, name, figure):
        """ 
        Creates the player and adds it stats
        Parameters: name of player object, decided piece figure
        """
        self.name = name                # Incase we wanna let the players give themsels names ;) Else this field will always have the input "player1" or "player2"
        self.pieces_remaining = 12      # All players start with 12 pieces in the beginning of the game (This property will be used to check if player lost, also if game can continiou)
        self.sign = figure        # Decides if player is X or O (or 1, 0 ect. Depending on what we decide)
        self.placed_pieces = 0          # Players always have 0 placed pieces in the start (property used to check if first phase of game is over)
        self.current_turn = False       # (Property used to tell wich players turn it currently is) Is false in beginning, until random func desides who start
        self.players_pieces = []        # Array that hold all the spot a player has a piece in.
        self.mill_count = 0
        self.mill_combos_cr = []        #mill combinations that have already been created and can not be recreated


    def lost_pieces(self):
        """Takes away on piece in the count"""
        self.pieces_remaining -= 1      # A player can only lose 1 piece per round, so this func can harddefine '-1'
           

    def make_players_turn(self):
        """to make it players turn"""
        self.current_turn = True        # (Other funcs now can tell its this players turn)


    def make_not_players_turn(self):
        """to make it NOT players turn"""
        self.current_turn = False        # (Other funcs now can tell its NOT this players turn)


    def place_piece(self):
        """Place a piece on the board in the beginning of the game."""
        if self.placed_pieces < 12:     # If placed_pieces is not 12, Phase 1 is not done yet. Ensures players cant place more than allowed amount of pieces in beginning
            self.placed_pieces += 1


    def add_placed_piece(self, piece):
        """
        Adds a piece to "currently placed pieces address"
        Parameters: piece - the address of where the piece is placed
        Precon: Calls in phase1 when moving pieces and when a piece is moved in phase2+3
        """
        self.players_pieces.append(piece.upper())
    
    
    def remove_placed_piece(self, piece):
        """
        Removes the information about where a piece that is placed 
        Parameters: piece - the address of where the piece is removed from
        Precon: (Calls only when a piece is lost, or a piece is moved). 
        Precon: Only legal to call when pieces exist and are placed.
        """
        if piece in self.players_pieces:
            self.players_pieces.remove(piece.upper())


    def have_player_lost(player):
        """
        Checks if a player has lost
        Return: If true, the player has lost. If false, player has not lost
        """
        if player.pieces_remaining < 3:     #Number 3 since when player les pieces than 3, they have lost
            return True
        else:
            return False
        
    
    
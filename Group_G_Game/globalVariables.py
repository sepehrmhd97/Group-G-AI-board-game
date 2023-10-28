

moveCounter = 0

validMills = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
         (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23))


whiteRemoved = 0
blackRemoved = 0

Trees = \
	((9, 0, 1, 2, 21), (9, 21, 22, 0, 23), (1, 2, 14, 0, 23), (22, 23, 14, 21, 2), (10, 3, 4, 5, 18), (4, 5, 13, 3, 20),
	 (10, 18, 19, 3, 20), (19, 20, 13, 18, 5), (11, 6, 7, 15, 8), (7, 8, 12, 6, 17), (11, 15, 16, 6, 17),
	 (16, 17, 12, 15, 8), (0, 1, 4, 7, 2), (2, 1, 4, 0, 7), (21, 22, 19, 16, 23), (23, 22, 19, 16, 21),
	 (0, 9, 10, 11, 21),
	 (21, 9, 10, 11, 0), (2, 13, 14, 12, 23), (13, 14, 23, 12, 2), (3, 4, 7, 5, 1), (3, 4, 1, 7, 5), (4, 5, 7, 3, 1),
	 (5, 4, 1, 7, 3), (22, 19, 18, 20, 16), (18, 19, 16, 22, 20), (20, 19, 22, 16, 18), (20, 19, 16, 18, 22),
	 (3, 10, 11, 9, 18), (3, 9, 10, 11, 18), (18, 10, 11, 9, 3), (18, 10, 9, 11, 3), (5, 12, 13, 14, 20),
	 (5, 13, 14, 12, 20),
	 (20, 13, 14, 12, 5), (20, 13, 12, 5, 14), (6, 7, 4, 1, 8), (8, 7, 4, 1, 6), (6, 11, 10, 9, 15), (15, 11, 10, 6, 9),
	 (15, 16, 19, 17, 22), (16, 17, 19, 15, 22), (17, 12, 13, 8, 14), (8, 12, 13, 14, 17))


validAdjacent = {0: (1, 9), 1: (0, 2, 4), 2: (1, 14), 3: (4, 10), 4: (1, 3, 5, 7), 5: (4, 13), 6: (7, 11),
           7: (4, 6, 8), 8: (7, 12), 9: (0, 21, 10), 10: (3, 9, 11, 18), 11: (6, 10, 15), 12: (8, 13, 17),
           13: (5, 12, 14, 20), 14: (2, 13, 23), 15: (11, 16), 16: (15, 17, 19), 17: (12, 16),
           18: (10, 19), 19: (16, 18, 20, 22), 20: (13, 19), 21: (9, 22), 22: (19, 21, 23), 23: (14, 22)}



validDoubleMills = (
	(23, 22, 21, 9, 0), (21, 22, 23, 14, 2), (21, 9, 0, 1, 2), (0, 1, 2, 14, 23), (20, 19, 18, 10, 3),
	(18, 19, 20, 13, 5),
	(18, 10, 3, 4, 5), (20, 13, 5, 4, 3), (17, 16, 15, 11, 6), (15, 16, 17, 12, 8), (15, 11, 6, 7, 8),
	(6, 7, 8, 12, 17),
	(0, 1, 2, 4, 7), (21, 22, 23, 19, 16), (0, 9, 21, 10, 11), (2, 14, 23, 12, 13), (1, 4, 7, 3, 5), (3, 10, 18, 9, 11),
	(5, 13, 20, 12, 14), (16, 19, 22, 18, 20), (6, 7, 8, 4, 1), (6, 11, 15, 9, 10), (15, 16, 17, 19, 22),
	(8, 12, 17, 13, 14))

millPiece = {0: [(1, 2), (9, 21)], 1: [(0, 2), (4, 7)], 2: [(0, 1), (14, 23)], 3: [(4, 5), (10, 18)],
               4: [(3, 5), (1, 7)],
               5: [(13, 20), (3, 4)], 6: [(7, 8), (11, 15)], 7: [(1, 4), (6, 8)], 8: [(6, 7), (12, 17)],
               9: [(0, 21), (10, 11)],
               10: [(9, 11), (3, 18)], 11: [(15, 6), (9, 10)], 12: [(8, 17), (13, 14)], 13: [(12, 14), (5, 20)],
               14: [(2, 23), (12, 13)],
               15: [(16, 17), (11, 6)], 16: [(15, 17), (19, 22)], 17: [(12, 8), (15, 16)], 18: [(3, 10), (19, 20)],
               19: [(18, 20), (16, 22)],
               20: [(13, 5), (18, 19)], 21: [(0, 9), (22, 23)], 22: [(21, 23), (16, 19)], 23: [(2, 14), (21, 22)]}


emptyField = {0: '0', 1: '1', 2: '2', 3:'3', 4: '4',  5: '5', 6: '6', 7: '7', 8: '8',  9: '9', 10: '10', 11: '11', 12: '12', 13: '13',
            14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21', 22: '22', 23: '23'}

# FIRST PHASE IS INIT
PHASE = 'INIT'
PHASECOPY = 'INIT' # I NEED THIS WHEN I AM SIMULATING MOVES AHEAD IN TREE
MAXIMUM = 10e9

TABLE = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']




# In the FLY phase, if both players remained with 3 figures, if after there is no
# winner after 20 moves, then the game is drawn
# COUNTPLAYSFLY = 0

# max time for computer to perform the move is 3 seconds
aiTime = 6
startTime = None

variable1 = ""
variable2 = ""


rules = str('+===================================================================+===| +\n'
	      '| RULES OF THE GAME :                                               |\n'
	      '| At the beginning, every playes has 9 pieces. The goal of the game |\n'
	      '| is to leave your opponent with only two pieces or leave him       |\n'
	      '| without any possible moves. Table has 24 fields and it is possible|\n'
	      '| to move only to adjacent fields, if they are free. If one of the  |\n'
	      '| players make mill (three pieces in a row) then he can remove one  |\n'
	      '| opponent\'s piece by choosing one of the fields where opponent     |\n'
	      '| placed his piece. NOTE: it\'s not allowed to remove opponent piece |\n'
	      '| if it\'s already in a MILL, unless his all pieces are in MILLS,    |\n'
	      '| then you can remove any piece you want. You can remove piece in   |\n'
	      '| any phase of the game.                                            |\n'
	      '|                                                                   |\n'
	      '| PHASES OF THE GAME:                                               |\n'
	      '| 1. PHASE (INIT) -> in this phase both playes are intermittently   |\n                                                   |\n'
	      '| placing pieces on free fields ( 0 - 23 on the table). When player | \n'
	      '| run out of pieces to place, then we are moving to the next stage  |\n'
	      '| of the game.                                                      |\n'
	      '| 2. PHASE (MOVE) -> in this phase players can move their pieces to |\n'
	      '| adjacent free fields. First, they input the piece they want to    |\n'
	      '| move, and then the field where they want to move that piece.      |\n'
	      '| 3. PHASE (FLY) -> if the player remained with only 3 pieces,      |\n'
	      '| then he has additional opportunity to move his pieces to ANY free |\n'
	      '| field on the table, filed doesn\'t has to be adjecent and jumping  |\n'
	      '| over pieces is allowed.                                           |\n'
	      '|                                                                   |\n'
	      '| When one of the players remained with only 2 pieces, or the player|\n'
	      '| can\'t perform any move because every adjacent field is taken, the |\n'
	      '| game is over. Right now, your enemy is computer, can you beat him?|\n'
	      '| You can choose if you want to play first. Yours pieces are marked |\n'
	      '| as W (white) and computers pieces are marked as B (black).        |\n'
	      '|                         GOOD LUCK!                                |\n'
	      '+-------------------------------------------------------------------+\n')

# ALLPLACED = False

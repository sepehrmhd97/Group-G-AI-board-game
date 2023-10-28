import player as Player
class GameBoard:
    def __init__(self):
        """ 
        Represents a board, and its functions
        """
        # To decide if a move is legal from a position to another
        self.possibleMoves=[
        #A B C D E F G H I J K L M N O P Q R S T U V W X
        [0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #A
        [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #B
        [0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], #C
        [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], #D
        [0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #E
        [0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], #F
        [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], #G
        [0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #H
        [0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], #I
        [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0], #J
        [0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0], #K
        [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0], #L
        [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0], #M
        [0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0], #N
        [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1], #O
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0], #P
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0], #Q
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0], #R
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0], #S
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0], #T
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1], #U
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0], #V
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1], #W
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0]  #X
        #A B C D E F G H I J K L M N O P Q R S T U V W X
        ]
        # We need to show the original board to the players even if the pieces have put down
        self.boardmap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']
        # The actual board that we have to maintain during the game
        self.board=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

    def printBoard(self):
        board=self.board
        boardmap=self.boardmap
        print( 
            f'{board[0]}--------{board[1]}--------{board[2]}            {boardmap[0]}--------{boardmap[1]}--------{boardmap[2]}\n'
            f'| \      |      / |            | \      |      / |\n'
            f'|  {board[3]}-----{board[4]}-----{board[5]}  |            |  {boardmap[3]}-----{boardmap[4]}-----{boardmap[5]}  |\n'
            f'|  | \   |   / |  |            |  | \   |   / |  |\n'
            f'|  |  {board[6]}--{board[7]}--{board[8]}  |  |            |  |  {boardmap[6]}--{boardmap[7]}--{boardmap[8]}  |  |\n'
            f'|  |  |     |  |  |            |  |  |     |  |  |\n'
            f'{board[9]}--{board[10]}--{board[11]}     {board[12]}--{board[13]}--{board[14]}            {boardmap[9]}--{boardmap[10]}--{boardmap[11]}     {boardmap[12]}--{boardmap[13]}--{boardmap[14]}\n'
            f'|  |  |     |  |  |            |  |  |     |  |  |\n'
            f'|  |  {board[15]}--{board[16]}--{board[17]}  |  |            |  |  {boardmap[15]}--{boardmap[16]}--{boardmap[17]}  |  |\n'
            f'|  | /   |   \ |  |            |  | /   |   \ |  |\n'
            f'|  {board[18]}-----{board[19]}-----{board[20]}  |            |  {boardmap[18]}-----{boardmap[19]}-----{boardmap[20]}  |\n'
            f'| /      |      \ |            | /      |      \ |\n'
            f'{board[21]}--------{board[22]}--------{board[23]}            {boardmap[21]}--------{boardmap[22]}--------{boardmap[23]}\n'
        )

    def PutPieceToPosition(self, position, player):
        position=position.upper()
        valid=False
        if position in self.board:
            for i, n in enumerate(self.board):
                if n==position:
                    self.board[i]=player.sign
                    player.add_placed_piece(position)
                    valid=True
        else:
            print('You can not place a character there, try again with a different position')
        return valid

    def RemovePieceFromBoard(self,position,player,remove_own=False):
        position=position.upper()
        found=False
        if position in self.boardmap:
            for i, n in enumerate(self.board):
                if  ((not remove_own and n!=player.sign and n not in self.boardmap) or (remove_own and n not in self.boardmap)):
                    if self.boardmap[i]==position:
                        self.board[i]=self.boardmap[i]
                        found=True
            if not found:
                print('Your opponent does not have a piece at that position, try again with a different one')
        else:
            print('You gave an invalid position, try again with a different one')
        return found

    def movePieceOnBoard(self,position_from, position_to, player):
        position_from=position_from.upper()
        position_to=position_to.upper()
        if self.possibleMoves[self.boardmap.index(position_from)][self.boardmap.index(position_to)] == 1:
            self.RemovePieceFromBoard(position_from, player, True)
            self.PutPieceToPosition(position_to, player)
        else:
            print('This move is not possible')



    
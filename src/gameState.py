import decisionCoeff as dc
import globalVariables as globalVar
from copy import deepcopy


class State(object):
	def __init__(self, board, blackToMove, move, parent=None, nextStates=None):
		if nextStates == None:
			nextStates = []
		self.board = board
		self.blackToMove = blackToMove
		self.move = move
		self.parent = parent
		self.nextStates = nextStates

	def isTerminalState(self):
		loserIsBlack, loserIsWhite = False, False
		if dc.allPlayerPiecesClosed(self, 'B') or dc.getNumberOfPlayerPieces(self, 'B') < 3:
			loserIsBlack = True
		if dc.allPlayerPiecesClosed(self, 'W') or dc.getNumberOfPlayerPieces(self, 'W') < 3:
			loserIsWhite = True
		if (not loserIsBlack) and (not loserIsWhite):
			return False
		self.isLoserBlack = (not loserIsWhite)
		return True

	def getTerminal(self):
		if self.isLoserBlack: return -globalVar.MAXIMUM
		else: return globalVar.MAXIMUM

	def nextStatesInit(self):
		for i in range(24):
			if self.board[i] in globalVar.emptyField.values():
				boardCopy = deepcopy(self.board)
				if self.blackToMove:
					boardCopy[i] = 'B'
				else:
					boardCopy[i] = 'W'
				self.nextStates.append(State(boardCopy, not self.blackToMove, [i], self))

	def nextStatesMove(self):
		if self.blackToMove:
			player = 'B'
		else:
			player = 'W'
		for key, value in globalVar.validAdjacent.items():
			if self.board[key] == player:
				for index in value:
					if self.board[index] in globalVar.emptyField.values():
						boardCopy = deepcopy(self.board)
						boardCopy[index] = player
						boardCopy[key] = globalVar.emptyField[key]
						self.nextStates.append(State(boardCopy, not self.blackToMove, [key, index], self))

	def nextStatesFly(self):
		if self.blackToMove:
			player = 'B'
		else:
			player = 'W'
		player_pieces = dc.getAllPositionsOfPlayer(self, player)
		empty_pos = dc.getAllEmptyPositionsOnBoard(self)
		for piece in player_pieces:
			for cell in empty_pos:
				boardCopy = deepcopy(self.board)
				boardCopy[cell] = player
				boardCopy[piece] = globalVar.emptyField[piece]
				self.nextStates.append(State(boardCopy, not self.blackToMove, [piece, cell], self))

	def nextStatesMill(self):
		br = 0
		for i in range(24):
			if not dc.pieceInMill(self, i):
				if (self.blackToMove and self.board[i] == 'W') or ((not self.blackToMove) and self.board[i] == 'B'):
					boardCopy = deepcopy(self.board)
					boardCopy[i] = globalVar.emptyField[i]
					self.nextStates.append(State(boardCopy, not self.blackToMove, [i], self))
					br += 1
		if br == 0:
			for i in range(24):
				if (self.blackToMove and self.board[i] == 'W') or ((not self.blackToMove) and self.board[i] == 'B'):
					boardCopy = deepcopy(self.board)
					boardCopy[i] = globalVar.emptyField[i]
					self.nextStates.append(State(boardCopy, not self.blackToMove, [i], self))

	def makeChildren(self, phase):
		if len(self.nextStates) == 0:
			if phase == 'INIT':
				self.nextStatesInit()
			if phase == 'MILL':
				self.nextStatesMill()
			if phase == 'MOVE':
				self.nextStatesMove()
			if phase == 'FLY':
				self.nextStatesFly()

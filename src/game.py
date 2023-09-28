import globalVariables as globalVar
import pretty_print as pp
from gameState import State
import decisionCoeff as dc
import sys
import userGameMoves
import random
from colorama import Fore, Back, Style
from time import time
from copy import deepcopy


def play(gameState):
	checkGameOver(gameState)
	print('Moves remaining',300 - globalVar.moveCounter)
	globalVar.moveCounter+=1
	

	millIsMade = False
	if gameState.parent is not None:
		if gameState.blackToMove:
			if dc.millHasBeenMadeInLastTurn(gameState, 'W'):
				millIsMade = True
				gameState.blackToMove = False
				userGameMoves.userGameMoves(gameState, True)
		else:
			if dc.millHasBeenMadeInLastTurn(gameState, 'B'):
				millIsMade = True
				gameState.blackToMove = True
				aiPlay(gameState, True)
	if not millIsMade:
		if gameState.blackToMove:
			aiPlay(gameState, False)
		else:
			userGameMoves.userGameMoves(gameState, False)


def checkGameOver(gameState):

	if(globalVar.moveCounter >= 300):
		print("DRAW , number of moves has exceeded 300")
		sys.exit()

	print("Empty positions" ,  dc.getAllEmptyPositionsOnBoard(gameState))
		



	if globalVar.PHASE != 'INIT':
		if dc.allPlayerPiecesClosed(gameState,'B') or dc.getNumberOfPlayerPieces(gameState,'B') < 3:
			print(Back.GREEN + '=========================CONGRATULATIONS, YOU WIN!=========================')
			sys.exit()
		if dc.allPlayerPiecesClosed(gameState, 'W') or dc.getNumberOfPlayerPieces(gameState, 'W') < 3:
			print(Back.RED+'===========================YOU LOSE!==========================')
			sys.exit()



# minMax algorithm
# min value
def minValue(gameState, alpha, beta, depth, phase, flyPrevious=False):
	val = globalVar.MAXIMUM
	gameState.makeChildren(phase)
	for successor in gameState.nextStates:
		val = min(val, alphaBeta(successor, alpha, beta, depth - 1, phase, flyPrevious))
		if val <= alpha: return val
		beta = min(beta, val)
	return val

# minMax algorithm
# max value
def maxValue(gameState, alpha, beta, depth, phase, flyPrevious=False):
	val = -globalVar.MAXIMUM
	gameState.makeChildren(phase)
	for successor in gameState.nextStates:
		val = max(val, alphaBeta(successor, alpha, beta, depth - 1, phase, flyPrevious))
		if val >= beta: return val
		alpha = max(alpha, val)
	return val

# alphaBeta Pruning
def alphaBeta(gameState, alpha, beta, depth, phase, flyPrevious=False):
	if phase == 'MILL':
		if flyPrevious is False:
			phase = globalVar.PHASECOPY
		else:
			phase = 'FLY'

	if phase == 'MOVE':
		if (gameState.blackToMove and dc.getNumberOfPlayerPieces(gameState, 'B') == 3) or \
				((not gameState.blackToMove) and dc.getNumberOfPlayerPieces(gameState, 'W')) == 3:
			phase = 'FLY'

	if gameState.isTerminalState() and phase != 'INIT':
		return gameState.getTerminal()
	if depth <= 0 or (time() - globalVar.startTime) > globalVar.aiTime:
		return dc.evalute(gameState, phase)

	if gameState.parent is not None:
		if gameState.blackToMove:
			if dc.millHasBeenMadeInLastTurn(gameState, 'W'):
				gameState.blackToMove = False
				if phase == 'FLY':
					#gameState.blackToMove = False
					return minValue(gameState, alpha, beta, depth, 'MILL', True)
				else:
					return minValue(gameState, alpha, beta, depth, 'MILL')
		else:
			if dc.millHasBeenMadeInLastTurn(gameState, 'B'):
				gameState.blackToMove = True
				if phase == 'FLY':
					#gameState.blackToMove = True
					return maxValue(gameState, alpha, beta, depth, 'MILL', True)
				else:
					return maxValue(gameState, alpha, beta, depth, 'MILL')

	if gameState.blackToMove:
		return maxValue(gameState, alpha, beta, depth, phase)
	else:
		return minValue(gameState, alpha, beta, depth, phase)


def aiNextMove(gameState, mill):
	globalVar.startTime = time()
	depth = 4

	if dc.getNumberOfPlayerPieces(gameState, 'B') + globalVar.blackRemoved == 9:
		globalVar.PHASE = 'MOVE'
	else:
		globalVar.PHASE = 'INIT'

	if dc.getNumberOfPlayerPieces(gameState, 'B') == 3 and globalVar.PHASE != 'INIT':
		globalVar.PHASE = 'FLY'
		depth = 2

	globalVar.PHASECOPY = globalVar.PHASE

	if mill:
		gameState.makeChildren('MILL')
	else:
		gameState.makeChildren(globalVar.PHASECOPY)
	depth -= 1

	bestMove = None
	alpha = -globalVar.MAXIMUM
	for successor in gameState.nextStates:
		if time() - globalVar.startTime > globalVar.aiTime: break
		score = alphaBeta(successor, -globalVar.MAXIMUM, globalVar.MAXIMUM, depth, globalVar.PHASECOPY)
		if score >= alpha:
			alpha, bestMove = score, successor.move
		if alpha >= globalVar.MAXIMUM:
			break
	return bestMove


def aiPlay(gameState, mill):
	move = aiNextMove(gameState, mill)
	old_state_table = deepcopy(gameState.board)
	if mill:
		globalVar.TABLE[move[0]] = globalVar.emptyField[move[0]]
		pp.print_table(gameState.board)
		print(Back.RED+Back.YELLOW+"The AI just made the MILL and dc. removed your piece from {}. field.".format(move[0]))
		globalVar.whiteRemoved += 1
	elif globalVar.PHASE == 'INIT':
		globalVar.TABLE[move[0]] = 'B'
		pp.print_table(gameState.board)
		print(Back.YELLOW+"The AI has placed piece at {}. field.".format(move[0]))
	elif globalVar.PHASE == 'MOVE' or globalVar.PHASE == 'FLY':
		globalVar.TABLE[move[1]] = 'B'
		globalVar.TABLE[move[0]] = globalVar.emptyField[move[0]]
		pp.print_table(gameState.board)
		print(Back.YELLOW+"The AI has moved piece from {}. field to {}. field.".format(move[0], move[1]))
	gameState.board = old_state_table
	new_state = State(globalVar.TABLE, False, move, gameState)
	play(new_state)


if __name__ == '__main__':
	
	print("GROUP G")
	print(Fore.YELLOW+Back.LIGHTBLACK_EX + '+================================================================\n'
	      '|                     Figure : Board                            |\n'     
	      '+================================================================\n'
	      '         0 --------------1 ---------------2         |\n'
	      '         |               |                |         |\n'
	      '         |    3 ---------4 ----------5    |         |\n'
	      '         |    |          |           |    |         |\n'
	      '         |    |    6 ----7 -----8    |    |         |\n'
	      '         |    |    |            |    |    |         |\n'
	      '         9 ---10---11           12---13---14        |\n'
	      '         |    |    |            |    |    |         |\n'
	      '         |    |    15----16----17    |    |         |\n'
	      '         |    |          |           |    |         |\n'
	      '         |    18---------19---------20    |         |\n'
	      '         |               |                |         |\n'
	      '         21--------------22---------------23        |\n'
	      '                                                    |\n'
	      '---------------------------------------------------+\n'
	      '+-------------------------------------------------------------------+\n')


	print(Fore.WHITE+"PLease select difficulty")
	print("1. Easy    2. Medium    3. Hard")
	ch = int(input())
	if(ch == 1):
		globalVar.aiTime = 1
	elif(ch ==2):
		globalVar.aiTime = 3
	elif(ch==3):
		globalVar.aiTime = 6
	else:
		print("invalid input")
		exit()
	while True:
		# random 
		x = random.randint(1,2)

		if x == 1:
			inp = "y"
		else:
			inp = "n"
		if inp == 'yes' or inp == 'y':
			gameState = State(globalVar.TABLE, False,[])
			break
		if inp == 'no' or inp == 'n':
			gameState = State(globalVar.TABLE, True, [])
			break
	play(gameState)
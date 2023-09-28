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
	"""Play the game with the given game state.

    :param gameState: The current game state.
    """
	checkGameOver(gameState)
	print('Moves remaining',300 - globalVar.moveCounter)
	globalVar.moveCounter+=1
	

	millIsMade = False
	if gameState.parent is not None:
		if gameState.blackToMove:
			if dc.millHasBeenMadeInLastTurn(gameState, globalVar.variable2):
				millIsMade = True
				gameState.blackToMove = False
				userGameMoves.userGameMoves(gameState, True)
		else:
			if dc.millHasBeenMadeInLastTurn(gameState, globalVar.variable1):
				millIsMade = True
				gameState.blackToMove = True
				aiPlay(gameState, True)
	if not millIsMade:
		if gameState.blackToMove:
			aiPlay(gameState, False)
		else:
			userGameMoves.userGameMoves(gameState, False)


def checkGameOver(gameState):
	"""Check if the game is over and handle game termination.

    :param gameState: The current game state.
    """

	if(globalVar.moveCounter >= 300):
		print("DRAW , number of moves has exceeded 300")
		sys.exit()

	print("Empty positions" ,  dc.getAllEmptyPositionsOnBoard(gameState))
		



	if globalVar.PHASE != 'INIT':
		if dc.allPlayerPiecesClosed(gameState,globalVar.variable1) or dc.numberOfPlayerPieces(gameState,globalVar.variable1) < 3:
			print(Back.GREEN + '=========================CONGRATULATIONS, YOU WIN!=========================')
			sys.exit()
		if dc.allPlayerPiecesClosed(gameState, globalVar.variable2) or dc.numberOfPlayerPieces(gameState, globalVar.variable2) < 3:
			print(Back.RED+'===========================YOU LOSE!==========================')
			sys.exit()



def minValue(gameState, alpha, beta, depth, phase, flyPrevious=False):
	"""Calculate the minimum value using the Minimax algorithm with alpha-beta pruning.

    :param gameState: The current game state.
    :param alpha: Alpha value for pruning.
    :param beta: Beta value for pruning.
    :param depth: Current depth in the search tree.
    :param phase: The phase of the game ('INIT', 'MOVE', or 'FLY').
    :param flyPrevious: Indicates if the previous phase was 'FLY'.
    :return: The minimum value.
    """
	val = globalVar.MAXIMUM
	gameState.makeChildren(phase)
	for successor in gameState.nextStates:
		val = min(val, alphaBeta(successor, alpha, beta, depth - 1, phase, flyPrevious))
		if val <= alpha: return val
		beta = min(beta, val)
	return val

def maxValue(gameState, alpha, beta, depth, phase, flyPrevious=False):
	"""Calculate the maximum value using the Minimax algorithm with alpha-beta pruning.

    :param gameState: The current game state.
    :param alpha: Alpha value for pruning.
    :param beta: Beta value for pruning.
    :param depth: Current depth in the search tree.
    :param phase: The phase of the game ('INIT', 'MOVE', or 'FLY').
    :param flyPrevious: Indicates if the previous phase was 'FLY'.
    :return: The maximum value.
    """
	val = -globalVar.MAXIMUM
	gameState.makeChildren(phase)
	for successor in gameState.nextStates:
		val = max(val, alphaBeta(successor, alpha, beta, depth - 1, phase, flyPrevious))
		if val >= beta: return val
		alpha = max(alpha, val)
	return val

def alphaBeta(gameState, alpha, beta, depth, phase, flyPrevious=False):
	"""Perform alpha-beta pruning to evaluate the game state.

    :param gameState: The current game state.
    :param alpha: Alpha value for pruning.
    :param beta: Beta value for pruning.
    :param depth: Current depth in the search tree.
    :param phase: The phase of the game ('INIT', 'MOVE', or 'FLY').
    :param flyPrevious: Indicates if the previous phase was 'FLY'.
    :return: The heuristic evaluation score for the game state.
    """
	if phase == 'MILL':
		if flyPrevious is False:
			phase = globalVar.PHASECOPY
		else:
			phase = 'FLY'

	if phase == 'MOVE':
		if (gameState.blackToMove and dc.numberOfPlayerPieces(gameState, globalVar.variable1) == 3) or \
				((not gameState.blackToMove) and dc.numberOfPlayerPieces(gameState, globalVar.variable2)) == 3:
			phase = 'FLY'

	if gameState.isTerminalState() and phase != 'INIT':
		return gameState.getTerminal()
	if depth <= 0 or (time() - globalVar.startTime) > globalVar.aiTime:
		return dc.evalute(gameState, phase)

	if gameState.parent is not None:
		if gameState.blackToMove:
			if dc.millHasBeenMadeInLastTurn(gameState, globalVar.variable2):
				gameState.blackToMove = False
				if phase == 'FLY':
					#gameState.blackToMove = False
					return minValue(gameState, alpha, beta, depth, 'MILL', True)
				else:
					return minValue(gameState, alpha, beta, depth, 'MILL')
		else:
			if dc.millHasBeenMadeInLastTurn(gameState, globalVar.variable1):
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
	"""Determine the AI's next move.

    :param gameState: The current game state.
    :param mill: Indicates if the AI is making a mill.
    :return: The best move for the AI.
    """
	globalVar.startTime = time()
	depth = 4

	if dc.numberOfPlayerPieces(gameState, globalVar.variable1) + globalVar.blackRemoved == 9:
		globalVar.PHASE = 'MOVE'
	else:
		globalVar.PHASE = 'INIT'

	if dc.numberOfPlayerPieces(gameState, globalVar.variable1) == 3 and globalVar.PHASE != 'INIT':
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
	"""Perform the AI's next move and update the game state.

    :param gameState: The current game state.
    :param mill: Indicates if the AI is making a mill.
    """
	move = aiNextMove(gameState, mill)
	old_state_table = deepcopy(gameState.board)
	if mill:
		globalVar.TABLE[move[0]] = globalVar.emptyField[move[0]]
		pp.print_table(gameState.board)
		print(Back.RED+"The AI just made the MILL and dc. removed your piece from {}. field.".format(move[0]))
		globalVar.whiteRemoved += 1
	elif globalVar.PHASE == 'INIT':
		globalVar.TABLE[move[0]] = globalVar.variable1
		pp.print_table(gameState.board)
		print(Back.YELLOW+"The AI has placed piece at {}. field.".format(move[0]))
	elif globalVar.PHASE == 'MOVE' or globalVar.PHASE == 'FLY':
		globalVar.TABLE[move[1]] = globalVar.variable1
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
		# y = random.randint(1,2)

		# if y ==1:
		# 	globalVar.variable1 = 'B'
		# 	globalVar.variable2 = 'W'
		# else:
		# 	globalVar.variable1 = 'W'
		# 	globalVar.variable2 = 'B'

		x=1
		if x == 2:
			inp = "y"
			globalVar.variable1 = 'W'
			globalVar.variable2 = 'B'
		else:
			inp = "n"
			globalVar.variable1 = 'B'
			globalVar.variable2 = 'W'
		# inp = "n"
		if inp == 'yes' or inp == 'y':
			gameState = State(globalVar.TABLE, False,[])
			break
		if inp == 'no' or inp == 'n':
			gameState = State(globalVar.TABLE, True, [])
			break
	play(gameState)
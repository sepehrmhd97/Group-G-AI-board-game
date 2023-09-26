import global_config as g
import pretty_print as pp
from state import State
# from playsound import playsound
import heuristic_state_functions as h
import sys
import human_play
import ai_play
import random





def play(state):
	check_if_over(state)
	check_counter_fly_plays(state)
	print('Moves remaining',300 - g.MOVESALLOWED)
	g.MOVESALLOWED+=1
	

	millIsMade = False
	if state.parent is not None:
		if state.blackToMove:
			if h.millHasBeenMadeInLastTurn(state, 'W'):
				millIsMade = True
				state.blackToMove = False
				human_play.human_play(state, True)
		else:
			if h.millHasBeenMadeInLastTurn(state, 'B'):
				millIsMade = True
				state.blackToMove = True
				ai_play.AI_play(state, True)
	if not millIsMade:
		if state.blackToMove:
			ai_play.AI_play(state, False)
		else:
			human_play.human_play(state, False)


def check_if_over(state):

	if(g.MOVESALLOWED >= 300):
		print("DRAW , number of moves has exceeded 300")
		sys.exit()
	
	# print("pieces taken" , state())
	# print("Number of white pieces to be placed",9-h.getNumberOfPlayerPieces(state,"B"))
	# print("Number of black pieces to be placed",9-h.getNumberOfPlayerPieces(state,"W"))

	print("Empty positions" ,  h.getAllEmptyPositionsOnBoard(state))
		



	if g.PHASE != 'INIT':
		if h.allPlayerPiecesClosed(state,'B') or h.getNumberOfPlayerPieces(state,'B') < 3:
			print('=========================CONGRATULATIONS, YOU WIN!=========================')
			# playsound(g.YOUWINSOUND)
			sys.exit()
		if h.allPlayerPiecesClosed(state, 'W') or h.getNumberOfPlayerPieces(state, 'W') < 3:
			print('===========================YOU LOSE!==========================')
			# playsound(g.YOULOSESOUND)
			sys.exit()

def check_counter_fly_plays(state):
	if g.PHASE != 'INIT':
		if h.getNumberOfPlayerPieces(state,'B') == 3 and h.getNumberOfPlayerPieces(state,'W') == 3:
			g.COUNTPLAYSFLY += 1
		if g.COUNTPLAYSFLY == 20:
			print('==================DRAWN==================')
			sys.exit()

if __name__ == '__main__':
	pp.welcome_prompt()
	print("PLease select difficulty")
	print("1. Easy    2. Medium    3. Hard")
	ch = int(input())
	if(ch == 1):
		g.TIMEALLOWED = 1
	elif(ch ==2):
		g.TIMEALLOWED = 3
	elif(ch==3):
		g.TIMEALLOWED = 6
	else:
		print("invalid input")
		exit()
	while True:
		# random 
		x = random.randint(1,2)
		# inp = input("Do you want to play first? (yes/no) >> ")

		if x == 1:
			inp = "y"
		else:
			inp = "n"
		if inp == 'yes' or inp == 'y':
			state = State(g.TABLE, False,[])
			break
		if inp == 'no' or inp == 'n':
			state = State(g.TABLE, True, [])
			break
	play(state)


from copy import deepcopy
import decisionCoeff as dc
import globalVariables as globalVar
import pretty_print as pp
from gameState import State
import game
import os
import sys
from colorama import Fore, Back, Style


def human_play_mill(gameState):
	old_state_board = deepcopy(gameState.board)
	print()
	pp.print_table(gameState.board)

	br = 0
	possibilities = []
	for i in range(24):
		if not dc.pieceInMill(gameState, i):
			if gameState.board[i] == 'B':
				possibilities.append(i)
				br += 1
	if br == 0:
		for i in range(24):
			if gameState.board[i] == 'B':
				possibilities.append(i)

	while True:
		place = input(Back.GREEN + "Mill created , type opponent piece you wish to remove from >> ")
		try:
			place = int(place)
		except:
			continue
		if place not in possibilities:
			print(Back.MAGENTA +"Invalid input can not remove")
		else:
			break

	globalVar.TABLE[place] = globalVar.emptyField[place]
	globalVar.blackRemoved += 1
	gameState.board = old_state_board
	new_state = State(globalVar.TABLE, True, [place], gameState)
	game.play(new_state)


def human_play_init(gameState):
	old_state_board = deepcopy(gameState.board)
	possibilities = []
	for i in range(24):
		if gameState.board[i] in globalVar.emptyField.values():
			possibilities.append(i)
	

	while True:
		print("PHASE 1")
		# print(Fore.YELLOW+"ALL POSITIONS" , dc.getAllEmptyPositionsOnBoard)
		print("To exit type 'exit' / to restart type 'restart'")
		print(Back.BLUE +"1 Type where do you wish to place a piece")
		print(Back.BLACK)
		place = input()
		if(place == 'exit'):
			print("Game exited")
			sys.exit()
		elif(place == 'restart'):
			os.system('python3 "/home/aravind/Desktop/MSCSY2P1/nine-mens-morris-python-game/src/game.py"')
	
		
		try:
			place = int(place)
		except:
			continue
		if place not in possibilities:
			print(Back.MAGENTA +"Invalid input can not place here")
		else:
			break

	globalVar.TABLE[place] = 'W'
	gameState.board = old_state_board
	new_state = State(globalVar.TABLE, True, [place], gameState)
	game.play(new_state)


def human_play_move(gameState):
	old_state_board = deepcopy(gameState.board)
	possibilities1 = []
	for i in range(24):
		if gameState.board[i] == 'W':
			possibilities1.append(i)

	while True:
		print("PHASE 2")
		first = input("Type the peice you wish to move from >> ")
		try:
			first = int(first)
		except:
			continue
		if first not in possibilities1:
			print(Back.MAGENTA +"Invalid input can not move from here")
		else:
			br = 0
			for index in globalVar.validAdjacent[first]:
				if gameState.board[index] in globalVar.emptyField.values():
					br = 1
					break
			if br == 1:
				break
			print("No adjavenct fields available.")



	possibilities2 = []
	for index in globalVar.validAdjacent[first]:
		if gameState.board[index] in globalVar.emptyField.values():
			possibilities2.append(index)
	print(Back.CYAN + Fore.BLACK + "All adjacent places" , possibilities2)
	while True:
		second = input("Where do you want to place theis piece >> ")
		try:
			second = int(second)
		except:
			continue
		if second not in possibilities2:
			print("Invald input , field not adjacent or is taken")
		else:
			break

	globalVar.TABLE[second] = 'W'
	globalVar.TABLE[first] = globalVar.emptyField[first]
	gameState.board = old_state_board
	new_state = State(globalVar.TABLE, True, [first, second], gameState)
	game.play(new_state)


def human_play_fly(gameState):
	old_state_board = deepcopy(gameState.board)
	possibilities1 = []
	possibilities_free = []
	for i in range(24):
		if gameState.board[i] == 'W':
			possibilities1.append(i)
		if gameState.board[i] in globalVar.emptyField.values():
			possibilities_free.append(i)

	while True:
		print("PHASE 3")
		first = input("Phase 3(FLY) : Type the field from which you want to move the piece ")
		try:
			first = int(first)
		except:
			continue
		if first not in possibilities1:
			print(Back.MAGENTA +"Invalid input can't move the piece from this field.")
		else:
			break

	while True:
		second = input("Tyype ANY free field on the table on which you want to move the piece >> ")
		print(Back.CYAN + Fore.BLACK + "All free places" , possibilities_free)
		
		try:
			second = int(second)
		except:
			continue
		if second not in possibilities_free:
			print(Back.MAGENTA +"Invalid Input this field is not free.")
		else:
			break

	globalVar.TABLE[second] = 'W'
	globalVar.TABLE[first] = globalVar.emptyField[first]
	gameState.board = old_state_board
	new_state = State(globalVar.TABLE, True, [first, second], gameState)
	game.play(new_state)


def userGameMoves(gameState, mill):
	if dc.getNumberOfPlayerPieces(gameState, 'W') + globalVar.whiteRemoved == 9:
		globalVar.PHASE = 'MOVE'
	else:
		globalVar.PHASE = 'INIT'

	if dc.getNumberOfPlayerPieces(gameState, 'W') == 3 and globalVar.PHASE != 'INIT':
		globalVar.PHASE = 'FLY'

	if mill:
		human_play_mill(gameState)
	elif globalVar.PHASE == 'INIT':
		human_play_init(gameState)
	elif globalVar.PHASE == 'MOVE':
		human_play_move(gameState)
	elif globalVar.PHASE == 'FLY':
		human_play_fly(gameState)

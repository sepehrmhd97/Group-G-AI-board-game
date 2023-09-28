import globalVariables as globalVar


def numberOf2Config(gameState, player):
	number = 0
	for trio in globalVar.validMills:
		if gameState.board[trio[0]] == gameState.board[trio[1]] == player and gameState.board[trio[2]] in globalVar.emptyField.values():
			number += 1
		if gameState.board[trio[1]] == gameState.board[trio[2]] == player and gameState.board[trio[0]] in globalVar.emptyField.values():
			number += 1
		if gameState.board[trio[0]] == gameState.board[trio[2]] == player and gameState.board[trio[1]] in globalVar.emptyField.values():
			number += 1
	return number


def numberOf3Config(gameState, player):
	number = 0
	for var in globalVar.Trees:
		if gameState.board[var[0]] == gameState.board[var[1]] == gameState.board[var[2]] == player and gameState.board[
			var[3]] in globalVar.emptyField.values() and gameState.board[var[4]] in globalVar.emptyField.values():
			number += 1
	return number


def numberOfPlayerDoubleMills(gameState, player):
	number = 0
	for var in globalVar.validDoubleMills:
		if gameState.board[var[0]] == gameState.board[var[1]] == gameState.board[var[2]] == gameState.board[var[3]] == gameState.board[
			var[4]] == player:
			number += 1
	return number


def numberOfPlayerMills(gameState, player):
	numberOfMills = 0
	for trio in globalVar.validMills:
		if gameState.board[trio[0]] == gameState.board[trio[1]] == gameState.board[trio[2]] == player:
			numberOfMills += 1
	return numberOfMills


def numberOfPlayerPieces(gameState, player):
	number = 0
	for position in gameState.board:
		if position == player:
			number += 1
	return number


def numberOfPlayerClosedPeaces(gameState, player):
	number = 0
	for key, value in globalVar.validAdjacent.items():
		temp = 0
		if gameState.board[key] == player:
			for adj in value:
				if gameState.board[adj] in globalVar.emptyField.values():
					temp = 1
					break
			if temp == 0: number += 1
	return number


def allPlayerPiecesClosed(gameState, player):
	for key, value in globalVar.validAdjacent.items():
		if gameState.board[key] == player:
			for adj in value:
				if gameState.board[adj] in globalVar.emptyField.values():
					return False
	return True


def differenceIn3PeacesConfig(gameState):
	black = numberOf3Config(gameState, globalVar.variable1)
	white = numberOf3Config(gameState, globalVar.variable2)
	return black - white


def differenceInDoubleMorrises(gameState):
	black = numberOfPlayerDoubleMills(gameState, globalVar.variable1)
	white = numberOfPlayerDoubleMills(gameState, globalVar.variable2)
	return black - white


def differenceIn2PeacesConfig(gameState):
	black = numberOf2Config(gameState, globalVar.variable1)
	white = numberOf2Config(gameState, globalVar.variable2)
	return black - white


def differenceInClosedPeaces(gameState):
	black = numberOfPlayerClosedPeaces(gameState, globalVar.variable1)
	white = numberOfPlayerClosedPeaces(gameState, globalVar.variable2)
	return black - white


def differceInNumberOfMills(gameState):
	black = numberOfPlayerMills(gameState, globalVar.variable1)
	white = numberOfPlayerMills(gameState, globalVar.variable2)
	return black - white


def differceInPieces(gameState):
	black = numberOfPlayerPieces(gameState, globalVar.variable1)
	white = numberOfPlayerPieces(gameState, globalVar.variable2)
	return black - white


def winningConfiguration(gameState):
	if allPlayerPiecesClosed(gameState, globalVar.variable2) or numberOfPlayerPieces(gameState, globalVar.variable2) < 3:
		return 1
	if allPlayerPiecesClosed(gameState, globalVar.variable1) or numberOfPlayerPieces(gameState, globalVar.variable1) < 3:
		return -1
	return 0


def getListOfAllPlayerMills(gameState, player):
	list = []
	for trio in globalVar.validMills:
		if gameState.board[trio[0]] == gameState.board[trio[1]] == gameState.board[trio[2]] == player:
			list.append(trio)
	return list


def millHasBeenMadeInLastTurn(gameState, player):
	parent_mills = getListOfAllPlayerMills(gameState.parent, player)
	current_mills = getListOfAllPlayerMills(gameState, player)
	for mill in current_mills:
		if mill not in parent_mills:
			return True
	return False


def closedMorris(gameState):
	if gameState.parent is None:
		return 0
	if gameState.blackToMove:
		if millHasBeenMadeInLastTurn(gameState, globalVar.variable2):
			return -1
	else:
		if millHasBeenMadeInLastTurn(gameState, globalVar.variable1):
			return 1
	return 0


def pieceInMill(gameState, index_peace):
	for par in globalVar.millPiece[index_peace]:
		if gameState.board[par[0]] == gameState.board[par[1]] == gameState.board[index_peace]:
			return True
	return False


def getAllPositionsOfPlayer(gameState, player):
	positions = []
	for i in range(24):
		if gameState.board[i] == player:
			positions.append(i)
	return positions


def getAllEmptyPositionsOnBoard(gameState):
	pos = []
	for i in range(24):
		if gameState.board[i] in globalVar.emptyField.values():
			pos.append(i)
	return pos



"""
Final heuristics, you can change coefficients if you see that
computer is playing better with those new coefficients
"""

def evalute(gameState, phase):
	result = 0
	if phase == 'INIT':
		result =18 * closedMorris(gameState) + \
				26 * differceInNumberOfMills(gameState) + \
				1 * differenceInClosedPeaces(gameState) + \
				9 * differceInPieces(gameState) + \
				10 * differenceIn2PeacesConfig(gameState) + \
				7 * differenceIn3PeacesConfig(gameState)

	elif phase == 'MOVE':
		result =14 * closedMorris(gameState) + \
				43 * differceInNumberOfMills(gameState) + \
				10 * differenceInClosedPeaces(gameState) + \
				11 * differceInPieces(gameState) + \
				8 * differenceInDoubleMorrises(gameState) + \
				1086 * winningConfiguration(gameState)

	elif phase == 'FLY':
		result =16 * differenceIn2PeacesConfig(gameState) + \
				10 * differenceIn3PeacesConfig(gameState) +\
				1 * closedMorris(gameState) + \
				1190 * winningConfiguration(gameState)
	return result



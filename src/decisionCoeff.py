import globalVariables as globalVar


def numberOf2Config(gameState, player):
	"""Calculate the number of possible 2-piece configurations for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate the configurations.
    :return: The number of 2-piece configurations.
	"""
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
	"""Calculate the number of possible 3-piece configurations for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate the configurations.
    :return: The number of 3-piece configurations.
    """
	number = 0
	for var in globalVar.Trees:
		if gameState.board[var[0]] == gameState.board[var[1]] == gameState.board[var[2]] == player and gameState.board[
			var[3]] in globalVar.emptyField.values() and gameState.board[var[4]] in globalVar.emptyField.values():
			number += 1
	return number


def numberOfPlayerDoubleMills(gameState, player):
	"""Calculate the number of double mills (two mills that share a piece) for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate double mills.
    :return: The number of double mills.
    """
	number = 0
	for var in globalVar.validDoubleMills:
		if gameState.board[var[0]] == gameState.board[var[1]] == gameState.board[var[2]] == gameState.board[var[3]] == gameState.board[
			var[4]] == player:
			number += 1
	return number


def numberOfPlayerMills(gameState, player):
	"""Calculate the number of mills (3 pieces in a row) for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate mills.
    :return: The number of mills.
    """
	numberOfMills = 0
	for trio in globalVar.validMills:
		if gameState.board[trio[0]] == gameState.board[trio[1]] == gameState.board[trio[2]] == player:
			numberOfMills += 1
	return numberOfMills


def numberOfPlayerPieces(gameState, player):
	"""Calculate the number of closed pieces (pieces surrounded by the opponent's pieces) for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate closed pieces.
    :return: The number of closed pieces.
    """
	number = 0
	for position in gameState.board:
		if position == player:
			number += 1
	return number


def numberOfPlayerClosedPeaces(gameState, player):
	"""Calculate the number of closed pieces (pieces surrounded by the opponent's pieces) for a player.

    :param gameState: The current game state.
    :param player: The player for whom to calculate closed pieces.
    :return: The number of closed pieces.
    """
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
	"""Check if all of a player's pieces are closed (surrounded) by the opponent's pieces.

    :param gameState: The current game state.
    :param player: The player to check.
    :return: True if all pieces are closed, False otherwise.
    """
	for key, value in globalVar.validAdjacent.items():
		if gameState.board[key] == player:
			for adj in value:
				if gameState.board[adj] in globalVar.emptyField.values():
					return False
	return True


def differenceIn3PeacesConfig(gameState):
	"""Calculate the difference in the number of 3-piece configurations between the two players.

    :param gameState: The current game state.
    :return: The difference in 3-piece configurations.
    """
	black = numberOf3Config(gameState, globalVar.variable1)
	white = numberOf3Config(gameState, globalVar.variable2)
	return black - white


def differenceInDoubleMorrises(gameState):
	"""Calculate the difference in the number of double mills between the two players.

    :param gameState: The current game state.
    :return: The difference in double mills.
    """
	black = numberOfPlayerDoubleMills(gameState, globalVar.variable1)
	white = numberOfPlayerDoubleMills(gameState, globalVar.variable2)
	return black - white


def differenceIn2PeacesConfig(gameState):
	"""Calculate the difference in the number of 2-piece configurations between the two players.

    :param gameState: The current game state.
    :return: The difference in 2-piece configurations.
    """
	black = numberOf2Config(gameState, globalVar.variable1)
	white = numberOf2Config(gameState, globalVar.variable2)
	return black - white


def differenceInClosedPeaces(gameState):
	"""Calculate the difference in the number of closed pieces between the two players.

    :param gameState: The current game state.
    :return: The difference in closed pieces.
    """
	black = numberOfPlayerClosedPeaces(gameState, globalVar.variable1)
	white = numberOfPlayerClosedPeaces(gameState, globalVar.variable2)
	return black - white


def differceInNumberOfMills(gameState):
	"""Calculate the difference in the number of mills between the two players.

    :param gameState: The current game state.
    :return: The difference in mills.
    """
	black = numberOfPlayerMills(gameState, globalVar.variable1)
	white = numberOfPlayerMills(gameState, globalVar.variable2)
	return black - white


def differceInPieces(gameState):
	"""Calculate the difference in the total number of pieces between the two players.

    :param gameState: The current game state.
    :return: The difference in the number of pieces.
    """
	black = numberOfPlayerPieces(gameState, globalVar.variable1)
	white = numberOfPlayerPieces(gameState, globalVar.variable2)
	return black - white


def winningConfiguration(gameState):
	"""Determine the winning configuration of the game.

    :param gameState: The current game state.
    :return: 1 if player 2 has lost, -1 if player 1 has lost, or 0 otherwise.
    """
	if allPlayerPiecesClosed(gameState, globalVar.variable2) or numberOfPlayerPieces(gameState, globalVar.variable2) < 3:
		return 1
	if allPlayerPiecesClosed(gameState, globalVar.variable1) or numberOfPlayerPieces(gameState, globalVar.variable1) < 3:
		return -1
	return 0


def getListOfAllPlayerMills(gameState, player):
	"""Get a list of all mills formed by a player.

    :param gameState: The current game state.
    :param player: The player for whom to retrieve mills.
    :return: A list of mill configurations.
    """
	list = []
	for trio in globalVar.validMills:
		if gameState.board[trio[0]] == gameState.board[trio[1]] == gameState.board[trio[2]] == player:
			list.append(trio)
	return list


def millHasBeenMadeInLastTurn(gameState, player):
	"""Check if a mill has been formed by a player in the last turn.

    :param gameState: The current game state.
    :param player: The player to check for mill formation.
    :return: True if a mill was formed in the last turn, False otherwise.
    """
	parent_mills = getListOfAllPlayerMills(gameState.parent, player)
	current_mills = getListOfAllPlayerMills(gameState, player)
	for mill in current_mills:
		if mill not in parent_mills:
			return True
	return False


def closedMorris(gameState):
	"""Determine if a closed mill has been formed in the last turn.

    :param gameState: The current game state.
    :return: -1 if player 2 formed a closed mill, 1 if player 1 formed a closed mill, or 0 otherwise.
    """
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
	 """Check if a piece is part of a mill.

    :param gameState: The current game state.
    :param index_peace: The index of the piece to check.
    :return: True if the piece is part of a mill, False otherwise.
    """
	for par in globalVar.millPiece[index_peace]:
		if gameState.board[par[0]] == gameState.board[par[1]] == gameState.board[index_peace]:
			return True
	return False


def getAllPositionsOfPlayer(gameState, player):
	"""Get all positions on the board occupied by a player's pieces.

    :param gameState: The current game state.
    :param player: The player for whom to retrieve positions.
    :return: A list of positions occupied by the player's pieces.
    """
	positions = []
	for i in range(24):
		if gameState.board[i] == player:
			positions.append(i)
	return positions


def getAllEmptyPositionsOnBoard(gameState):
	"""Get all empty positions on the game board.

    :param gameState: The current game state.
    :return: A list of empty positions on the board.
    """
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
	"""Calculate the heuristic evaluation score for the current game state.

    :param gameState: The current game state.
    :param phase: The phase of the game ('INIT', 'MOVE', or 'FLY').
    :return: The heuristic evaluation score for the game state.
    """
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



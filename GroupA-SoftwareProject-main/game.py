import backend
import gameBoard
#import menu
import player
import playinput
import random
#import tkinter as tk
#from tkinter import ttk
#from tkinter import *




def random_start(player1, player2):
    res = random.randint(0,1)
    if res == 0:
        player1.current_turn = True
    else:
        player2.current_turn = True


def gameRunner():
    game_running = True

    player1_name = playinput.decide_name('player1')         # This asks for what the player want to be named
    player2_name = playinput.decide_name('player2')
    
    player1 = player.Player(player1_name, '1')              # Creates the player objects
    player2 = player.Player(player2_name, '2')

    random_start(player1, player2)
    board = gameBoard.GameBoard()

    while game_running:
        # TODO: Add the round counter
        #board.printBoard()
        #current_players_turn = backend.check_turn(player1, player2)

        
        while player1.placed_pieces < 12 or player2.placed_pieces < 12:
            # Phase 1
            # Allowed to place freely
            board.printBoard()
            current_players_turn = backend.check_turn(player1, player2)                                 # Just to print whos players turn it is
            
            where_to_place = playinput.choose_slot()                                                    # Player decides where they want to place the piece freely
            valid_or_not = board.PutPieceToPosition(where_to_place, current_players_turn)               # TODO: Check that the position is free
            current_players_turn.place_piece()
            
            if backend.check_for_mills(current_players_turn):                                           # Has the player made a new mill?
                board.printBoard()
                remove_from = input('Which place do you want to remove from?')                          # Player inputs the slot they want to remove a piece from
                board.RemovePieceFromBoard(remove_from, current_players_turn)                           # Piece is removed from the board
                current_players_turn = backend.change_turn(player1, player2)                            # Change to the other players turn to easier remove the right piece
                current_players_turn.remove_placed_piece(remove_from)                                   # Remove piece from player array
            else:
                current_players_turn = backend.change_turn(player1, player2)
                

        while player1.pieces_remaining > 3 or player2.pieces_remaining > 3:
            # Phase 2
            # Regulations on how to move
            board.printBoard()
            current_players_turn = backend.check_turn(player1, player2) 
            move_from = input('Where is the piece you want to move?')
            move_to = input('Where do you want to place the piece?')
            current_player = backend.check_turn(player1, player2)
            current_players_turn = backend.change_turn(player1, player2)
            #TODO: CALL PUTPIECE BOARD FUNC
            board.movePieceOnBoard(move_from,move_to,current_player) 
            backend.move_a_piece(current_player, current_players_turn, move_from, move_to)
            
            if backend.check_for_mills(current_player):                            # Has the player made a new mill?
                #TODO: MAke the changes appear on board too
                board.printBoard()
                remove_from = input('Which place do you want to remove from?')     # Player inputs the slot they want to remove a piece from
                board.RemovePieceFromBoard(remove_from, current_player)            # Piece is removed from the board
                current_players_turn.remove_placed_piece(remove_from)              # Remove piece from player array

        phase3 = True
        while phase3:
            board.printBoard()
            current_players_turn = backend.check_turn(player1, player2) 
            if current_players_turn.pieces_remaining == 3:
                print(f"{current_players_turn.name} you have flying privileges")
                move_from = input('Where is the piece you want to move?')
                move_to = input('Where do you want to place the piece?')
                current_player = backend.check_turn(player1, player2)
                current_players_turn = backend.change_turn(player1, player2)
                board.RemovePieceFromBoard(remove_from,current_player,True)
                board.PutPieceToPosition(move_to,current_player)
                backend.move_a_piece(current_player, current_players_turn, move_from, move_to)
                
                if backend.check_for_mills(current_player):                            # Has the player made a new mill?
                    #TODO: MAke the changes appear on board too
                    board.printBoard()
                    remove_from = input('Which place do you want to remove from?')     # Player inputs the slot they want to remove a piece from
                    board.RemovePieceFromBoard(remove_from, current_player)            # Piece is removed from the board
                    current_players_turn.remove_placed_piece(remove_from)              # Remove piece from player array
            else:
                current_players_turn = backend.check_turn(player1, player2) 
                move_from = input('Where is the piece you want to move?')
                move_to = input('Where do you want to place the piece?')
                current_player = backend.check_turn(player1, player2)
                current_players_turn = backend.change_turn(player1, player2)
                #TODO: CALL PUTPIECE BOARD FUNC
                board.movePieceOnBoard(move_from,move_to,current_player) 
                backend.move_a_piece(current_player, current_players_turn, move_from, move_to)
                
                if backend.check_for_mills(current_player):                            # Has the player made a new mill?
                    #TODO: MAke the changes appear on board too
                    board.printBoard()
                    remove_from = input('Which place do you want to remove from?')     # Player inputs the slot they want to remove a piece from
                    board.RemovePieceFromBoard(remove_from, current_player)            # Piece is removed from the board
                    current_players_turn.remove_placed_piece(remove_from)              # Remove piece from player array


            if player1.pieces_remaining < 3 or player2.pieces_remaining <3:
                phase3 = False
         
        backend.end_game(player1, player2)
        game_running = False
    return True

gameRunner()
# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe
Author: Shadman Ahmed

"""

from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
        
def player_input():
    
    marker = ' '

    #Ask Player 1 to choose their marker
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        
    #Assign Markers Upon Input
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else: player2 = 'X'
        
    return(player1,player2)
    
def marker_assignment(board, marker, position):
    board[position] = marker
       
def check_win(board, mark):   
    
    #ALL ROW CHECKER
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    #ALL COLUMN CHECKER
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    #DIAGONALS CHECKER
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def player_picker():
    
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_checker(board,position):
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_checker(board,i):
            return False
    return True

def player_choice(board,turn):
    
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_checker(board,position):
        position = int(input('{}, choose a position on the numpad: '.format(turn)))
    return position


def replay():
    
    choice = input('Play again? Type either "Y" to accept or "N" to decline: ')
    return choice == 'Y'

#MAIN WHILE LOOP
    
print('Welcome to Tic-Tac-Toe')

while True:
    
    ##SETUP
    the_board = [' ']*10
    player1_marker,player2_marker =player_input()
    turn = player_picker()
    print(turn + ' will go first!')
    play_game = input('Ready to play? Type either "Y" to accept or "N" to decline: ')
    if play_game =='Y':
        game_on = True
    elif play_game =='N':
        game_on = False
    
    #Gameplay     
    while game_on:
        
        if turn =='Player 1':
            #Display the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board,turn)
            #Place Marker at the position
            marker_assignment(the_board,player1_marker,position)
            #Check win
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
            #Display the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board,turn)
            #Place Marker at the position
            marker_assignment(the_board,player2_marker,position)
            #Check win
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

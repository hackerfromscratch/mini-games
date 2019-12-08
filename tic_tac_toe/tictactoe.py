#!/usr/bin/env python3.7
import game_def
from game_def import *

game = ''  # a var needed to know what game is played
game_init = True  # the whole game init
game_mode_check = True # the actual game init it doesnt ask for the game mode it just play it !
answer_to_continue_game = 'f'  # a var to know if the player want to play again

print('-----------------------------------------')
print('---------welcome to Tic Tac Toe----------')
print('-----------------------------------------')
print('---------------important !---------------')
print('-----------------------------------------')
print(">>>>>> play with your num pad so you don't have to memorize the numbers for each case <<<<<<<<< ")

while game_init is True:
    game_def.board = ['None', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # reset of the game board values
    game_def.played_move = []  # same deal here
    game_def.player1.win = False
    game_def.player2.win = False
    game_def.ai.win = False
    while game != '1' or game != '2':
        print('please select if you want to play a solo game or a 2 players game ( 1 or 2) ')
        game = input('> ')
        if game == '1':
            game_def.game_vs_ai()
            break
        elif game == '2':
            game_def.game_2_players()
            break
    while answer_to_continue_game != 'n' or answer_to_continue_game != 'y':
        print('do you want to play again ? (y/n)')
        answer_to_continue_game = input('> ')
        if answer_to_continue_game == 'y':
            game_init = True  # if yes we play another game
            break
        elif answer_to_continue_game == 'n':
            game_init = False  # if n that we break the loop and the game end
            break
print('good bye !')

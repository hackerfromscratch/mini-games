#!/usr/bin/env python3.7
from game_ai import *
import game_ai

# -------------------------------------------common vars-------------------------------------------------

board = ['None', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # first is none cause users count from 1 not from 0

# -------------------- this 2 lists down below are the possible combinations for wining
list1 = [(1, 1, 2), (1, 1, 4), (4, 4, 5), (7, 7, 8), (2, 2, 5), (3, 3, 6), (7, 7, 5), (9, 9, 5)]
list2 = [(2, 3, 3), (4, 7, 7), (5, 6, 6), (8, 9, 9), (5, 8, 8), (6, 9, 9), (5, 3, 3), (5, 1, 1)]

played_move = []
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # all possible moves
corners = [1, 3, 7, 9]  # corners numbers
next_move = 'f'  # the next move of the computer it's f by default to init the loop
game_run = True  # another init var

class Player:  # class for player so we don't have to create multiple players var

    def __init__(self, name, atr, win):
        self.atr = atr  # atr is the X or O in the game
        self.name = name
        self.win = win


player1 = Player('', 'X', False)
player2 = Player('', 'O', False)
ai = Player('computer', 'O', False)

# --------------------------------------------common functions------------------------------------------------


def print_board():
    global board
    print('-------------')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('-------------')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('-------------')
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('-------------')


def turn(player):  # function for a human player turn
    global played_move, player1, player2
    print(f'it is {player.name} turn ')
    print("what is your next move ? (1-9)")
    move = input('> ')
    move_check = isinstance(move, int)
    end_of_turn = False
    used_move = True

    while end_of_turn is False:

        try:  # --------------------we try to convert the variable to int to check if it's really a number
            move = int(move)
            move_check = isinstance(move, int)
            if 0 < move < 10:
                if move in played_move:
                    out_of_range = True
                else:
                    out_of_range = False
                    used_move = False
            else:
                out_of_range = True
        except ValueError:
            out_of_range = True
            pass

        if move_check is True and out_of_range is False and used_move is False:  # finally if it's a valid move we play it
            board[move] = player.atr
            played_move.append(move)
            end_of_turn = True
        elif move_check is False and out_of_range is True:  # if the user had entered a number already used or a character...
            print('miss click you must enter a number ! ')
            print("what is your next move ? (1-9)")
            move = input('> ')

        elif out_of_range:  # if move already played
            print("error you have to enter a number between 1 and 9 that you din not already use !")
            print("what is your next move ? (1-9)")
            move = input('> ')


def check_if_win(player):  # the function that check if a player know
    if board[1] == player.atr and board[2] == player.atr and board[3] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[4] == player.atr and board[5] == player.atr and board[6] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[7] == player.atr and board[8] == player.atr and board[9] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[1] == player.atr and board[4] == player.atr and board[7] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[3] == player.atr and board[6] == player.atr and board[9] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[2] == player.atr and board[5] == player.atr and board[8] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[7] == player.atr and board[5] == player.atr and board[3] == player.atr:
        player.win = True
        print(f"{player.name} has won !")

    elif board[9] == player.atr and board[5] == player.atr and board[1] == player.atr:
        player.win = True
        print(f"{player.name} has won !")


def game_vs_ai():  # functions that load the functions for a game between the computer and the user
    global player1
    print("Enter player 1 name :")
    player1.name = input('> ')
    print(f'welcome {player1.name}')

    counter = 1
    game_def.print_board()
    while counter < 10:
        n = counter % 2
        if n == 1:
            player = player1
            turn(player)
            print_board()
            check_if_win(player)
            if player.win is True:
                counter = 20
        else:
            player = ai
            print("it's computer turn !")
            game_ai.ai_turn()
            print_board()
            check_if_win(player)
            if player.win is True:
                counter = 20

        counter += 1

    if player1.win is False and ai.win is False:
        print("it's a tie !")


def game_2_players():  # function that load the functions for a game between 2 players
    # ----------------------------------------------getting players names
    print("Enter player 1 name :")
    player1.name = input('> ')
    print("Enter player 2 name :")
    player2.name = input('> ')

    print(f'welcome {player1.name} and {player2.name}')

    counter = 0
    print_board()
    while counter < 9:
        n = counter % 2
        if n == 0:
            player = player1
            turn(player)
            print_board()
            check_if_win(player)
            if player.win is True:
                counter = 20
        else:
            player = player2
            turn(player)
            print_board()
            check_if_win(player)
            if player.win is True:
                counter = 20
        counter += 1

    if player1.win is False and player2.win is False:
        print("it's a tie !")

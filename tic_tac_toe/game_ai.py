#!/usr/bin/env python3.7


import random
import game_def
from game_def import *
# -------------------- this 2 lists down below are the possible combinations for wining
list1 = [(1, 1, 2), (1, 1, 4), (4, 4, 5), (7, 7, 8), (2, 2, 5), (3, 3, 6), (7, 7, 5), (9, 9, 5)]
list2 = [(2, 3, 3), (4, 7, 7), (5, 6, 6), (8, 9, 9), (5, 8, 8), (6, 9, 9), (5, 3, 3), (5, 1, 1)]

temp_list = list(list1[0])  # important i don't remember what it does but do not delete it !

def wining_move():
    # so how this part work : instand of doing a lot of if and else i made 2 list with the 8 tuples that contain the
    # possibilities of wining if you remove the double in the first tuple of list1 and the first tuple of list2 it will
    # give you (1, 2, 3) so if you have 1 and 3 in the num pad you need the 2 to win we verify if we are in this
    # case than by deduction of the 3 possibilities from the already played move we got our wining move
    # it's verify 2 times in case we don't have 1 and 3 but 3 and 1 we just have to change the order
    global list1, list2, played_move, next_move
    stop = False
    next_move = 'f'
    counter_wining_move = 0
    while counter_wining_move < 8 and stop is False:
        temp_list = list1[counter_wining_move]
        temp_list2 = list2[counter_wining_move]
        for i in range(len(temp_list)):
            x = temp_list[i]
            z = temp_list2[i]

            if game_def.board[x] is game_def.ai.atr and game_def.board[z] is game_def.ai.atr:
                ai_wining_move = []
                ai_wining_move.extend((temp_list[i], temp_list2[i]))
                temp_list3 = temp_list + temp_list2
                solution = list(set(temp_list3) - set(ai_wining_move))
                solution = solution[0]
                if solution in game_def.played_move:
                    pass
                else:
                    next_move = solution
                    game_def.ai.win = True
                    stop = True
        counter_wining_move += 1
    return next_move


def block_player():
    # same deal for wining_move the only dif is that we check wining for opponent
    global list1, list2, next_move
    stop = False
    next_move = 'f'
    counter_block_move = 0
    while counter_block_move < 8 and stop is False:
        temp_list = list1[counter_block_move]
        temp_list2 = list2[counter_block_move]
        for i in range(len(temp_list)):
            x = temp_list[i]
            z = temp_list2[i]

            if game_def.board[x] is game_def.player1.atr and game_def.board[z] is game_def.player1.atr:
                ai_wining_move = []
                ai_wining_move.extend((temp_list[i], temp_list2[i]))
                temp_list3 = temp_list + temp_list2
                block_move = list(set(temp_list3) - set(ai_wining_move))
                block_move = block_move[0]
                if block_move in game_def.played_move:
                    pass
                else:
                    if game_def.board[block_move] is ' ':
                        next_move = block_move
                        stop = True
        counter_block_move += 1
    return next_move


def block_trick():  # if the player want to win by making triangle the ai play in the center to block it
    global next_move
    for i in game_def.corners:
        if game_def.board[i] is game_def.player1.atr:
            if game_def.board[5] is not game_def.ai.atr and game_def.board[5] is not game_def.player1.atr:
                next_move = 5
                break
    return next_move


def corner():  # to play in a random corner
    global played_move, next_move, corners, used_corners, free_corners
    next_move = 'f'
    used_corners = []
    for i in game_def.played_move:
        if i in game_def.corners:
            used_corners.append(i)
    free_corners = list(set(game_def.corners) - set(used_corners))
    temp_var = len(free_corners)
    if free_corners is []:
        next_move = 'f'
    else:
        next_move = random.randrange(temp_var)
        next_move = free_corners[next_move]
    return next_move


def ai_turn():  # the algo of the ai it's check case by order
    global next_move, played_move, corners, used_corners, free_corners
    run = True
    if run:  # first if it can play a wining move
        wining_move()
        if next_move is 'f':
            pass
        else:
            game_def.board[next_move] = game_def.ai.atr
            run = False
    if run:  # than if it can block the player from making a wining move
        block_player()
        if next_move is 'f':
            pass
        else:
            game_def.board[next_move] = game_def.ai.atr
            game_def.played_move.append(game_def.board[next_move])
            run = False
    if run and game_def.board[5] is ' ':  # block the triangle trick if the center is free
        block_trick()
        if next_move is 'f':
            pass
        else:
            game_def.board[next_move] = game_def.ai.atr
            game_def.played_move.append(game_def.board[next_move])
            run = False
    if run: # than if it play in corner
        corner()
        if next_move is 'f':
            pass
        else:
            game_def.board[next_move] = game_def.ai.atr
            game_def.played_move.append(game_def.board[next_move])
            run = False

    if run:  # if no one it's play a random move from the availed ones
        allowed_move = list(set(moves) - set(played_move))
        temp_var = random.randrange(len(allowed_move))
        next_move = allowed_move[temp_var]
        game_def.board[next_move] = game_def.ai.atr
        game_def.played_move.append(game_def.board[next_move])


#!/usr/bin/python3.6
import re
import getch
import subprocess

# start var 
door = 24

with open('facile.txt', 'r') as file:
    game_map = file.read()


def print_map():
    subprocess.call('clear')
    print(game_map)

def find_x():
    global position
    result = re.search(r'X', game_map, flags=0)
    s1 = result.span(0)
    position = s1[0]


def welcome_msg():
    subprocess.call('clear')
    print('-------------------------------------------')
    print('------------Welcome to Roboc ! ------------')
    print('-------------------------------------------')
    print('rules :')
    print("to move forward press    : 'z' ")
    print("to move backward press   : 's' ")
    print("to move right press      : 'd' ")
    print("to move left press       : 'q' ")
    print("to quit the game press   : 'p' ")
    print("to start a new game press enter")


def make_move(direction):
    global game_map, position
    if direction == 'q':
        game_map = game_map[:position] + ' ' + game_map[position +1:]
        game_map = game_map[:position -1] + 'X' + game_map[position:]
    elif direction == 'd' :
        game_map = game_map[:position] + ' ' + game_map[position +1:]
        game_map = game_map[:position + 1] + 'X' + game_map[position + 2:]
    elif direction == 'z' :
        game_map = game_map[:position] + ' ' + game_map[position +1:]
        game_map = game_map[:position -11] + 'X' + game_map[position - 10:]
    elif direction == 's' :
        game_map = game_map[:position] + ' ' + game_map[position +1:]
        game_map = game_map[:position + 11] + 'X' + game_map[position + 12:]


def check_door():
    global game_map, door
    if game_map[door] != 'X' and game_map[door] != '.' :
        game_map = game_map[:door] + '.' + game_map[door +1:]

    

welcome_msg()
start = getch.getch()
while start != '':
    welcome_msg()
    start = input()
        

while True:
    find_x()
    print_map()
    print('move > ')
    move = getch.getch()
    check_door()

    if move == 'q':
        new_position = position - 1
        if game_map[new_position] == 'O':
            pass
        elif game_map[new_position] == '.':
            door = new_position
            make_move('q')
        elif game_map[new_position] == 'U' :
            make_move('q')
            print_map()
            print('you won !')
            break
        else:
            make_move('q')
            
    elif move == 'd' :
        new_position = position + 1
        if game_map[new_position] == 'O':
            pass
        elif game_map[new_position] == '.':
            door = new_position
            make_move('d')
        elif game_map[new_position] == 'U' :
            make_move('d')
            print_map()
            print('you won !')
            break
        else:
            make_move('d')
    elif move == 's' :
        new_position = position + 11
        if game_map[new_position] == 'O':
            pass
        elif game_map[new_position] == '.':
           door = new_position
           make_move('s')
        elif game_map[new_position] == 'U' :
            make_move('s')
            print_map()
            print('you won !')
            break
        else:
            make_move('s')
    elif move == 'z' :
        new_position = position - 11
        if game_map[new_position] == 'O':
            pass
        elif game_map[new_position] == '.':
            door = new_position
            make_move('z')
        elif game_map[new_position] == 'U' :
            make_move('z')
            print_map
            print('you won !')
            break
        else:
            make_move('z')
    elif move == 'p' :
        print('good bye !')
        break

    check_door()
#!/usr/bin/python3.6
import re
import getch
import subprocess

with open('facile.txt', 'r') as file:
    game_map = file.read()

print(len(game_map))

print(game_map[0:1])
print(game_map[119:120])

print(game_map[9:10])

line5 = game_map.count('\n')
print(line5)
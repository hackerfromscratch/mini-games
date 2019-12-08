#!/usr/bin/python3.7
import os
import pickle
import random
from game_var import *


def score_load():
    global score, player, test
    player = input('name > ')      #getting the name
    check_save_file = os.stat('score.pickle').st_size == 0 #check if the score is empty
    print("----------------------------------------")
    if check_save_file == True:  #if file empty we just set the score var for now and save later
        score = {}
        score[player] = 0
        print('welcome {} your score is 0'.format(player))
    else:

        with open ('score.pickle', 'rb') as file:  #score file exist
            file = pickle.Unpickler(file)
            score = file.load()
            if player in score.keys():  # player exist in the score save file
                print('welcome ' + player + ' tour score is '+ str(score[player]))
            else:                       # player does not exist in the score save file
                score[player] = 0
                print('welcome ' + player + ' tour score is ' + str(score[player]))


#function to get the level of the game
def level_c():
    global level, level_innit
    level_innit = True
    level =int(5)
    while level_innit:
        try:
            level = int(level)
            while int(level) <= 0 or int(level) >= 4:
                print("choose between 1 and 3")
                print('1) easy')
                print('2) normal')
                print('3) hard')
                level = input('> ')

        except ValueError:
            print("error this is not a number !")
            level = 5

            continue

        level_innit = False
        break

def pick_word():

    global word_to_guess, word_len, user_word, level , dico_easy, dico_normal, dico_hard, dico
    i = random.randrange(0,4)
    if int(level) == 1:
        dico = dico_easy
    elif int(level) == 2:
        dico = dico_normal
    else:
        dico = dico_hard

    word_to_guess = ''.join(dico[i])
    word_len = int(len(word_to_guess))
    user_word = word_len*"*"
    user_word = list(user_word)

def turn():
    global win, user_word, check_word
    index = int(word_len)
    user_char = input("character : ")
    user_char_len = len(user_char)
    while user_char_len > 1:
        print("you can only enter one char try again !")
        user_char = input("character : ")
        user_char_len = len(user_char)

    for x in range(index):
        temp_var = word_to_guess[x]  # i used a temp var cause when i compare with the_word[x] it give an error
        check_word = list(word_to_guess)
        if user_char == check_word[x]:
            user_word[x] = user_char
    print("----------------------------------------")
    print(user_word)
    print("----------------------------------------")

#a simple def to save the score in the score.pickle file chnage in the score var are made outside of this function as playing
def score_save():
    with open('score.pickle', 'wb') as file:
        file = pickle.Pickler(file)
        file.dump(score)

import pickle
with open('file', 'w') as file:
    file = pickle.Pickler(file)
    
    file.dump(variable)

#!/usr/bin/python3.7
import pickle
import game_def

game_innit = True

print("----------------------------------------")
print("---------  Welcome to hangman  ---------")
print("----------------------------------------")



while game_innit:

    game_def.score_load()
    game_def.level_c()
    game_def.pick_word()
    #to cheat uncomment the line bellow
    # print(game_def.word_to_guess)
    print("----------------------------------------")
    print(game_def.user_word)
    print("----------------------------------------")
    win = False
    i = 0
    while i < 8 and win == False:
        game_def.turn()
        new_game_check = True
        if game_def.user_word == game_def.check_word:
            win = True
            temp_score = 7 - i
            print("you won ! with a score of {}".format(temp_score))
            game_def.score[game_def.player] = temp_score + game_def.score[game_def.player]
            with open('score.pickle', 'wb') as file:
                file = pickle.Pickler(file)
                file.dump(game_def.score)
            print("now your whole score is {}".format(game_def.score[game_def.player]))





        i += 1
        if i == 8:
            print('sorry no attempt remaning you lost :(')

    while new_game_check:
        new_game = input("do you want to play again ? (y/n)")
        if new_game == 'n':
            print("ok good bye !")
            game_innit = False
            new_game_check = False
        elif new_game == 'y':
            game_innit = True
            new_game_check = False
            game_def.level_innit = True
        else:
            new_game_check = True


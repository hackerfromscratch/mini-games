#!/usr/bin/python3.6

# import :
import random
import subprocess
import getch
import time 
import pickle
from pynput import keyboard
import os
# global variables
get_move = None
autorized = [keyboard.Key.down, keyboard.Key.up, keyboard.Key.right, keyboard.Key.left]
level = 0
speed = [0.1, 0.2, 0.3] # the level logic is the number of time in secondes the game wait 
                        # before clearing the screen and print the map again 
game_init = False
curent_direction = 'right' # default direction  
first_msg = '''
to start a new game chose the level :
    1 -----> easy
    2 -----> medium
    3 -----> hard
'''


with open('map.txt', 'r') as file: # reading the map from map.txt
    game_map = file.read()
with open('banner.txt', 'r') as file: # reading the map from map.txt
    banner = file.read()
subprocess.call('clear')

class Snake:
    
    def __init__(self):
            global game_map,level
            self.score = 0
            self.head = 'X'
            self.body_member = 'O'
            self.meal = '+'
            self.meal_position = 0
            self.body = []
            self.head_position = 230
            self.lost = False
            for x in self.body :   # spawning the head
                    game_map = game_map[:x] + self.body_member + game_map[x + 1:]

            for i in range(4): # spawning the body
                    i = i + 1
                    self.body.append(self.head_position - i)
            game_map = game_map[:self.head_position] + self.head + game_map[self.head_position + 1:]

    def make_a_move(self,number_of_moves, direction):

            global game_map, target, old_head_position, path, score, game
            
            for i in range(number_of_moves): 
                if self.meal_position == 0: # sapwning a meal 
                    while True:
                        self.meal_position = random.randrange(55,969)
                        if game_map[self.meal_position] == ' ':
                            game_map = game_map[:self.meal_position] + self.meal + game_map[self.meal_position + 1:]
                            break
                        else:
                            pass 
                
                time.sleep(level)  # the speed game (level)
                
                old_head_position = self.head_position 
                target = self.head_position + direction
                
                if game_map[target] == '+' : # expending the body if the snake eat a fruit
                    len_body = len(self.body)
                    new_body_part = self.body[len_body - 1] -1
                    self.body.append(new_body_part)
                    self.meal_position = 0    # we change the position to 0 so the loop for the meal init again 
                    self.score = self.score + 1 # adding 1 point to the score

                # the magic boucle where every body part get a new position wich is the part in front of it....
                path = self.body.copy()
                x = len(self.body)
                x = x-1
                i = 1
                while True :
                    path[0] = self.head_position
                    if i >= x :
                        break
                    else:
                        path[i] = self.body[i -1 ] 
                    i = i + 1

                #moving the head ------------
                self.head_position = self.head_position + direction
                target = self.head_position + direction
                if game_map[self.head_position] == '|'  or game_map[self.head_position] == '-'or game_map[self.head_position] == '"':
                    print('game over !') 
                    self.lost = True
                    break
                game_map = game_map[:self.head_position ] + self.head + game_map[self.head_position + 1 :]
                game_map = game_map[:old_head_position] + ' ' + game_map[old_head_position + 1:]
                
                # ---- moving the body
                old_path = self.body.copy()  
                for x in range(len(path)) :
                    
                    game_map = game_map[:path[x] ] + self.body_member + game_map[path[x] + 1 :]
                    game_map = game_map[:old_path[x] ] + ' '+ game_map[old_path[x] + 1 :]
                
                self.body = path # saving the new body parts position from the path
                
                # printing the map and the scores---------------
                subprocess.call('clear')
                print(game_map)
                print(f"current score is >> {self.score} <<        best score is >> {score[game]}<<")
        
python = Snake() # init a new snake object named python ;)
 
def on_press(key): # a function to use with pynut when a key is pressed
    global get_move, autorized
    try:
        get_move = key.char
    except AttributeError:
        if key in autorized:
            get_move = key
            
listener = keyboard.Listener( # ------------------------------------------------------------------
    on_press=on_press)
listener.start() # the listener is always runing to check if th user entred a new move for more info check pynut library


check_save_file = os.stat('score.pickle').st_size == 0 #check if the score is empty
if check_save_file == True:  #if file empty we just set the score var for now and save later
        score = [0, 0, 0, 0]
        with open ('score.pickle', 'wb') as file:  #score file exist
            file = pickle.Pickler(file)
            file.dump(score)  
else:
    with open ('score.pickle', 'rb') as file:  # loading the score if exist
        file = pickle.Unpickler(file)
        score = file.load()
          

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> game loops start here
print(banner)
    
def ask_for_new_game():
    global game, level,game_init
    print(first_msg)
    while True :  # getting the level and starting the game
        with open('map.txt', 'r') as file: # reading the map from map.txt
            game_map = file.read()
        game = getch.getch()
        python.lost = False
        try : 
            game = int(game)
            if game == 1 :
                level = speed[2]
                game_init = True
                break
            elif game == 2 :
                level = speed[1]
                game_init = True
                break
            elif game == 3 :
                level = speed[0]
                game_init = True
                break
        except:
            pass
print(game_map)
ask_for_new_game()
while game_init:    
    
    try:
        if python.lost is True:  # if lost than break the loop
            print('do you want to play another game ? ')
            ask_for_new_game()
             
                
        if get_move is keyboard.Key.down: # we check the move from keyborad input 
            if curent_direction == 'up': # check if the player not triying to go reverse if yes we ignore the move
                get_move = keyboard.Key.up # we force the snake like this the opposite way wich is the current way... 
                pass
            else:
                python.make_a_move(1,54) # the actual move 54 is for going down in this particular map
                curent_direction = 'down' # we save the direction to check after if it not trying to go reverse
        
        # same logic for the rest of the moves...
        
        elif get_move is keyboard.Key.right:      
            if curent_direction == 'left':
                get_move = keyboard.Key.left
                pass
            else:
                python.make_a_move(1,1)
                curent_direction = 'right'
        
        elif get_move is keyboard.Key.left:
            if curent_direction == 'right':
                get_move = keyboard.Key.right
                pass
            else:
                python.make_a_move(1,-1)
                curent_direction = 'left'
        
        elif get_move is keyboard.Key.up:
            if curent_direction == 'down':
                get_move = keyboard.Key.down
                pass
            else:
                python.make_a_move(1,-54)
                curent_direction = 'up'
        
        else: # the default move direction right could be change but the spawn is a fix point near the left wall be carful 
            python.make_a_move(1,1)
            curent_direction = 'right'
    except KeyboardInterrupt: # simply exit with the keyboard 
        game_init = False




if score[game] < python.score: # saving the score
    score[game] = python.score
    with open('score.pickle', 'wb') as file:
        file = pickle.Pickler(file)
        file.dump(score)
        

print('good bye ! ')

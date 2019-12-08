#!/usr/bin/python3.7
import pickle

score = {}


with open('score.pickle','wb') as file:
    file = pickle.Pickler(file)
    file.dump(score)

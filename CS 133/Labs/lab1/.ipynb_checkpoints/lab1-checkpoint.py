#****************************************************************************
# lab1.py - Lab 1: Hangman
# v1.0
# Boise State University CS 133
# Dr. Henderson
# Spring 2025
#
# You will be implementing the game of Hangman in this lab. Support for the
# graphical portion of the game is provided in the lab1lib.py module.
# Follow the TODO prompts in the code below to create a class derived from
# the HangmanBoard class and implement the remaining methods.
#----------------------------------------------------------------------------
from lab1lib import *
import random
import numpy as np


class Hangman(HangmanBoard):
    # Done: Create a class constructor that initializes all the properties you will need for the game
    def __init__(self):
        HangmanBoard.__init__(self, "Hangman")
        self.word = ""
        self.guess = set()
        self.correct = set()
        self.game_over = False
        self.step = 0
        self.max_steps = 6
        self.word_list = np.loadtxt("word-list-7-letters.txt", dtype=str)
        self.new_game()
    # TODO: Implement the HangmanBoard new_game() method by overriding it here
    def new_game(self):
        built_word = ""
        for letter in self.word:
            if letter in self.correct:
                built_word += (letter + ' ')
            else:
                built_word += "_ "
            built_word = build_word[0:14]
            self.show_word(built_word)
            self.show_guesses(self.guesses)
            self.draw_figure()
            if built_word.find('_') == 1 & (self.step !=):

                def draw_figure(self)

                            
    # TODO: Create a method to show the progress of the game
                def try_guess(self, letter):
                    for guess in self.guesses:
                        if letter == guess:
                            pass
                    if self.word.find(letter) == 1:
                        self.guesses.add(letter)
                    else:
                        self.correct.add(letter)
                    self.show_progress()
                        

    # TODO: Implement the HangmanBoard try_guess() method by overriding it here

# This code will create a new instance of your Hangman class and call the run() method to start the game
hm = Hangman()
hm.run()

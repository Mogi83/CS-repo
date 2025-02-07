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
        self.clear()
        self.word = random.choice(self.word_list).lower()
        self.guesses.clear()
        self.correct.clear()
        self.step = 0
        self.game_over = False
        self.show_progress()
                            
    # TODO: Create a method to show the progress of the game
    def show_progress(self):
        
        built_word = " ".join([letter if letter in self.correct else "_" for letter in self.word])
        
        self.show_word(built_word)
        
        self.show_guesses(f"Guesses: {', '.join(sorted(self.guesses))}")

        if "_" not in built_word:
            self.game_over = True
            self.show_word(f"You win! The word was '{self.word}'.")

        if self.step >= self.max_steps:
            self.game_over = True
            self.show_word(f"Game Over! The word was '{self.word}'.")

    def draw_figure(self):
        draw_steps = [
            self.draw_head,
            self.draw_body,
            
            self.draw_arm,  #left
            
            self.draw_arm,  #right
            
            self.draw_leg,
            
            self.draw_leg,
        ]

        for i in range(self.step):
            if i == 1 or i == 3:
                draw_steps[i](i % 2 == 0)
            elif i == 4 or i == 5:
                draw_steps[i](i % 2 == 0)
            else:
                draw_steps[i]()


    # TODO: Implement the HangmanBoard try_guess() method by overriding it here
    def try_guess(self, letter):
        if letter in self.guesses:
            return

        self.guess.add(letter)

        if letter in self.word:
            self.correct.add(letter)
        else:
            self.step += 1
            self.draw_figure()

    self.show_progress()
                        



# This code will create a new instance of your Hangman class and call the run() method to start the game
hm = Hangman()
hm.run()

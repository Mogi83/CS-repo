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

#Ive added some other function definitions I hope thats fine. 


from lab1lib import *
import random
import numpy as np


class Hangman(HangmanBoard):
    def __init__(self):
        HangmanBoard.__init__(self, "Hangman")
        self.word = ""
        self.guessed_letters = set()
        self.correct = set()
        self.game_over = False
        self.step = 0
        self.max_steps = 6
        self.word_list = np.loadtxt("word-list-7-letters.txt", dtype=str)
        self.new_game()

    def new_game(self):
        self.clear()
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters.clear()
        self.correct.clear()
        self.step = 0
        self.game_over = False
        
        #print(f"The word is: {self.word}") #for cheaters
        
        self.show_progress()

    def show_progress(self):
        built_word = " ".join([letter if letter in self.correct else "_" for letter in self.word])
        self.show_word(built_word)
        self.show_guesses(f"Guesses: {', '.join(sorted(self.guessed_letters))}")

        if built_word.find('_') == -1:
            self.game_over = True
            self.show_word(f"You win! The word was '{self.word}'.")

        if self.step >= self.max_steps:
            self.game_over = True
            self.show_word(f"Game Over! The word was '{self.word}'.")

    def draw_figure(self):
        draw_steps = [
            self.draw_head,
            self.draw_body,
            self.draw_arm,  # Left arm
            self.draw_arm,  # Right arm
            self.draw_leg,  # Left leg
            self.draw_leg,  # Right leg
        ]
    
        for i in range(self.step):
            if i == 2 or i == 3:  # Arms (left and right)
                draw_steps[i](i % 2 == 0)  # Pass True for left, False for right
            elif i == 4 or i == 5:  # Legs (left and right)
                draw_steps[i](i % 2 == 0)  # Pass True for left, False for right
            else:  # Head and body (no arguments needed)
                draw_steps[i]()

    def try_guess(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Error expected letter recived multiple, or non letter")
            return

        if letter in self.guessed_letters:
            print("You've already guessed that letter! Try again.")
            return

        self.guessed_letters.add(letter)  

        if letter in self.word:
            self.correct.add(letter) 
        else:
            self.step += 1
            self.draw_figure()
            
        self.show_progress()

# This code will create a new instance of your Hangman class and call the run() method to start the game
hm = Hangman()
hm.run()

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

class Hangman(HangmanBoard):

    # TODO: Create a class constructor that initializes all the properties you will need for the game

    # TODO: Implement the HangmanBoard new_game() method by overriding it here
        
    # TODO: Create a method to show the progress of the game

    # TODO: Implement the HangmanBoard try_guess() method by overriding it here

# This code will create a new instance of your Hangman class and call the run() method to start the game
hm = Hangman()
hm.run()

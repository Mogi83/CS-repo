#****************************************************************************
# lab1lib.py - Lab 1 support files
# v1.0
# Boise State University CS 133
# Dr. Henderson
# Spring 2025
#
# This class draws the gameboard for a game of hangman. It provides methods
# draw the parts of the man, show the guessed word and more.
#
# The derived class must implement the mechanics of the game (see TODOs below)
#----------------------------------------------------------------------------
import tkinter as tk
from PIL import Image, ImageDraw

class HangmanBoard(tk.Tk):
    def __init__(self, title, width = 300, height = 300):
        tk.Tk.__init__(self)
        self.geometry(f"{width}x{height+200}")
        self.title(title)
        self.width = width
        self.height = height
        self.hang_x = 150
        self.hang_y = 50
        self.headsize = 50
        self.bodysize = 100

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="white", cursor="cross")
        row = 0
        self.canvas.grid(row=row, column=0, sticky=tk.W)
        row += 1

        self.label_word = tk.Label(self, font=("Helvetica", 18))
        self.label_word.grid(row=row, column=0,pady=2)
        row += 1
        
        self.entry = tk.Entry(self, width=2, font=('Helvitica',14,'normal'))
        self.entry.focus_set()
        self.entry.grid(row=row,column=0,pady=2)
        row += 1

        self.guess_btn = tk.Button(self, text="Guess", command=self.on_guess)
        self.guess_btn.grid(row=row,column=0,padx=2,pady=2)
        row += 1

        self.button_reset = tk.Button(self, text="New Game", command=self.new_game )
        self.button_reset.grid(row=row,column=0,pady=2)
        row += 1

        self.label_guesses = tk.Label(self, font=("Helvetica", 18))
        self.label_guesses.grid(row=row, column=0,pady=2)
        row += 1

        self.img = Image.new("L", (self.width, self.height), (0))
        self.imgdraw = ImageDraw.Draw(self.img)

    def run(self):
        self.mainloop()

    def clear(self):
        self.canvas.delete('all')
        self.img = Image.new("L", (self.width, self.height), (0))
        self.imgdraw = ImageDraw.Draw(self.img)

    def draw_head(self):
        x = self.hang_x - self.headsize // 2
        y = self.hang_y
        self.canvas.create_oval(x, y, x+self.headsize, y+self.headsize)

    def draw_body(self):
        x = self.hang_x
        y = self.hang_y + self.headsize
        self.canvas.create_line(x, y, x, y + self.bodysize)

    def draw_arm(self, is_left = False):
        x = self.hang_x
        y = self.hang_y + self.headsize + self.bodysize // 3
        armlen = -50 if is_left else 50
        self.canvas.create_line(x, y, x + armlen, y)

    def draw_leg(self, is_left = False):
        x = self.hang_x
        y = self.hang_y + self.headsize + self.bodysize
        leglen = -50 if is_left else 50
        self.canvas.create_line(x, y, x + leglen, y + abs(leglen))

    def show_word(self, word):
        self.label_word.configure(text=word)

    def show_guesses(self, guesses):
        self.label_guesses.configure(text=guesses)

    def on_guess(self):
        guess = self.entry.get()
        self.entry.delete(0)
        self.try_guess(guess)

    def try_guess(self, guess):
        #TODO
        pass

    def new_game(self, guess):
        #TODO
        pass

    def get_word(self):
        #TODO
        pass
    


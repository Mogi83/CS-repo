Lab 1: Hangman
==========
_Version 1_

Hangman is a word guessing game where the player incrementally guesses letters. If a guess is incorrect, another part of the "hangman" is drawn on the board.
When the "hangman is full drawn the player loses. If the player guesses all the corrrect letters before the hangman is fully drawn they win.

For this lab you are given an implemented class called HangmanBoard which handles all of the graphics for you. Your job is to derive your own class that implements
all the gameplay. The file lab1.py has the starter code with comments marked # TODO in the places you need to implement.

When the HangmanBoard.run() method is called it will display the gameboard screen with some buttons. By clicking the buttons it will cause an event that eventually
calls your code. For example, when the user clicks on the New Game button, your implementation of the new_game() method will be called. Inside your implementation
you can then call some of the helper methods of the HangmanBoard class. For example, you might want first clear the board by calling clear(). Note: To call one
of the methods of the HangmanBoard class you still use the `self` parameter like this: `self.clear()`

**Description of files**
| File               | Description                                                  |
|--------------------|:-------------------------------------------------------------|
| lab1.py            | Main file for the lab - add your implementation here         |
| lab1lib.py         | Support library implementing the HangmanBoard class          |
| word-list-7-letter.txt | List of seven letter words to use for the game              |


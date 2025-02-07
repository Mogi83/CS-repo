from lab1lib import *

from lab1 import *


class TestHangman:
    def __init__(self):
        self.board = HangmanBoard("Test Hangman", 300, 400)  # Initialize with a basic size
        self.board.word = "hangman"  # Set the word for testing
        self.board.correct = set()
        self.board.guessed_letters = set()
        self.board.step = 0  # Start with 0 incorrect guesses

    def test_correct_guess(self, guess):
        print(f"Testing correct guess: {guess}")
        self.board.try_guess(guess)  # Simulate the correct guess
        built_word = " ".join([letter if letter in self.board.correct else "_" for letter in self.board.word])
        print(f"Word after correct guess: {built_word}")
        print(f"Correct guesses so far: {self.board.correct}")
        print(f"Incorrect guesses: {self.board.step}")
        print("-" * 50)

    def test_incorrect_guess(self, guess):
        print(f"Testing incorrect guess: {guess}")
        self.board.try_guess(guess)  # Simulate the incorrect guess
        built_word = " ".join([letter if letter in self.board.correct else "_" for letter in self.board.word])
        print(f"Word after incorrect guess: {built_word}")
        print(f"Correct guesses so far: {self.board.correct}")
        print(f"Incorrect guesses: {self.board.step}")
        print("-" * 50)

test_game = TestHangman()

# Test Correct Guess
test_game.test_correct_guess("a")  # Correct guess: 'a' is in "hangman"
test_game.test_correct_guess("n")  # Correct guess: 'n' is in "hangman"

# Test Incorrect Guess
test_game.test_incorrect_guess("z")  # Incorrect guess: 'z' is not in "hangman"
test_game.test_incorrect_guess("b")  # Incorrect guess: 'b' is not in "hangman"
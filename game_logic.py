import random
from typing import List

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word() -> str:
    """Select a random word from the list."""
    return random.choice(WORDS)


def get_valid_guess(guessed_letters: List[str]) -> str:
    """Ask the user for a single new letter and validate the input."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter from a–z.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        return guess


def display_game_state(mistakes: int, secret_word: str, guessed_letters: List[str]) -> None:
    """Show the current snowman stage and the masked word."""
    print(STAGES[mistakes])
    print(f" Mistakes: {mistakes} / {MAX_MISTAKES}")

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f" Word:     {display_word}")

    if guessed_letters:
        print(" Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print(" Guessed letters: (none yet)")

    print("-" * 40)


def play_game() -> bool:
    """Run one full game and return True if the player wins."""
    secret_word = get_random_word()
    guessed_letters: List[str] = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("-" * 40)

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You saved the snowman. The word was '{secret_word}'.")
            return True

        if mistakes >= MAX_MISTAKES:
            print(STAGES[mistakes])
            print(f"Oh no! The snowman melted. The word was '{secret_word}'.")
            return False

        guess = get_valid_guess(guessed_letters)

        if guess in secret_word:
            print(f"Good job! The letter '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            mistakes += 1

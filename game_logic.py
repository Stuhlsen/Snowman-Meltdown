from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters: list[str] = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # last valid stage index

    print("Welcome to Snowman Meltdown!")

    while True:
        # Show current state (stage + revealed letters)
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win condition: all unique letters of the secret word have been guessed
        if set(secret_word).issubset(set(guessed_letters)):
            print(f"You saved the snowman! The word was '{secret_word}'.")
            break

        # Lose condition: mistakes reached the last stage
        if mistakes >= max_mistakes:
            print(f"Meltdown! The word was '{secret_word}'.")
            break

        # Prompt for a single-letter guess
        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Already guessed?
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Check guess
        if guess in secret_word:
            guessed_letters.append(guess)
            print(f"Good guess: '{guess}'")
        else:
            mistakes += 1
            print(f"Wrong guess: '{guess}'")


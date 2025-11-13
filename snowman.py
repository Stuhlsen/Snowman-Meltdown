from game_logic import play_game


def main() -> None:
    """Program entry point; allows the user to play multiple games."""
    while True:
        play_game()

        answer = input("\nPlay again? (y/n): ").strip().lower()
        while answer not in ("y", "n"):
            answer = input("Please enter 'y' or 'n': ").strip().lower()

        if answer == "n":
            print("Thanks for playing Snowman Meltdown. Goodbye!")
            break


if __name__ == "__main__":
    main()

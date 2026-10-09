"""
CodeAlpha - Python Programming Internship
TASK 1: Hangman Game

A simple text-based Hangman game.
- 5 predefined words
- Max 6 incorrect guesses
- Basic console input/output
"""

import random

WORDS = ["python", "hangman", "coding", "internship", "programming"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("  WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: ", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[wrong_guesses])
                print(f"Word: {display_word(word, guessed_letters)}")
                print("\n🎉 Congratulations! You guessed the word: " + word)
                break
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")
    else:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"\n💀 Game Over! The word was: {word}")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye 👋")
            break


if __name__ == "__main__":
    main()

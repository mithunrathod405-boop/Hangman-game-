import random

# Five predefined words to choose from
WORDS = ["python", "keyboard", "program", "variable", "function"]
MAX_WRONG_GUESSES = 6


def display_word(secret, guessed):
    """Return the word with guessed letters revealed and the rest as underscores."""
    result = ""
    for letter in secret:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def play_hangman():
    secret = random.choice(WORDS)
    guessed = []  # letters the player has guessed so far
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", display_word(secret, guessed))
        print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)
        print("Letters guessed:", ", ".join(guessed) if guessed else "none")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed:
            print("You already guessed that letter.\n")
        else:
            guessed.append(guess)
            if guess in secret:
                print("Good guess!\n")
            else:
                wrong_guesses += 1
                print("Wrong!\n")

        # Win check: every letter in the secret word has been guessed
        if all(letter in guessed for letter in secret):
            print("Word:", secret)
            print("You won!")
            return

    print(f"Out of guesses! The word was '{secret}'.")


if __name__ == "__main__":
    play_hangman()

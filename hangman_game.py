import random


def play_hangman():
    words = ["FUTURE", "LAPTOP", "CODING", "PYTHON", "MACHINE"]

    secret_word = random.choice(words)

    guessed_letters = []
    wrong_guesses = []
    max_wrong_guesses = 6

    print("\n" + "=" * 45)
    print("       WELCOME TO HANGMAN WORD GAME!")
    print("=" * 45)
    print("Guess the hidden word one letter at a time.")
    print(f"You can make only {max_wrong_guesses} wrong guesses.")
    print("=" * 45)

    while len(wrong_guesses) < max_wrong_guesses:
        displayed_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "

        print("\nWord:", displayed_word)
        print(
            "Guessed letters:",
            ", ".join(guessed_letters) if guessed_letters else "None",
        )
        print("Wrong guesses:", ", ".join(wrong_guesses) if wrong_guesses else "None")
        print("Wrong guesses remaining:", max_wrong_guesses - len(wrong_guesses))

        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 45)
            print("Congratulations! You guessed the word!")
            print("The word was: ", secret_word)
            print("=" * 45)
            return

        guess = input("\n Enter a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another one.")
            continue
        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            wrong_guesses.append(guess)
            print("Wrong guess!")

    print("\n" + "=" * 45)
    print("Game Over! You ran out of wrong guesses.")
    print("The correct word was:", secret_word)
    print("=" * 45)


def main():
    while True:
        play_hangman()

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if again != "yes":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()

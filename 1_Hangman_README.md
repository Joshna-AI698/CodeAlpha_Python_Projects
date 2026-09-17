# Hangman Game

## Description

Hangman is a simple console-based word-guessing game developed using Python. The player must guess a randomly selected hidden word by entering one letter at a time.

The player is allowed a maximum of six incorrect guesses. The game ends when the player guesses the word correctly or uses all the allowed attempts.

## Features

- Selects a word randomly from a predefined list
- Allows the player to guess letters one at a time
- Displays the progress of the hidden word
- Tracks incorrect guesses
- Allows a maximum of six incorrect guesses
- Displays winning and losing messages
- Provides an option to play again

## Concepts Used

- Python
- `random` module
- Lists
- Strings
- While loops
- If-else statements
- User input

## How to Run

1. Make sure Python is installed on your system.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python hangman_game.py
```

## How the Game Works

1. The program selects a word randomly from a predefined list.
2. The selected word is displayed as underscores.
3. The player enters a letter as a guess.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses increase the incorrect-guess count.
6. The player wins by guessing the complete word within six incorrect guesses.
7. The player loses if all six incorrect guesses are used before completing the word.

## Project Type

Console-based Python Game

## Internship

This project was developed as part of the CodeAlpha Python Internship.

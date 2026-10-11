# Python Hangman Game — Task 1

## Project overview
Hangman is a text-based word-guessing game. The computer randomly selects one word from a list of five words. The player guesses one letter at a time and has up to six incorrect guesses.

## Features
- Random word selection from five predefined words
- Hidden-letter display using underscores
- Six incorrect guesses maximum
- Input validation (one alphabet letter at a time)
- Repeated guesses do not consume a life
- Win/lose messages and option to play again

## Concepts used
- `random.choice()` for random selection
- Lists and strings
- `while` loops
- `if-elif-else` conditions
- Functions
- `input()` and `print()`

## Requirements
Python 3.8 or newer. No extra libraries are needed.

## How to run
1. Save `hangman.py` to your computer.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python hangman.py
   ```

   If your system uses `python3`, run `python3 hangman.py`.

## Rules
1. Enter one alphabet letter per turn.
2. Correct guesses reveal the letter.
3. Incorrect guesses reduce your remaining lives.
4. Guess the whole word's letters before you run out of six lives to win.

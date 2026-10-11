import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "coding", "gamer", "laptop", "syntax"]
    
    # Randomly select a word from the list
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect:
        # Build the current display word (e.g., "_ y t _ o n")
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("Word:", display_word.strip())

        # Check if the player has won
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            return

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabetical letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.\n")
            continue

        # Add the guess to our tracked list
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word.")
            print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}\n")

    # If the loop finishes and they ran out of guesses
    print(f"Game Over! You ran out of guesses. The word was: {word_to_guess}")

# Run the game
if __name__ == "__main__":
    play_hangman()

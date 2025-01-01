import random

def run_game():
    # You can keep adding more words to the list if you like
    word_list = [
        'apple', 'secret', 'banana', 'python', 'keyboard',
        'mountain', 'hangman', 'jupyter', 'developer'
    ]

    word: str = random.choice(word_list)

    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!\n")

    guessed_letters: str = ''
    tries: int = 5

    while tries > 0:
        blanks: int = 0

        # Show the current state of the guessed word
        print('Word: ', end='')
        for char in word:
            if char in guessed_letters:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
        print()  # Move to a new line

        # If no blanks, the user has guessed all letters
        if blanks == 0:
            print(f"Congratulations! You correctly guessed '{word}'!")
            break

        guess: str = input("Enter a single letter: ").strip().lower()

        # Validate input: must be a single alpha character
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter exactly one letter (A-Z).")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f'You already used "{guess}". Try another letter.')
            continue

        # Add the guess to the set of guessed letters
        guessed_letters += guess

        # If guess not in word, decrement tries
        if guess not in word:
            tries -= 1
            if tries > 0:
                print(f"Sorry, '{guess}' is not in the word. ({tries} tries remaining)\n")
            else:
                print("No more tries remaining...")
                print(f"The word was '{word}'. Better luck next time!\n")
                break

def main():
    while True:
        run_game()
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == '__main__':
    main()

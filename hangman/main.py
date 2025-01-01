import random


def run_game():
    word: str = random.choice(['apple', 'secret', 'banana'])

    username: str = input('What is your name? >>')
    print(f'Welcome to hangman, {username}')

    guessed: str = ''

    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
        print()  # adds a blank line

        if blanks == 0:
            print('You guessed the word.')
            break
        guess: str = input('Enter a letter: ')

        if guess in guessed:
            print(f'You already used: "{guess}". Please try another letter')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining...')
                break


if __name__ == '__main__':
    run_game()

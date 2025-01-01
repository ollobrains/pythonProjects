import random

def play_guessing_game(lower_num=1, higher_num=10, max_attempts=5):
    random_number = random.randint(lower_num, higher_num)
    print(f"\nGuess the number between {lower_num} and {higher_num}!")
    attempts = 0

    while attempts < max_attempts:
        try:
            guess_str = input(f"Attempt {attempts+1}/{max_attempts} - Your guess: ")
            user_guess = int(guess_str)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_guess < lower_num or user_guess > higher_num:
            print(f"Your guess is out of range! ({lower_num}-{higher_num})")
            continue

        attempts += 1

        if user_guess < random_number:
            print("Too low!")
        elif user_guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number: {random_number}")
            return

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {random_number}.")

if __name__ == "__main__":
    while True:
        play_guessing_game(1, 10, 5)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

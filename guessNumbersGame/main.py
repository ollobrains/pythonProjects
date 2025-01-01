import random

lower_num, higher_num = 1, 10

random_number: int = random.randint(lower_num, higher_num)

print(f"Guess the number in the range from {lower_num} to {higher_num}.")

while True:
    try:
        user_guess: int = int(input("Guess: "))
    except ValueError as err:
        print(f"Enter a valid number: {err}")
        continue
    if user_guess > random_number:
        print("The number is lower")
    elif user_guess < random_number:
        print("The number is higher")
    else:
        print(f"You guessed the number: it is {random_number}!")
        break

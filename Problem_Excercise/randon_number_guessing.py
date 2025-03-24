import random

number_to_guess = random.randrange(150)

total_chances = 5
guess_ctr = 0

while guess_ctr < total_chances:
    guess_ctr += 1
    guess = int(input("Enter your guess (0-150): "))

    if guess == number_to_guess:
        print("You found it right!")
        break
    elif guess < number_to_guess:
        print("Your guess is lower!")
    elif guess > number_to_guess:
        ("Your guess is higher!")


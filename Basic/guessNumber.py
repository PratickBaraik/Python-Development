import random

secretNumber = random.randint(10, 50)

attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 10 to 50: "))
        attempts += 1

        if guess == secretNumber:
            print(f"Congratulations! You've guessed {secretNumber} in {attempts} attempts.")
            break
        elif guess < secretNumber:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid integer between 10 and 50.")

print("Thank you for playing!")
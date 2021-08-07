import random

secretNumber = random.randint(1,50)
print("I am thinking of a number between 1 and 50")
for Guesses in range(1,8):
    guessedNumber = int(input("Take a guess: "))
    if guessedNumber > secretNumber:
        print("Your number is too high")
    elif guessedNumber < secretNumber:
        print("Your number is too low")
    else:
        break

if secretNumber == guessedNumber:
    print(f"Congratulations, you won in {Guesses} moves")
else:
    print(f"You lost, the number was {secretNumber}")

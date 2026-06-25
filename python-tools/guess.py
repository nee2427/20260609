import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print("Guess a number between 1 to 99.")
print("I will give you 6 tries.")

while tries < 6:
    guess = int(input("What's your guess? "))
    tries += 1
    if guess < secret:
        print("Your guess is too low.")
    elif guess > secret:
        print("Your guess is too high.")
    else:
        break

if guess == secret:
    print("Yes! You got it!")
else:
    print("No more guesses!")
    print("The secret number was", secret)

import random

print("***Welcome to the Number Guessing Game! ***\nI'm thinking of number between 1 and 100. Can you guess it?")
num = random.randrange(1,100)
attempt = 0
while True:
    player = int(input("Enter your guess: "))
    if player > num:
        print("Too high, Try again")
        attempt += 1
    elif player < num:
        print("Too low, Try again")
        attempt += 1
    elif player == num:
        print(f"Congratulations!!! You guessed the number attempts {attempt+1}")
        break
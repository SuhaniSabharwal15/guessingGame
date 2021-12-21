import random 
print ("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9:")
while chances < 5:
    guess = int(input("enter your guess:"))
    if guess == number:
        print("you won")
        break
    elif guess < number:
        print ("guess a higher number")
    else: 
        print ("guess a lower number")
    chances += 1
if not chances < 5:
    print("You Lose! the number is ", number)

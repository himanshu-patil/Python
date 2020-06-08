import random
print("I am thinking of a number between 1 to 20...")
secretNumber=random.randint(1,20)

for guessTaken in range(1,7):
    guess=int(input("Take a guess:"))
    if guess > secretNumber:
        print("Your guess is too high")
    elif guess< secretNumber:
        print("your guess is too low")
    else:
        print("You got it!")
        break
if guess==secretNumber:
    print("Good Job! You guessed my no in "+str(guessTaken)+" guesses!")
else :
    print("Nope.The number i was thinking of was.. "+str(secretNumber))





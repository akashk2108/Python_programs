import random

highest =100
answer = random.randint(1,highest)

guess= None
while(True):
    guess= int(input("Please enter a number between 1 and {}:- ".format(highest)))
    if guess ==0:
        print("Game over")
        break
    if guess==answer:
        print("you have guess it correctly")
        break
    elif guess>answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
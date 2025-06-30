'''
water = 0
gun = 1
snake = -1
'''
import random

chossDict = {"s" : -1, "w": 0, "g": 1}
revdict = {-1: "snake", 0:"water", 1:"gun"}

com_choice = random.choice([0,1,-1])
your_choice = input("Enter your choice :> ")

you = chossDict[your_choice]

print(f"you chose :> {revdict[you]} \ncomputer chose :> {revdict[com_choice]}")

if(you == com_choice):
    print("its draw")
else:
    if((com_choice-you) == -1 or (com_choice- you) == 2):
        print("you loose")
    else:
        print("you win")



'''
-----------------------------------------------------refined version--------------------------------------------------------
import random

# Mappings
choiceDict = {"s": -1, "w": 0, "g": 1}
revDict = {-1: "snake", 0: "water", 1: "gun"}

# Computer choice
com_choice = random.choice([-1, 0, 1])

# Player input
your_choice = input("Enter your choice (s for snake, w for water, g for gun):> ").lower()

if your_choice not in choiceDict:
    print("Invalid input. Please choose 's', 'w', or 'g'.")
else:
    you = choiceDict[your_choice]

    print(f"\nYou chose        : {revDict[you]}")
    print(f"Computer chose   : {revDict[com_choice]}\n")

    # Game logic
    if you == com_choice:
        print("It's a draw!")
    elif (you == -1 and com_choice == 0) or \
         (you == 0 and com_choice == 1) or \
         (you == 1 and com_choice == -1):
        print("You win!")
    else:
        print("You lose!")

'''
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
    if(com_choice == 0 and you == 1):
        print("you loss")
    elif(com_choice == 0 and you == -1):
        print("you win")
    elif(com_choice == 1 and you == 0):
        print("you win")
    elif(com_choice == 1 and you == -1):
        print("you loss")
    elif(com_choice == -1 and you == 0):
        print("you loss")
    elif(com_choice == -1 and you == 1):
        print("you win")
    else:
        print("somthing wrong")

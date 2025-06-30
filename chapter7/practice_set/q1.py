# 1. Write a program to print multiplication table of a given number using for loop. 

table = int(input("enter a number :> "))
def mutiplication (n):
    for i in range (10):
        print(f"{i+1} X {n} = {(i+1)*n}")
        
mutiplication(table)
# 1. Write a program to print multiplication table of a given number using for loop. 

# 3. Attempt problem 1 using while loop. 

table = int(input("enter a nunber :> "))

i = 1
while(i<11):
    print(f"{table} X {i} = {table * i}")
    i+=1

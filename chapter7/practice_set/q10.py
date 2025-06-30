# 10. Write a program to print multiplication table of n using for loops in reversed order. 


n = int(input("enter a number :> "))

# method 1

for i in range(1,11):
    print(f'{n} X {11-i} = {n*(11-i)}')



print("----------------------------------------------------------------------")

# method 2

for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")
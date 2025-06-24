# 1. Write a program to store seven fruits in a list entered by the user.

lis = []

for i in range(7):
    fru = input(f"enter a {i+1} fruits name :> ")
    lis.append(fru)

print(lis)
# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

n= int(input("enter a number: "))

t = [i * n for i in range(1,11)]
print(t)

with open("tables.txt", "a") as f :
    f.write(f"table of {n}: {str(t)} \n")
import random 

n = random.randint(1,100)

a = -1

gas = 0
while(a != n):
    
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        gas += 1
    elif(a<n):
        print("Higher number please")
        gas += 1
    
        

print(f"you have gassed the number correctly in {gas} attempt")
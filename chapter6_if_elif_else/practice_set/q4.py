# 4. Write a program to find whether a given username contains less than 10 characters or not. 

username = input("enter a username :> ")

# 1st 
# if(len(username)< 10)

# 2nd
c = 0
for i in username:
    c = c+1

if (c < 10):
    print("less")
else:
    print("more")
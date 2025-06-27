# 1. Write a program to find the greatest of four numbers entered by the user. 

# 1st method
# a = int(input("1st no. :> "))
# b = int(input("2nd no. :> "))
# c = int(input("3rd no. :> "))
# d = int(input("4th no. :> "))

# def findgrager(a,b,c,d):
#     if(a>b and a>c and a>d):
#         print("a")
#     elif(b>a and b>c and b<d):
#         print("b")
#     elif(c>a and c<b and c<d):
#         print("c")
#     else:
#         print("d")
        
# findgrager(a,b,c,d)


#  2nd method  manually
n = int(input("enter how many user wants to enter the no. :> "))

def grater(n):
    num = []
    for i in range(n):
        a = int(input(f"enter {i+1} number :> "))
        num.append(a)
    print(num)
    c = 0
    for i in num:
        if c<i:
            c = i
    
    return c
    # return max(num) 

print(grater(n))
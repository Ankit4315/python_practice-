# 1. Write a program using functions to find greatest of three numbers. 

def greater():
    a = int(input("enter a number :> ")) 
    b = int(input("enter a number :> ")) 
    c = int(input("enter a number :> ")) 
    if(a>b and a>c):
        print("a is greater")
    elif(b>a and b>c):
        print("b is greater")
    elif(c >a and c>b):
        print("c is grater")
    elif(a==b and a==c):
        print("all the number are equals")
    elif a == b and a > c:
        print("a and b are equal and greater than c")
    elif a == c and a > b:
        print("a and c are equal and greater than b")
    elif b == c and b > a:
        print("b and c are equal and greater than a")

    else:
        print("both are equle")

greater()
    
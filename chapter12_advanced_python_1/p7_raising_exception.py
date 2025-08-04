# RAISING EXCEPTIONS 
'''
We can raise custom exceptions using the 'raise' keyword in python. 
'''

a = int(input("enter a 1st num: "))
b = int(input("enter a 2nd num: "))


if(b==0):
    raise ZeroDivisionError("its con't be zero")
    # raise Exception ("hyee")
else:
    print(f"the divsion is {a/b}")


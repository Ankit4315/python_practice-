# Recursion is a function which calls itself. 
# It is used to directly use a mathematical formula as function.


'''

factorial(n) = n x factorial (n-1) 
This function can be defined as follows: 
def factorial(n) 
    if i == 0 or i==1: # base condition which doesn't call the function 
any further 
    return 1 
else: 
    return n*factorial(n-1) # function calling itself
    
'''

n = int(input("enter a  n umber :> "))

def fact(n):
    if(n==1 or n== 0):
        return 1
    return n * fact(n-1)

print(fact(n))



'''
The programmer needs to be extremely careful while working with recursion to ensure 
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most 
direct way to code an algorithm.
'''
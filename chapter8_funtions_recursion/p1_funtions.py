'''
A function is a group of statements performing a specific task. 
When a program gets bigger in size and its complexity grows, it gets difficult for a 
program to keep track on which piece of code is doing what! 
A function can be reused by the programmer in a given program any number of
'''

# EXAMPLE AND SYNTAX OF A FUNCTION 

def func1(): 
    print('hello') 
    
# This function can be called any number of times, anywhere in the program


# FUNCTION CALL  
'''
Whenever we want to call a function, we put the name of the function followed by 
parentheses as follows:
'''

func1() # This is called function call. 

# FUNCTION DEFINITION
'''
The part containing the exact set of instructions which are executed during the function call.
'''
def avg():                       # funtion defination
    a = int(input("inter a number :> "))
    b = int(input("inter a number :> "))
    print ((a+b)/2)

avg() # funtion call


# Quick Quiz:  Write a program to greet a user with “Good day” using functions.


def greet():
    name = input("enter a name :> ")
    print(f"good day {name}")
    
greet()
# FUNCTIONS WITH  ARGUMENTS 

'''
A function can accept some value it can work with. We can put these values in the parentheses.
'''

def goodday(name, surename):
    print("good day," + name)
    print(surename)
    
goodday("ankit", "dhakad")
goodday("ritik", "bhargava")
goodday("arvid", "kirar")


# A function can also return value 
def greet(name): 
    gr = "hello "+ name  
    return gr  
                    
a = greet ("ankit")
print(a)


# DEFAULT PARAMETER VALUE 

'''
We can have a value as default as default argument in a function. 
If we specify name = “stranger” in the line containing def, this value is used when no 
argument is passed.
'''

def greet(name , gr = "thank you"):
    print(f"hello {name}")
    print(gr)

greet("ankit")
greet("rohan", "thanks")

# EXCEPTION HANDLING IN PYTHON 

''' 
There are many built-in exceptions which are raised in python when something goes wrong. 
Exception in python can be handled using a try statement. The code that handles the 
exception is written in the except clause.
'''

try: 
   # Code which might throw exception  
   pass
except Exception as e:  
    print(e) 
    
'''
When the exception is handled, the code flow continues without program interruption. 
We can also specify the exception to catch like below: 
'''
try: 
    # Code 
    pass
except ZeroDivisionError: 
    # Code 
    pass
except TypeError: 
    # Code 
    pass
except: 
    # Code       # All other exceptions are handled here.
    pass


try:
    a= int(input("enter a number: "))
    print(a)
except Exception as e:
    print(e)
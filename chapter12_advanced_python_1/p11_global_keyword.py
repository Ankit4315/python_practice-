# THE GLOBAL KEYWORD  
'''
'global' keyword is used to modify the variable outside of the current scope.
'''
a = 89

def fun():
    global a
    a = 3  #local variable for the this funtion 
    print(a)
    
    

fun()
print(a)
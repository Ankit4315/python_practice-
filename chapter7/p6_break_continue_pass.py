
# THE BREAK STATEMENT 
'''
'break' is used to come out of the loop when encountered. It instructs the program to – 
exit the loop now. 
'''

for i in range (0,80): 
    print(i)     # this will print 0,1,2 and 3 
    if i==3:
        break    # exit the loop
    


# THE CONTINUE  STATEMENT
''' 
‘continue’ is used to stop the current iteration of the loop and continue with the next 
one. It instructs the Program to “skip this iteration”.
'''

for i in range(4): 
    print("printing") 
    if i == 2:   # if i is 2, the iteration is skipped  
        continue  # skip this itreration
    print(i)
    
    
# PASS STATEMENT 
''' 
pass is a null statement in python. 
It instructs to “do nothing”. 
'''
 
l = [1,7,8] 
for item in l: 
    pass          # without pass, the program will throw an error 
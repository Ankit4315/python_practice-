
'''
The range() function in python is used to generate a sequence of number. 

We can also specify the start, stop and step-size as follows: 

range(start, stop, step_size) # step_size is usually not used with range() 

AN EXAMPLE  DEMONSTRATING  RANGE () FUNCTION.  
 for i in range(0,7): # range(7) can also be used. 
    print(i) # prints 0 to 6
    
'''

for i in range(0,6):
    print(i)

name = ['ankit', 'jitendra']
for i in name:
    print(f"{i} dhakad")

for i in range(0,50):
    print(i+1, end=" ")
    
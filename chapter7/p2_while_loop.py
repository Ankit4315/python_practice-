# Syntax: 
a = 6
while (a > 0 ): # The block keeps executing until the condition is true Body of the loop 
    print(a)
    a= a-1
    
    
    
'''
in while loops, the condition is checked first. If it evaluates to true, the body of the loop 
is executed otherwise not! 
If the loop is entered, the process of [condition check & execution] is continued until 
the condition becomes False.
'''

# Quick Quiz: Write a program to print 1 to 50 using a while loop.
a = 1
while(a<51):
    print(a,end=" ")
    a=a+1
    
    
# Quick Quiz:  Write a program to print the content of a list using while loops.
li = ["ankit",True, 3, 4.2, "mohan", "vidya"]

i=0
while(len(li)>i):
    print(li[i])
    i+=1
    
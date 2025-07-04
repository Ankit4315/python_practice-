# 5. Write a python function to print first n lines of the following pattern: 
'''
*** 
**               - for n = 3 
* 
'''

def pat(n):
    if(n==0):
        return
    print("*"*n)
    pat(n-1)
    
n = int(input("enter a number :> "))
pat(n)
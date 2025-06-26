'''
Sometimes we want to play PUBG on our phone if the day is Sunday. 
Sometimes we order Ice Cream online if the day is sunny. 
Sometimes we go hiking if our parents allow. 
All these are decisions which depend on a condition being met.  

 **In python programming too, we must be able to execute instructions on a condition(s) being met. **
 
'''

# IF ELSE AND ELIF  IN PYTHON  

# If else and elif statements are a multiway decision taken by our program due to certain 
# conditions in our code.

# this if elif else ladder
age = int(input("enter your age :> "))
if (age>=18): # if condition1 is True 
    print ("yes") 
        
elif(age<18 and age>0): # if condition2 is True  
    print("no") 
 
else:             # otherwise 
    print("maybe")  
    
    
    
#  this is a if else statement
a=22 
if(a>9): 
    print("greater") 
else: 
    print("lesser") 
    
    
# Quick Quiz: Write a program to print yes when the age entered by the user is greater 
#             than or equal to 18.

ag = int(input("enter the age:> "))

if(age>=18):
    print("yes")
else:
    print("no")
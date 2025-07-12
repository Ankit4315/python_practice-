# SUPER() METHOD   

'''
super() method is used to access the methods of a super class in the derived class. 
super().__init__() 
# __init__() Calls constructor of the base class 
'''




class Employee:
    def __init__(self):
        
        print("constuctor of employee") 
    a= 1
        
        
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("constuctor of programmer") 
    b=2
       
class manger(Programmer):
    def __init__(self):
        super().__init__()
        print("constuctor of manager") 
    c = 3
    

# obj = Employee()

# p = Programmer()

m = manger()

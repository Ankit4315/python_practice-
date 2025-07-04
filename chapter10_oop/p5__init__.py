# __INIT__() CONSTRUCTOR 
'''
__init__() is a special method which is first run as soon as the object is created. 
__init__() method is also known as constructor. 
It takes 'self' argument and can also take further arguments. 
'''
# For Example: 

class Employee: 
    def __init__(self, name, sal):  # <------------------- dunder methos which is automatically called (starts with [__] duble under score)
        self.name=name 
        self.sal=sal
        
    def getSalary(self): 
        ... 
 
ankit = Employee("ankit", 200000) 

print(ankit.sal,ankit.name)
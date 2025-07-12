# @PROPERTY DECORATORS 

class Employee: 
    @property 
    def name(self): 
        return self.ename 
    
'''    
If e = Employee() is an object of class employee, we can print (e.name) to print the 
ename by internally calling name() function.
'''


class namestr:
     
     @property
     def name(self):
         return f"{self.fname} {self.lname}"
     
     @name.setter
     def name(self, value):
         self.fname = value.split(" ")[0]
         self.lname = value.split(" ")[1]
         
         
e = namestr()
e.name = "ankit dhakad"
print(e.fname, e.lname)



# @.GETTERS AND  @ .SETTERS  
'''
The method name with ‘@property’ decorator is called getter method.  
We can define a function + @ name.setter  decorator like below:
 
@name.setter 
def name (self,value): 
    self.ename = value 

'''
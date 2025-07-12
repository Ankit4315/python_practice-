# Inheritance is a way of creating a new class from an existing class.

class Employee:  # Base class  
    company = "itc"
    def show(self):
        print(f"the name is {self.name} and salary is {self.salary}")
 
# class Programmer():
#     company = "ITC company"
#     def show(self):
#         print(f"the name is {self.name} and salary is {self.salary}")
        
#     def showLanguage(self):
#        print(f"the name is {self.name} and he is good in {self.language} language")
       

class Programmer(Employee):
    company = "ITC company"
    def showLanguage(self):
       print(f"the name is {self.name} and he is good in {self.language} language")
    
# a = Employee()
b = Programmer()

b.name = "Ankit"
b.salary = 50000
b.language = "Python"


print(b.company)

print(b.show())



# We can use the method and attributes of ‘Employee’ in ‘Programmer’ object. 
# Also, we can overwrite or add new attributes and methods in ‘Programmer’ class.
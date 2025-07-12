class Employee:  # Base class  
    company = "itc"
    def show(self):
        print(f"the name is {self.name} and salary is {self.salary}")
 
class coder:  # Base class
    langauge = "python"
    def code(self):
        print("coding")
        
        
class Programmer(Employee, coder):
    company = "ITC company"
    def showLanguage(self):
       print(f"the name is {self.name} and he is good in {self.language} language")
    
# a = Employee()
b = Programmer()

b.name = "Ankit"
b.salary = 50000
b.language = "Python"


b.show()
b.code()
# print(b.company)

# print(b.show())

# print(b.code())

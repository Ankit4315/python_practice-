# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 



# method 1 
'''
class programmer():
    def __init__(self,language,name,team,project):
        self.language = language
        self.name=name
        self.team=team
        self.project= project
    
    def getinfo(self):
        print(f"name :> {self.name}, language :> {self.language}, team :> {self.team}, project :> {self.project}")
        

emp = programmer("java","ankit","new","realstate")

emp.getinfo()
'''
# method 2

class programmer():
    company = "microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    

emp = programmer("ankit",20000, 452012)

print(emp.name, emp.company, emp.pin, emp.salary)
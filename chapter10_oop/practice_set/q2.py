# 2. Write a class “Calculator” capable of finding square, cube and square root of a number. 

class calculator():
    
    def __init__(self, number):
        self.number = number
        
    def square(self):
        return self.number**2
    
    def cube(self):
        return self.number**3 
    
    def squreRoot(self):
        return self.number ** 0.5
    

s = calculator(4
               )
print(s.square())
print(s.cube())
print(s.squreRoot())
# OPERATOR OVERLOADI NG IN PYTHON 

'''
Operators in Python can be overloaded using dunder methods. 
These methods are called when a given operator is used on the objects. 
Operators in Python can be overloaded using the following methods:
'''

class Number:
    def __init__(self,n):
        self.n = n
        
    def __add__(self , others):
        return Number(self.n + others.n)
    
    def __len__(self):
        return len(self.n)
    
    def __str__(self):
        return str(self.n)    
        

n= Number(1)
m=Number(2)
o= Number(5)

s = Number("ankit")

print(n+m+o) # Triggers n.__add__(m)
print(len(s))



'''

p1+p2 # p1.__add__(p2) 
p1-p2 # p1.__sub__(p2) 
p1*p2 # p1.__mul__(p2) 
p1/p2 # p1.__truediv__(p2) 
p1//p2 # p1.__floordiv__(p2)

'''

# Other dunder/magic methods in Python: 

'''
__str__() # used to set what gets displayed upon calling str(obj) 

__len__() # used to set what gets displayed upon calling.__len__() or len(obj)
'''


class Employee:   
    a= 1
        
        
class Programmer(Employee):
    b=2
       
class manger(Programmer):
    c = 3
    

obj = Employee()

print(obj.a)
# print(obj.b)    --- giving error like thre is no attribute b in class employee

p = Programmer()
print(p.a)
print(p.b)
# print(p.c)   --- gives an error like thre is no attribute c in class programmer

m = manger()
print(m.a)
print(m.b)
print(m.c)

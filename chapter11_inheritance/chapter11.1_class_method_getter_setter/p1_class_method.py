# @CLASS  METHOD

'''
A class method is a method which is bound to the class and not the object of the class. 
@classmethod decorator is used to create a class method.
'''

@classmethod 
def method(cls,p1,p2):
    pass



class employee:
    a = 1
    @classmethod                       # now this will help to show the class attribute insted of instance atribute
    def show(self):
        print(f"the class atrribute of a is {self.a}")
        
e = employee()
e.a = 34

e.show() 
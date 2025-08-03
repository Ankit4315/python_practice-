import random

class gass:
    def __init__(self, u):
        self.u = u
        # self.c = c 
        
    def chal(self):
        c = random.randint(1,2)
        if self.u > c:
            print("lower")
        elif self.u < c:
            print("higher")
        else:
            print(f"number is {c} you choss {self.u}")
            

u = int(input("enter a number :- "))
g = gass(u)
g.chal() 
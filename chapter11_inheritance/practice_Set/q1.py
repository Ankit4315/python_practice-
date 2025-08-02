# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class towDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")
        

class threeDvector(towDvector):
    def __init__(self,i ,j ,k):
         super().__init__(i, j)
         self.k = k
         
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
         

o = towDvector(1,3)
o.show()
b= threeDvector(1,2,3)
b.show()
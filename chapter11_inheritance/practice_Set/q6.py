# 6. Write __str__() method to print the vector as follows: 

#                                  7i + 8j +10k  
# Assume vector of dimension 3 for this problem. 


class vector:
    def __init__(self,i ,j ,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        result = vector(self.i + other.i, self.j + other.j, self.k + other.k)
        return result
    
    def __mul__(self, other):
        result = self.i * other.i + self.j * other.j + self.k * other.k
        return result
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    

v1 = vector(1, 2, 3)
v2 = vector(1, 2, 3)
v3 = vector(1, 2, 3)

print(v1 + v2)
print(v1 + v2 + v3)
print(v1 * v2)
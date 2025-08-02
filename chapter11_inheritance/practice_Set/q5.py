# 5. Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them. 

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
        return f"vector ({self.i}, {self.j}, {self.k})"
    

v1 = vector(1, 2, 3)
v2 = vector(1, 2, 3)
v3 = vector(1, 2, 3)

print(v1 + v2)
print(v1 + v2 + v3)
print(v1 * v2)


# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class vector:
    def __init__(self, l):
        self.l = l 
        self.i, self.j , self.k  = l
    
    def __add__(self, other):
        result = vector([self.i + other.i, self.j + other.j, self.k + other.k])
        return result
    
    def __mul__(self, other):
        result = self.i * other.i + self.j * other.j + self.k * other.k
        return result
        
    def __str__(self):
        return f"vector ({self.i}, {self.j}, {self.k})"
    
    def __len__(self):
        return len(self.l)
    


v4 = vector([2, 4, 5])
print(len(v4))

v1 = vector([1, 2, 3])
v2 = vector([1, 2, 3])

print(v1 + v2)
# v3 = vector(1, 2, 3)
# print(v1 + v2 + v3)

print([v1 * v2])
# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 


# NO - clasee attribute is not change


class n():
    a=7
    # def __init__(self, a):
    #     self.a = 7
        
    
    
obj = n()

print(obj.a)  # Print the class attribute because instance attribute is not present

obj.a = 0

print(obj.a)  # print the instance attribute because instance attribute is present

print(n.a)   # print the class attribute becouse we directly accasing
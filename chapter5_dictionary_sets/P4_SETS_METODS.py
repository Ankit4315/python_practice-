s = {1,8,2,3}  

# 1• len(s): Returns 4, the length of the set  
print(len(s))

# 2• s.remove(3): Updates the set s and removes 3 from s. 
print(s.remove(3)) # return non becouse remove dont return anything
print(s)

# 3• s.pop(): Removes an arbitrary(rendom) element from the set and return the element removed. 
print(s.pop())
print(s)

# 4• s.clear():empties the set s. 
s.clear()
print(s)

# 5• s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
a={1,3,4,5,7}
b={3,7,9,5, 10}

print(a.union(b))

# 6• s.intersection({8,11}): Return a set which contains only item in both sets  {8}. 
print(a.intersection(b))


print(a.difference(b))
print(b.difference(a))

print({1,3}.issubset(a)) # true/flase

print(a.issuperset({1,3})) # true/false

 
 
 
 
 
 
 
 

# 3. Check that a tuple type cannot be changed in python.

tup = (1,4)
print(type(tup))
print(id(tup))


tup[0] = 5   # Traceback (most recent call last):  tup[0] = 5
                                             # TypeError: 'tuple' object does not support item assignment
# 5. Write a program to find the maximum of the numbers in a list using the reduce function. 
from functools import reduce

l = [1,5,7,0,8,2,9,10,2,8]

# def grate(a,b):
#     if(a>b):
#         return a
#     return b

grate = lambda a,b: a if a>b else b

print(reduce(grate,l))
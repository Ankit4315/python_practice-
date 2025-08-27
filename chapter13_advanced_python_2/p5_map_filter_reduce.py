# MAP, FILTER  & RE DUCE 

'''
Map applies a function to all the items in an input_list. 
Syntax. 
'''

input_list = [10, 2, 3, 4, 5]
square = lambda X : X*X

sqList = map(square, input_list)
print(list(sqList))
              
              
# Filter creates a list of items for which the function returns true. 
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyenven = list(filter(even ,input_list)) 
print(list(onlyenven))
              
              
# Reduce applies a rolling computation to sequential pair of elements. 
from functools import reduce 

s_um = lambda a,b:a+b

print(reduce(s_um,input_list))

'''
  [10]--[2]--[3]--[4]--[5]
    |    |
    [ 12 ]-- [3]
       |      |
       [  15  ] -- [4]
           |        |
           [   19   ]---[5]
                |        |
                [    24  ]
'''

 
 

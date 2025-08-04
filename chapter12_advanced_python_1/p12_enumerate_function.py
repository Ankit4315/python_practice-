# ENUMERATE FUNCTION IN PYTHON  

'''
The 'enumerat' function adds counter to an iterable and returns it 
'''
# for i,item in list1: 
#     print(i,item)  # Prints the items of list 1 with index 
    
    
    
l = [3, 4, 5, 655]
# index = 0
# for item in l:
#     print(f"the item number at index{index} is {item}")
#     index += 1
    
for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")

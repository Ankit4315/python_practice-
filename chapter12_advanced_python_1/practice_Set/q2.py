# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l= [101,41,24,3,44,54,64,74,84,94,5,58,5,7]


# for index , item in enumerate(l):
#     if(index == 3 or index == 5 or index == 7):
#         print(index)
    
    
for index , item in enumerate(l):
    if(item == 3 or item == 5 or item == 7):
        print(item)
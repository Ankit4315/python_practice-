# LIST COMPREHENSIONS  

'''
List Comprehension is an elegant way to create lists based on existing lists. 
'''

list1 = [1,7,12,11,22,]
list2 = [i for i in list1 if i > 8] 
print(list2)

print("-----------------------------------------**-------------------------")
 
mylist = [1,4,5,8]

squaredList = [i*i for i in mylist]

# for item in mylist:
#     squaredList.append(item*item)

print(squaredList)
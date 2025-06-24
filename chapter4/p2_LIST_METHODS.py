# LIST METHODS.

l1 = [15, 2, 8, 7, 1, 21]
print(l1)
print(id(l1))


# 1• l1.sort(): updates the list to [1,2,7,8,15,21]
l1.sort()
print(l1)
print(id(l1))

# 2• l1.reverse(): updates the list to [15,21,2,7,8,1]
l1.reverse()
print(l1)
print(id(l1))

# 3• l1.append(8): adds 8 at the end of the list
l1.append(8)
print(l1)
print(id(l1))

# 4• l1.insert(3,8): This will add 8 at 3 index
l1.insert(3,8)
print(l1)
print(id(l1))

# 5• l1.pop(2): Will delete element at index 2 and return its value.
print(l1.pop(3))
print(l1)
print(id(l1))

# 6• l1.remove(8): Will remove 8 from the list. (only that element that is come first)
l1.remove(8)
print(l1)
print(id(l1))
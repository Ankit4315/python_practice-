'''
3. A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers. 
                                        7
                                        17
                                        .
                                        .
                                        .
'''

# l = [7,14,21,28,35,42,49,56,63,70]

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)

print(s)
    
    
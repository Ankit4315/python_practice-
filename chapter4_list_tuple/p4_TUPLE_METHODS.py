a = (True ,1, 7, 2, 46, False, False, "ankit", 2, 1, 1)

# • a.count (1): a count (1) will return number of times 1 occurs in a.
n = a.count(0)
print(n) # output is 2 becouse False is 0

n = a.count(1)
print(n) # output is 4 becouse true is condiderd as 1

# • a.index (1) will return the index of first occurrence of 1 in a.

i = a.index(1)
print(i) # output is 0 becouse ture considerd as a 1f

# • len

print(len(a))

# membersship opraters 

print("ankit" in a) # output true 


# unpacking
 
mytup = (1,2,3)

a,b,c = mytup

print(a,b,c)
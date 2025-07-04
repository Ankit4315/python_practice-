# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dictionary = {}

for i in range(4):
    key = input("enter your name :> ")
    value = input("enter your favorite language :> ") 
    # dictionary[key]= value
    dictionary.update({key:value})    #both work same
    
print(dictionary)
    
    
    
    
    
    
    
    
# my_dict = {}
# n = int(input("How many items in the dictionary? "))

# for _ in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     my_dict[key] = value

# print("Your dictionary:", my_dict)

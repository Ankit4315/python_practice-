# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 

# Answer => its update the vaule with the recent one, if the key is same 

dictionary = {}

for i in range(2):
    key = input("enter your name :> ")
    value = input("enter your favorite language :> ") 
    dictionary[key]= value
    # dictionary.update({key:value})    #both work same
    
print(dictionary)
    
# 8. If languages of two friends are same; what will happen to the program in problem 6?

#  answer :> if the langauage is same then matter becouse value of any is anything

dictionary = {}

for i in range(2):
    key = input("enter your name :> ")
    value = input("enter your favorite language :> ") 
    dictionary[key]= value
    # dictionary.update({key:value})    #both work same
    
print(dictionary)
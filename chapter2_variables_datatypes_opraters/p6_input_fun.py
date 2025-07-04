# This function allows the user to take input from the keyboard as a string
# It is important to note that the output of input is always a string (even is a number is entered).

A = input("enter a first no.: ") #5
B = input("enter a second no.: ") #5
print("sum of A and B is > ",A+B) #result is "55" becouse the input function take input as a string from user you need to convert the input explitlly

A = int(input("enter a first no.: ")) #5
B = int(input("enter a second no.: ")) #5
print("sum of A and B is > ",A+B) #result is 10

a= "PRACTICE"
b = a.lower()
print(b)

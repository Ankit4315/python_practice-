# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888” 

name = input("enter a name : - ")
marks = int(input("ente a marks :- "))
phone = int(input("enter a phone :- "))

print("the name of the student is {0}, his marks are {1} and phobne number is {2}".format(name,marks,phone))
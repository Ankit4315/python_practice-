# CLASS  
'''
A class is a blueprint for creating object. 
'''
# Syntax:
 
class Employee: # Class name is written in pascal case Methods & Variables
    pass


class Employee:
    # name = "ankit"
    language = "hindi" # this is class attribuite
    salary = "120000"


# OBJECT 

'''
An object is an instantiation of a class. When class is defined, a template (info) is 
defined. Memory is allocated only after object instantiation. 
Objects of a given class can invoke the methods available to it without revealing the 
implementation details to the user. - Abstractions & Encapsulation! 
'''

obj = Employee()

print(obj.language, obj.salary)


ankit = Employee()
ankit.name = "ankit dhakad"   # this is instance(object)  attribuite
print(ankit.name, ankit.salary, ankit.language)

kana = Employee()
kana.name = "kana kana"
print(kana.name, kana.salary, kana.language)

#  here name is instance attribuite and salary and language are class  attribuites as they are directly belong to class 

# MODELLING A PROBLEM IN OOPS  

'''
We identify the following in our problem. 
• Noun → Class → Employee 
• Adjective → Attributes → name, age, salary 
• Verbs → Methods → getSalary(), increment()
'''


# CLASS ATTRIBUTES  
'''
An attribute that belongs to the class rather than a particular object.
'''


# INSTANCE ATTRIBUTES

''' 
An attribute that belongs to the Instance (object). Assuming the class from the previous 
example: 
harry.name = "harry" 
harry.salary = "30k"  # Adding instance attribute   
 
Note: Instance attributes, take preference over class attributes during assignment & retrieval. <------

When looking up for harry.attribute it checks for the following: 
    1) Is attribute present in object? 
    2) Is attribute present in class?

'''

class Emp():
    lang = "python"
    rate = 50


p1 = Emp()

p1.lang = "javascript"

print(p1.lang, p1.rate)
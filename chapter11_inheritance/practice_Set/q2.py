# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class 'Dog' from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animals:
    def pet():
        print("frindly")
    def forest():
        print("not frinedly")


class pets(Animals):
    print("stay with humnas")


class Dog(pets):
    @staticmethod
    def bark():
        print("barking")
        


d= Dog()
d.bark()
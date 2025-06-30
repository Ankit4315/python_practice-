# 2. Write a python program using function to convert Celsius to Fahrenheit. 

def celToFah(dgree):
    return (dgree * 9/5) + 32

n = int(input("enter a temprature in celsius :> "))
print(celToFah(n))


def fToC(tem):
    return  (tem - 32) * 5/9

tem = int(input("enter a temrature into fahrenheit :> "))
print(fToC(tem))

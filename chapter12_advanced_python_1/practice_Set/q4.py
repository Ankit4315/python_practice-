# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    result = a/b
    print(result)

except ZeroDivisionError as e:
    print("Infinite")
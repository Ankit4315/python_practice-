# 3. Write a program to detect double space in a string.


def detectDouble(str):
    if '  ' in str:
        print("double space detected")
    else:
        print("double space is not detected")
    
str1 = input("enter a string to dectect double space :> ")
detectDouble(str1)    


# def deleteDoubleSpace(str):
#     st = str.replace('  ','')
#     print(st)

# str1 = input("Enter a string with double space :> ")

# deleteDoubleSpace(str1)
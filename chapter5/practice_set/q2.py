# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).


# 1st method
number = input("enter a 8 digit number :> ")
print(number)
se = set(number)
print(se)

# 2nd method

st = set()
def setproblem():
    for i in range(8):
        number = input(f"enter a {i+1} number :> ")
        st.add(number)
    
setproblem()
print(st)

#3rd method 

num = int(input("enter a 8 digit number :> "))
n= set(str(num))
print(n)
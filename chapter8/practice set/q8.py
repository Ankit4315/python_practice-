
# 8. Write a python function to print multiplication table of a given number. 
  
  
  
def muti(n):
    for i in range(1,11):
        print(f"{n} X {i} = {i*n}")
     
     
n = int(input("enter a number :> "))    
muti(n)
# 4. Write a recursive function to calculate the sum of first n natural numbers. 


'''
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4

sum(n) = 1 + 2 + 3 + 4 + ..... + n
sum(n) = sum(n-1) + n
''' 

def nSum(n):
    if(n== 1):
        return 1
    return nSum(n-1) + n

print(nSum(5))
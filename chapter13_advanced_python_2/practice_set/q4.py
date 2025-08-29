# 4. Write a program to filter a list of numbers which are divisible by 5. 

l = [5,10,2,1]

def div5(n):
    if(n%5==0):
        return True
    return False


f = list(filter(div5, l))
print(f)
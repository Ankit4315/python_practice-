def cal(n):
  c = 0
  for i in range(1,n):
    if(i%1!=1 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
      c = c+1
  return c
  
n = int(input("Enter the number:- "))
result = cal(n)
print("answer is:- ", result)
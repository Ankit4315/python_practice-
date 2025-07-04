def mean(a,b):
  m = (a+b)/(a-b)
  print(m)

def grater (a,b):
  if a>b:
    print(f"{a} is grater")
  elif b>a:
    print(f"{b} is grater")
  else:
    print(f"{a} = {b}")

mean(2,3)
grater(13,4)
grater(1,1)
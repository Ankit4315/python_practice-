def add(a,b):
  return print(a+b)

def multi(a,b):
  return print(a*b)

def sub(a,b):
  return print(a-b)

def div(a,b):
  if(b==0):
    return print("not divisibale by zero")
  return print(a/b)

def cal():
  print("select your choise")
  print("for addition. 1")
  print("for subtract. 2")
  print("for division. 3")
  print("dor multipal. 4")
  ch = int(input("enter your choise:- "))

  if ch in [1,2,3,4]:
    a = int(input("enter first no:-"))
    b = int(input("enter second no:- "))
    if(ch==1):
      add(a,b)
    if(ch==2):
      sub(a,b)
    if(ch==3):
      div(a,b)
    if(ch==4):
      multi(a,b)


cal()


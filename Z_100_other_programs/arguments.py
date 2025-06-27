print("positon arguments")
def position (a,b):
  print("avarge is :- ",(a+b)/2)

position(10, 1)
# position(10 ,20 ,20) error

print("\nkeyword arguments")
def keyword (first,second):
  print(first +second)


keyword(first="ankit",second="dhakad")
keyword(second=1, first=2)


print("\ndefault arguments")
def default(a=2,b=4):
  print(a+b)

default()
default(b=3)
default(a=1,b=1)


print("\n variable arguments")
print("\n * stands for tupal")

def variable(*num):
  for i in num:
    print(i)

variable(7,4,4,4,4,)

print("\n ** stands for discnary")

def variaval(**dic):
  print("hello", dic["fname"] ,dic["mname"], dic["lname"])

variaval(fname="ankit",mname="varma",lname="dhakad")
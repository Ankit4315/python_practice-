x = int(input("Enter a number:- "))

match x:
  case 0:
    print("noting")
  case 1:
    print("one")
  case _ if x>1:
    print("greater then one")

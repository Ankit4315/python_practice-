# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''

import time


 
def letter():
    # name = "ank" #local variables has more priority
    # ctime = 13
    letter = f'''Dear {name},
You are selected!
{ctime}'''
    print(letter)


name = input("enter a name:> ")
ctime = time.strftime('%d-%m-%Y')
letter()
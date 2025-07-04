# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

import time
timestam = int(time.strftime('%H'))
print(timestam);

def wish(name):
    if(timestam <= 12 and timestam >=6):
        print('good morning, '+ name)
    elif(timestam > 12 and timestam <= 4):
        print('good afternoon, '+ name)
    elif(timestam > 4 and timestam < 8):
        print('good evining, '+ name)
        

name = input("Enter your name :> ")  
wish(name)
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

with open("poems.txt") as f:
    c = f.read()
    if("twinkle" in c):
        print("present")
    else:
        print("not present")    
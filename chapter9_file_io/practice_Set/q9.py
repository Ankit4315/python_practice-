# 9. Write a program to find out whether a file is identical & matches the content of another file. 

with open("log.txt") as f:
    data = f.read()
    
    
with open("log_copy.txt") as f:
    data1 = f.read()

# with open("poems.txt", encoding="utf-8") as f:
#     data1 = f.read()

if data == data1 :
    print("yes")
else:
    print("no")
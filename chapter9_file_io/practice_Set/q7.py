# 7. Write a program to find out the line number where python is present from ques 6. 

with open("log.txt") as f:
    data = f.readlines()

ln = 1
found = False
for i in data: 
    if("python" in i):
        print(f"yes, on lineno {ln}")
        # break
        found = True
    ln += 1
    
if not found:
    print("no")
        
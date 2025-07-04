# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt") as f:
    data = f.read()

if ("python" in data):
    print("yes")
else:
    print("no")
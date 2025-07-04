# 8. Write a program to make a copy of a text file “log.txt”

with open("log.txt") as f:
    data = f.read()

with open("log_copy.txt", "w") as f:
    f.write(data)
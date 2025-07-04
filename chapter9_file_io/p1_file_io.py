'''
The random-access memory is volatile, and all its contents are lost once a program 
terminates. In order to persist the data forever, we use files. 
A file is data stored in a storage device. A python program can talk to the file by reading 
content from it and writing content to it. 
'''

# TYPE OF FILES.

'''
There are 2 types of files: 
1. Text files (.txt, .c, etc) 
2. Binary files (.jpg, .dat, etc) 
Python has a lot of functions for reading, updating, and deleting files.
'''


# OPENING A FILE 

'''
Python has an open() function for opening files. It takes 2 parameters:  filename and mode. 
'''

# open("filename", "mode of opening(read mode by default)") 

# open("example.txt", "r")


# READ IN FILES

f = open("example.txt")
data = f.read()
print(data)
f.close()

print("----------------------------------------------------------------------------------------------")
# WRITE IN FILS 

st = "amazing"
f = open("myfils.text", "w")
f.write(st)
f.close


# OTHER METHODS TO READ THE FILE.
f = open("example.txt")

'''
data1 = f.readline()
print(data1)
data3 = f.readline()
print(data3)
data4 = f.readline()
print(data4)
'''

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
    


# data2 = f.readlines() # it restuns a list
# print(data2) 
f.close()

 

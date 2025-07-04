# 11. Write a python program to rename a file to “renamed_by_ python.txt. 
 
# with open("old.txt") as f:
#     data = f.read()

# with open("new.txt", "w") as f:
#     f.write(data)

import os

# Rename the file
os.rename("old.txt", "renamed_by_python.txt")

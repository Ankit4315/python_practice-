# WITH STATEMENT  
'''
The best way to open and close the file automatically is the with statement. 
'''

# Open the file in read mode using 'with', which automatically closes the file 


f = open("example.txt")
data = f.read()
print(data)
f.close()

# same can be writen in with statemant

with open("myfils.text", "r") as f: 
    # Read the contents of the file 
    text = f.read() 
 
# Print the contents 
print(text) 
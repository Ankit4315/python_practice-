# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

word = "Donkey"

with open("poems.txt", "r", encoding="utf-8") as f:
    data = f.read()
    
newdata = data.replace(word, '######')

with open("poems.txt", "w", encoding="utf-8") as f:
    f.write(newdata)
# 5. Repeat program 4 for a list of such words to be censored. 
l = ["donkey", "ankit", "dhakad", "kamal", "kisore"]

with open("poems.txt", "r", encoding="utf-8") as f:
    data = f.read()


for i in l:
    data = data.replace(i, "#" * len(i))

with open("poems.txt", "w", encoding="utf-8") as f:
    f.write(data)
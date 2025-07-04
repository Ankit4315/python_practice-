# 7. Write a python function to remove a given word from a list ad strip it at the same time. 

l = ['ankit' , 'vivek', 'arman', 'kamal', 'a']

def rem(l, word): 
    li = []
    for i in l:
        if i != word:
            li.append(i.strip(word))
        else:
            print(i)
    return li

print(rem(l, "a"))
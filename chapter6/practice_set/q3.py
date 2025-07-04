# 3. A spam comment is defined as a text containing following keywords: 
#   “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
#   to detect these spams. 


# method 1


# s1 = 'Make a lot of money'
# s2 = 'buy now'
# s3 = 'subscribe this'
# s4 = 'click this'
# inp = input("enter your commit :> ")
# if((s1 in inp) or (s2 in inp) or (s3 in inp) or (s4 in inp)):
#     print("spam he")
# else:
#     print("safe")


# method 2

spam = ['Make a lot of money','buy now', 'subscribe this', 'click this']
inp = input("enter your commit :> ")

is_spam = False
for i in spam:
    if i in inp:
        is_spam = True
        break
    
if(is_spam is True):
    print("spam hai")
else:
    print("safe")
# 4. What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(s) # it return {'20', 20} becouse 20==20.0 is true 

#  answer is 2

print(len(s))


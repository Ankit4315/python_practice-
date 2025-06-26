# 9. Can you change the values inside a list which is contained in set S?  
#     s = {8, 7, 12, "Harry", [1,2]} 


#  answer :> NO  you can not change the value inside the list contained in the set, in fact you cant not even hava a list as an element in a 
#            set becouse sets in python require all theire elements to be immutable and hased,
#            list are mutable and not hashedble, so they cannot be added to set.


s = {8, 7, 12, "Harry", [1,2]} 

'''
give this error
s = {8, 7, 12, "Harry", [1,2]}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list' 
'''
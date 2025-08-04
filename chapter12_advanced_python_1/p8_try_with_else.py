# TRY WITH ELSE CLAUSE 
'''  
Sometimes we want to run a piece of code when try was successful. 
'''
 
try: 
    # Somecode 
    pass
except: 
    # Somecode 
    pass
else: 
    # Code         # This is executed only if the try was successful
    pass


try:
    a= int(input("enter a num: "))

except Exception as e:
    print(e)
else:
    print("hyee. there")
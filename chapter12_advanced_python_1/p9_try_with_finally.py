# TRY WITH FINALLY  
'''
Python offers a 'finally' clause which ensures execution of a piece of code inspective of 
the exception. 
'''
 
try: 
    # Some Code 
    pass
except: 
    # Some Code 
    pass
finally: 
    # Some Code           # Executed regardless of error!
    pass




# try:
#     a= int(input("enter a num: "))
#     print(a)

# except Exception as e:
#     print(e)
    
# finally:
#     print("hyee. there")
    
    
def main():
    try:
        a= int(input("enter a num: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    
    finally:
        print("hyee. there")
        
main()
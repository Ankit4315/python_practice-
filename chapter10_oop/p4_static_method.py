# Sometimes we need a function that does not use the self-parameter. We can define a static method like this:

'''
@staticmethod   # decorator to mark greet as a static method  
def greet(): 
    print("Hello user") 

'''


class emp:
    lan = "java"
    sal = 10000
    
    def detSal(self):
        print(f"the langage is {self.lan}, salery is {self.sal}")
        
    @staticmethod   #<----
    def greet():
        print("good morning")
    

ankit = emp()
ankit.greet()
ankit.detSal()   #<----- this converts like this emp.detSal(ankit)
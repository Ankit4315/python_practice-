# self refers to the instance of the class. It is automatically passed with a function call from an object


class emp:
    lan = "java"
    sal = 10000
    
    def detSal(self):
        print(f"the langage is {self.lan}, salery is {self.sal}")
        
    def greet(self):
        print("good morning")
    

ankit = emp()
ankit.greet()
ankit.detSal()   #<----- this converts like this emp.detSal(ankit)
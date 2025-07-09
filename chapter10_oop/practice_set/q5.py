# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 


from random import randint

class train():
    
    def __init__(self,tatinNo):
        self.tatinNo =tatinNo
        
    def ticket(self, fr, to):
        print(f"ticket is booked in {self.tatinNo} from {fr} to {to}")
        
    def status(self, fr, to ):
        print(f"train no. {self.tatinNo} is running from {fr} to {to} on time" )
        
    def fare(self, fr, to):
        print(f"ticket fare for train {self.tatinNo} from {fr} to {to} is {randint(200, 500)}")
        


t= train(81254888)
t.ticket("shivpuri", "bhopal")
t.status("shivpuri", "bhopal")
t.fare("shivpuri", "bhopal")
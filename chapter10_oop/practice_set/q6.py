# 6. Can you change the self-parameter inside a class to something else (say “change”). 
# Try changing self to “slf” or “change” and see the effects. 

# answer :> NO - nothing will chnage but for better readabilty use self


from random import randint

class train():
    
    def __init__(slf,tatinNo):
        slf.tatinNo =tatinNo
        
    def ticket(change, fr, to):
        print(f"ticket is booked in {change.tatinNo} from {fr} to {to}")
        
    def status(slf, fr, to ):
        print(f"train no. {slf.tatinNo} is running from {fr} to {to} on time" )
        
    def fare(slf, fr, to):
        print(f"ticket fare for train {slf.tatinNo} from {fr} to {to} is {randint(200, 500)}")
        


t= train(81254888)
t.ticket("shivpuri", "bhopal")
t.status("shivpuri", "bhopal")
t.fare("shivpuri", "bhopal")
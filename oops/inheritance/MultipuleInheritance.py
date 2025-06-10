#mul parent 1 child
class Country:
    def __init__(self):
        self.name = "INDIA"
        self.x=100
        print("country class const called....")
    
    def payGST(self):
        print("payGST called....")    

class State:
    def __init__(self):
        self.name = "GUJARAT"
        self.y=200
        print("state class const called...")
        
    def payTAX(self):
        print("pay tax called...")    

class City(State,Country):    
    
    def __init__(self):
        super().__init__()
        print(f"name ={self.name} ")
        print(f"x = {self.y}")
    
    def pay(self):
        self.payGST()
        self.payTAX()    


city = City()        
city.pay()

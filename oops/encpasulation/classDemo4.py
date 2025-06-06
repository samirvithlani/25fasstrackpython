class Bank:
    
    def __init__(self):
        print("bank class const called...")
        self.name ="SBI"
        self.IFSC = "SBIN007"
     
    def detail(self):
        print(f"name of bank = {self.name}")
        print(f"IFSC OF  {self.name} = {self.IFSC}")    


SBI = Bank()   #constructor call..  
SBI.detail()   

HDFC = Bank()
HDFC.detail()

class Bank:
    
    def __init__(self,name,ifsc):
        print("bank class const called...")
        self.name =name
        self.IFSC = ifsc
     
    def detail(self):
        print(f"name of bank = {self.name}")
        print(f"IFSC OF  {self.name} = {self.IFSC}")    


SBI = Bank("SBI","SBIN007")   #constructor call..  
SBI.detail()   

HDFC = Bank("HDFC","HDFC007")
HDFC.detail()

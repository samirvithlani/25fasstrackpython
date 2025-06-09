class India:
    
    def __init__(self):
        self.country = "INDIA"
        print("india class default const called...")
    
    def indian(self):
        print("indian method called....")    


class Gujarat(India):
    
    def __init__(self):
        super().__init__() #invoking India class const...
        self.state = "Gujarat"
        print("Gujarat class COnst callled...")        
    
    def Gujarati(self):
        print("Gujarati method called...")    
        print(f"Country name = {self.country}")


class Ahmedabad(Gujarat):
    
    def __init__(self):
        super().__init__() #invoking gujarat class const...
        self.city = "Ahmedabad"
        print("Ahmedabad class const called,,,")
    
    def Ahmedabadi(self):
        print("ahmedabdi method called...")        
        print(f"country name = {self.country} state name  = {self.state}")


a = Ahmedabad()        
a.Gujarati()
a.Ahmedabadi()
        
    
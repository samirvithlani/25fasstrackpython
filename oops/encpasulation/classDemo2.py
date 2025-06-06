class City:
    
    def printCityName(self,name):
        print(f"City name = {name}")
        print(f"city NAme from self = {self.cityName}") #ahm.cityName
    
    def displayCity(self):
        print(f"display city called...")
        self.cityName = "AHMEDABAD" #Mumbai.cityName = "AHMEDABAD"
            



ahm = City()
ahm.printCityName("Ahmedabad")        #printCityName(ahm) address1

mumbai = City()
mumbai.displayCity() #displayCity(mumbai) --> address2
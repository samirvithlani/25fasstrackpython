class Univericity:
    uniName ="GUJARAT TECH UNI" #class level variabel...
    
    def __init__(self,collageName):
        #instancevariable  = localv
        self.collageName = collageName
    
    def printData(self):
        print(f"{self.collageName} collage is register under uni {Univericity.uniName} ")    



GLS = Univericity("GLS")        
GLS.printData()

LD = Univericity("LD")
LD.printData()
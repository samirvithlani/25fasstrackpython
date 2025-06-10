class Book:
    def __init__(self,pages): #b1 = 100 , b2= 200
        self.pages = pages
        
    def __add__(self,other): #self b1 other b2
        print(f"self {self.pages}") #b1.pages = 100
        print(f"other {other.pages}")#b2.pages = 200
        #return Book(self.pages + other.pages)
    def __sub__(self,nextobj):
        return self.pages - nextobj.pages    
    
    #truediv
    #flordiv


b1 = Book(100)  #param const      
b2 = Book(200)

b3 = b1+b2 # __add__(self,other)

b4 = b1 - b2 #__sub__(b1,b2)
print(b4)
    
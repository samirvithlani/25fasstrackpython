class Circle:
    pi = 3.14 #class level variable
  
    @staticmethod  
    def area(r):
        return Circle.pi * (r*r)


# c = Circle()
# c.area(1)    

x =Circle.area(10)
print(x)
    
        
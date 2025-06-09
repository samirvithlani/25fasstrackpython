class Parent:
    
    def parentFunction(self):
        print("parent class funciton called...")


#inheriance
class Child(Parent):
    
    def childFunction(self): # Child...
        print("child class function called...")
        self.parentFunction()        #child object



# p = Parent() #default...
# p.parentFunction()     

c = Child()
c.childFunction()   
c.parentFunction()
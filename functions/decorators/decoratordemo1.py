
#hof
def order_food(func): #3
      #func ==   throw_party
    
    def inner(): #5
        print("ordering food") #6
        func() #7 throw_party()
    
    return inner  #4  
    
    

@order_food #2
def throw_party(): #8
    print("throw party function called...") #9


throw_party()   #1  
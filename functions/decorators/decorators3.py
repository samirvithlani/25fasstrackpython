
def order_food(func):
    
    
    def inner(noofpersons):
        print(noofpersons)
        func(120) #throw_party()
    
    
    return inner
    

@order_food
def throw_party(persons):
    print("throwing party...",persons)



throw_party(100)    
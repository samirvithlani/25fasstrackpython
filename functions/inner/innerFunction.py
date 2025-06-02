def outer():
    print("outer function called..")
    def inner():
        print("inner function called...")
    inner() #calling part...


outer()    
        
        
def checkData(**kwargs):
    try:
        for i in kwargs.values():
            if type(i).__name__!="str":
                raise TypeError("all key must be string")
    except TypeError as e:
        print(f"{e}")
    else:
        print(kwargs)    

checkData(ram=22,shyam=22,ajay=100)        
                    
        
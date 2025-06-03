def isValid(func):
    
    #royal
    #a
    #data = "ahmedabdad"
    #query = "x"
    def inner(data,query):
        flag = False
        if query in data:
            flag = True
            
        
        if flag:
            func()
        else:
            print("string is not valid...")        
    
    return inner

@isValid
def getData():        
    print("data is valid...")


getData("royal","x")    
        

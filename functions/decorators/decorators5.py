def isValid(func):
    def inner(data,query):
        flag = False
        if query in data:
            flag = True
            
        
        if flag == True:
            func(data) #getData(data)
        else:
            print("string is not valid...")        
    
    return inner

@isValid
def getData(data):        
    print("data is valid...",data)


getData("royal","l")    
        

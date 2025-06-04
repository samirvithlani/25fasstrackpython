
def validate(func):
    
    def inner(*args):
        flag =True
        for i in args:
            if type(i) != int:
                flag = False
                break
        
        if flag == True:
            result = [i**2 for i in args]
            func(*result)
        else:
            print("All arguments must be integers...")            

    return inner


@validate
def getData(*args):
    print("data is valid...",args)

getData(1, 2,"ok", 3, 4)    
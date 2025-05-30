def goa(name):
    print("goa funtion called...")
    return "KAJU"

def dubai(name):
    print("dubai function called..")
    return "KHAJUR"

def kashmir(name):
    print("kashmir function called...")
    return "shindoor"




def trip(cb):
    print("trip function called...")
    x = cb("ram") #function call...
    print("x",x)



budget = int(input("enter budget"))
if budget>60000:
    trip(kashmir)
elif budget>50000:
    trip(goa)    
elif budget>10000:
    trip(goa)
    
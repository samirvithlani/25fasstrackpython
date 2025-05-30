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
    return cb("ram")


data = None
budget = int(input("enter budget"))
if budget>60000:
    data = trip(kashmir) #shi
elif budget>50000:
    data = trip(goa)    
elif budget>10000:
    data = trip(goa)

print("data =",data)    
    
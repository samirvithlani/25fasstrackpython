def commerce(name):
    print(f"{name} has taken admission in commerce")
    
def arts(name):
    print(f"{name} has taken admission in arts")

def science(name):
    print(f"{name} has taken admission in science")


#cb call back...
def admission(cb,name):
    #cb == commerce
    print("admission function called....")
    #cb("ram") #commerce arts sciecnr 
    cb(name)
    #commerce


#admission(commerce)    
name = input("enter name :")
pers = float(input("enter your pers :"))
if pers>80:
    admission(science,name)
elif pers>70:
    admission(commerce,name)    
else:
    admission(arts,name)    
    
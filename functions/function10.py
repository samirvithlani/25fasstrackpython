
def commerce():
    print("user has taken admission in commerce")
    
def arts():
    print("user has taken admission in arts")

def science():
    print("user has taken admission in science")



#cb call back...
def admission(cb):
    #cb == commerce
    print("admission function called....")
    cb() #commerce arts sciecnr 
    #commerce


#admission(commerce)    
pers = float(input("enter your pers"))
if pers>80:
    admission(science)
elif pers>70:
    admission(commerce)    
else:
    admission(arts)    
    
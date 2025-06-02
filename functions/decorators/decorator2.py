
def loginRequired(func):
    def inner():
        name = input("enter name :")
        role = input("enter role : ")
        
        if name =="MANAGER" and role =="MANAGER":
            func()
        else:
            print("user is not valid....")    

    return inner

@loginRequired
def access_data():
    print("user is accessing data...")


access_data()    
def login_system(username,password):
    
    def validate_user():
        #20 line code
        return username == "ADMIN" and password == "ADMIN"
    
    valid = validate_user() #true false
    if(valid):
        print("user is valid")
    else:
        print("user is not valid...")


login_system("ADMIN","ADMIN")            
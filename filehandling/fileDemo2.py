# write mode : openn --data over....
# write mode : if file not exist ... create -- write if file exist overri..

# with open("./filehandling/ex1.txt","w") as file:
#     file.write("this is example run again.......")
    
    
with open("./filehandling/ex1.txt","a") as file:
    file.write("this is example run again.......")
    

users = ['ram',"shyam","amit","sumit","ajay","jaya"]
with open("./filehandling/users.txt","a") as file:
    file.writelines(users)
    
        
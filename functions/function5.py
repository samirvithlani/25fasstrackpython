#key word arguments

def getUserDetail(name,age,email,status):
    print(f"Name = {name} age = {age} email = {email} status = {status}")



#getUserDetail("ram","ram@gmail.com","23",True)    
getUserDetail(name="ram",email="ram@gmail.com",status=True,age=22)



def getStudentData(*args,x):
    print("args",args)
    print("x ",x)
    

getStudentData("ram","shyam","amit","jay",x="principal")    

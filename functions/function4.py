def getUsers(user):
    print(user)


getUsers("raj")    
getUsers(["raj","parth","amit","sumit"])

#args
def getStudents(*args):
    print(args)

getStudents()    
getStudents("raj","parth","amit","sumit")
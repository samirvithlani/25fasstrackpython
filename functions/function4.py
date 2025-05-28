def getUsers(user):
    print(user)


getUsers("raj")    
getUsers(["raj","parth","amit","sumit"])

#args
def getStudents(*args):
    print(args)

getStudents()    
getStudents("raj","parth","amit","sumit")

# def test(*args,x):
#     print(args)
#     print(x)

def test(x,y,*args):
    print(args)
    print(x)


test(100,20,30,40)    
# def add(a,b):
#     print("add function called,,")
#     return a + b 


def add(a,b)->str:
    print("add function called,,")
    return a + b 

ans = add(100,20)
print("ans = ",ans)
print("ans = ",add(100,1000))
print("ans = ",add("ram","shyam"))
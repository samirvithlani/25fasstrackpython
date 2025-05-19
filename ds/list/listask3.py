data =["ram","shyam","ram","seeta","seeta","ajay"]
uniqueElm = []
duplicate=[]



#data =["ram","shyam","ram","seeta","seeta","ajay"] 
#duplicate elem
#out["ram","seeta"]

#room1 --> room2
#5 toys --> car
#2 toy ---> ball
#3 toy --> car []

for i in data:
    #ram -->
    #shaym
    #ram
    #seeta
    #seeta
    if i not in uniqueElm:
        uniqueElm.append(i) #ram shyam seeta
    else:
        duplicate.append(i) #ram seeta
            

print(uniqueElm)        
print(duplicate)
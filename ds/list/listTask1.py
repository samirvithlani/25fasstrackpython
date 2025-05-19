data = [1,2,3,4,5,67,7,8,8]
evenList=[]
oddList=[]

for i in data:
    if i %2==0:
        evenList.append(i)
    else:
        oddList.append(i)    

print(evenList)        
print(oddList)
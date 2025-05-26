# data =set({})
# print(data)

data = {10,20,30,90,40,50,60,10,30}

print(data)
print(type(data))

#print(data[0])

data.add(500)
data.update({77,66,55,44}) #extend
#data.update("java")


#remove...

#data.clear() --> clear set --
removedElm = data.pop() #len check ...
print("removing...",removedElm)

data.remove(60)
#data.discard(600)

print(data)



# for i in data:
#     print(i)
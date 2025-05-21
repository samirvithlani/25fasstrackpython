#data = {}
data = {"Gujarat":"Gandhinagar","Bihar":"Patna","UP":"Lucknow"}
print(data)
print(type(data))

print(data["Gujarat"]) #

data["WB"] = "Kolkatta" #at time one key value pair add...
data["Gujarat"] = "Ahmedabad"

#add multipule data

data.update({"Tamilnadu":"chennai","punjab":"Chandigadh","Gujarat":"Gandhinagr"})

#keys
k = data.keys()
print(k)
v = data.values()
print(v)

kv = data.items() #[(k,v),(k,v)]
print(kv)

for i ,j in data.items():
    print(i,j)
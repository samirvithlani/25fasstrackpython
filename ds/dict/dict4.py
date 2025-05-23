data = {"opsindoor":["PM","HOME MIN","DEF","AIR FORCE","ARMY","NEAVY"],"URI":["PM","HOME MIN","ARMY"]}

print(data)
print(data["opsindoor"])

opsindoor = data["opsindoor"] #["".""."."]

# for i in opsindoor:
#     print(i)
    
for i,j in data.items():
    print(i,end=" ") #    j = list
    for x in j:
        print(x,end=" ")
    
    print()    
    
name = input("enter name")
convertedName = ""

for  i in name:
    if " " not in i:
        convertedName+=i

print(convertedName)        
        
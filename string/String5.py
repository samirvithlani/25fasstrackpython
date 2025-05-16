name = input("enter name")
char = input("enter chr")
flag = -1

#
for i in range(len(name)):
    #name[i] = j
    #name[1] = a
    if name[i] == char:
        flag = i #i =1
        break
        

print(char," found at index ",flag)    
        

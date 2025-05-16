name = input("enter name")
count =0
for i in name:
    if " " in i:
        count+=1

print(count)    
print("words ",count+1)    
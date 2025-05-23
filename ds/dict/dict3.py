#no type key
#no type value {1:100,2:201}

#{1:100,2:22,3:44}


data = {1:100,2:34,3:23,4:121,5:44}
filtDict ={}

for i,j in data.items():
    if j %2 ==0:
        filtDict[i]=j

print(filtDict)        


#{"string":"string"}
#{either it starts with 's' or having len >5 or palindrome}

data = {"cricket":"seema","football":"dharmaraj","rugby":"sus","volleyball":"het"}

data1={}
for i ,j in data.items():
    if j.startswith("s") or len(j)>5 or j ==j[::-1]:
        data1[i]=j

print(data1)        
        



# result = find_pairs([1, 2, 3, 4, 5, 6], 7)
# print(result)  # Output: [(3, 4), (2, 5), (1, 6)]

def find_pair(data,target):
    pairs=[] #empty list
    for i in range(0,len(data)): # 2 #3
        for j in range(i+1,len(data)): #4
            if data[i] + data[j] == target:  #2+3,2+4,2+5,
                pairs.append((data[i],data[j])) #[(1,6),(2,5),(3,4)]
    
    return pairs            

x = find_pair([1,2,3,4,5,6],5)       
print(x)
                
                
            
        
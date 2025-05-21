sales = ([10,20],[12,22],[10,12],[34,56],[100,200],[90,76],[90,90])
avgSales=[]
for i,j in sales:
    avg = (i + j) //2
    avgSales.append(avg)


print(avgSales)    

maxvalue = max(avgSales)
print("max value...",maxvalue)

ind = avgSales.index(maxvalue)
print("index ",ind+1)


d = (10,20,30)    
maxvalue1 = max(d)
print(maxvalue1)

d1 = ("ram","shyam","amit","hariram","ajay")

#maxvalue2 = max(d1,key=len)
maxvalue2 = max(d1)
print(maxvalue2)



    
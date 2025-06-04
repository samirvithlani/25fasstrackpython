data1 = [1,2,3]
data2 = [4,5,6]

#[5,7,9]

ans = list(map(lambda x,y : x+y, data1,data2))
print(ans)

firstName = ["ram","shyam","mohan"]
lastName = ["sharma","shukla","patel"]

fullName = tuple(map(lambda x,y : x+" "+y,firstName,lastName))
print(fullName)
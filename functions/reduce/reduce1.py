from functools import reduce

data = [i for i in range(11)] #list...

ans = reduce(lambda x,y : x+y, data)
# x = 0 ,y =0 = 0
# x = 0 ,y =1 = 1
# x = 1 ,y =2 = 3
# x = 3 ,y =3 = 6
print(ans)

# sum = 0
# for i in data:
#     sum += i

# print(sum)    
    


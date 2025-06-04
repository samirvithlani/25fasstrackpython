#1to10 numbers square -> 30

nums = range(1,11)

#ans = filter(lambda x: x>30,nums)
ans = filter(lambda x: x>30,map(lambda x: x**2,nums))
#filter(lambda x: x>30,[1,4,9,.....]]))
print(list(ans))


data = ["amit","sumit","jay","raj","parth","kunal","smit","sanjay"]

ans1 = filter(lambda x : x.startswith('S'),map(lambda x: x.upper(),data))
print(list(ans1))

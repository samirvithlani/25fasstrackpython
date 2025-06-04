numbers = [1,2,3,4,5,6,7,8,9,10]
# x = [i for i in numbers if i%2==0]
# print(x)
x = filter(lambda x: x%2==0,numbers)
print(list(x))


data = ["amit","sumit","jay","",None,"raj","parth",None,"kunal","smit","sanjay"]
x1 = filter(lambda x: x and len(x)>4, data)
print(list(x1))
x2 = filter(lambda x: x and x.startswith('s'),data)
print(list(x2))

x3 = filter(lambda x: x,data)
print(list(x3))
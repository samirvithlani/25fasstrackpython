numbers = [1,2,3,4,5]
#[odd,even,odd,even,odd]

x =["even" if i %2 ==0 else "odd" for i in numbers]
print(x)

data = ["ram","","shyam",None,"amit"]

x1 = [i for i in data if i]
print(x1)

numbers =[-1,-2,-3,1,2,3]

x2 = ["positive" if i >0 else "neg" for i in numbers]
print(x2)
import random
x = random.random() #0 to 1
#print(x)

x1 = random.randint(1,100)
#print(x1)

x2 = random.uniform(1,10)
#print(x2)

data = ["ram","shyam","amit","sumit"]
#name = random.choice(data)
#print(name)

#print(random.choice([1,2,3],k=4))

random.shuffle(data)
print(data)

#random.seed(1)
print(random.randint(1,100))

name=  ""
for i in range(1,6):
    x = chr(random.randint(97,122))
    name = name+x

#print(name)    

data = [chr(i) for i in range(97,123)]
#print(data)
name1=""
for i in range(1,6):
    name1 += random.choice(data)

    
    

print(name1)    

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

random.seed(1)
print(random.randint(1,100))



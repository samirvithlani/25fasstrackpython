user1 = {"ram","shyam","amit","sumit","ajay"}
user2 = {"ram","shyam","amit","kunal","parth"}

x = user1.union(user2) #
print(x)

x = user1.difference(user2) #
print(x)

x = user1.intersection(user2)
print(x)

x= user1.issuperset(user2) #
print(x)

x = user1.issubset(user2) #
print(x)

x = user1.symmetric_difference(user2)
print(x)

x = user1.isdisjoint(user2)
print(x)


days = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday"}
print(days)

removedValue = days.pop(2) #tuesday
print("removing...",removedValue)
print(days)


x = days.popitem()
print("removing...",x)
print(days)


print(days.get(1))
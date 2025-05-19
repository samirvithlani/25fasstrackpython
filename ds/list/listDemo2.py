sales =[100,23,45,678,900,333,234,765]
#sales=[]
print(sales)
removedelm = sales.pop() #last index if list empty IndexError: pop from empty list
#removedelm = sales.pop(3) #specif index IndexError: pop index out of range
print("removing...",removedelm)
print(sales)


#remove...

sales.remove(900)
print(sales)
# for i in sales:
#     print(i)

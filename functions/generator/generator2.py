numbers  = [1,2,3,4,5,6,7,8,9,0,10,11,22,3,4,56,7,33,2,22,5,6,54,33,3]

def even_numbers(data):
    for i in data:
        if i %2 ==0:
            yield i

x = even_numbers(numbers)            
# print(next(x))
# print(next(x))
# print(next(x))

for i in x:
    print(i)
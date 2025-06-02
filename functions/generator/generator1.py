# def my_fun():
#     return 1
#     return 2


# x = my_fun()
# print(x)


def my_fun():
    yield 1 #-->
    yield 2 #-->2
    yield 3
    yield 4
    yield 5


gen = my_fun()
for i in gen:
    print(i)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

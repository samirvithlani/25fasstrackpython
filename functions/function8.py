def greet(name):
    return f"Hello {name}"


x = greet #()* no ()

#message  = greet("MS")
message = x("VIRAT") #function
print(message)
print(x("MS"))
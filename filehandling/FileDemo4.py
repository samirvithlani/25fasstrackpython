#read mode...
# with open("./filehandling/emp.txt","r") as file:
#     data = file.read()
#     print(data)


# with open("./filehandling/emp.txt","r") as file:
#     data = file.readline()
#     data1 = file.readline()
#     print(data)  
#     print(data1)  

# with open("./filehandling/emp.txt","r") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())


# with open("./filehandling/emp.txt","r") as file:
#     for data in file:
#         print(data.strip())


#readlines
# with open("./filehandling/emp.txt","r") as file:
#     lines = file.readlines()
#     print(lines)
    
with open("./filehandling/emp.txt","r") as file:
    data = file.read(10)
    print(data)    
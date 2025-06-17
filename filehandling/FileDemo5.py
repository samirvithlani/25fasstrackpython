with open("./filehandling/python.txt","r") as file:
    print("pos of cur :",file.tell())
    print(file.read(5))
    file.seek(0)
    print(file.read(5))
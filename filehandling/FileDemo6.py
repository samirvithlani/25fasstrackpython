with open("./filehandling/mydata.txt","r") as file:
    header_p = False #false...
    while True:
        position = file.tell() #curr pos...
        print(position)
        line = file.readline()
        
        if not line:
            break
        
        if line.startswith("Header"):
            if not header_p:
                print("Keeping Heder",line.strip())
                header_p = True
            else:
                print("skiiping header")
                file.seek(file.tell())    
        else:
            print(line.strip())        
with open("./filehandling/userdata.txt","a") as f:
    while True:
        name = input("enter name (or type exit for exit) :")
        if name == "exit":
            break
        
        num1 = int(input("enter no 1"))
        num2 = int(input("enter no 2"))
        total = num1 + num2
        f.write(f"{name}:{total}")

#prodct name : 
#prodyct price:
    
#product: pen
#price : 100
#--------------    
#product: pencil
#price : 200

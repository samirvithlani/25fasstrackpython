chatroom = set({})
# data =[]
# x ={}
# tup =()
while True:
    choice = int(input(f"1. Join Chat \n2. Leave Chat \n3. Show Active Users 4. Exit\nEnter your choice (1-4):"))
    
    match choice:
        case 1:
            name = input("enter name")
            if name in chatroom:
                print(f"{name} is already taken or {name} already joined ")
            else:
                chatroom.add(name)
        case 2:
            name = input("enter name from exit chat room")
            if name in chatroom:
                chatroom.remove(name)
                print(f"{name} exited chat room successfully !")
            else:
                print(f"{name} is not in this chat room")    
        
        case 3:
            print("active users in chat room are:")        
            for i in chatroom:
                print(i)
        case 4:
            break
        
        case _:
            print("invalud choice!!")
            break
                    
                        
            
    
    
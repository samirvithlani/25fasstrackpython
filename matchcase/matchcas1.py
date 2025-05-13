'''

switch(choice){
    
    case 1:
    break;
    
}
'''

print(" enter 1 for add \n enter 2 for sub \n enter 3 for div \n enter 4 for mul")
choice = int(input()) #typecast..

match choice:
    case 1:
        ans = 10 + 20
        print("add = ",ans)
    case 2:
        ans = 10 - 20
        print("sub = ",ans)
    case 3:
        ans = 10 / 20
        print("div = ",ans)        
    case 4:
        ans = 10 * 2
        print("mul = ",ans)    
    case _: #default..
        print("invalid choice..")    
            
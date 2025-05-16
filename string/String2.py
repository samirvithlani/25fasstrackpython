name = input("enter name")
upperName = ""

#97 a 65 A
#32
#a mit
#97-32 - 65
for i in name:
    #                        97 - 32 = chr(65) ="A"
    #                        65 -32 = chr(33) = "!"
    # "" = ""+A "A"
    # "A" = "A"+"M" "AM"
    if ord(i)>=97 and ord(i)<=122: #"small"
        upperName = upperName + chr(ord(i)-32)
    else:
        upperName = upperName + i    

print(upperName)    
    

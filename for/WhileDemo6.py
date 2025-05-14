a = int(input("enter no 1"))
b = int(input("enter no 2"))
#4 6
#b!=0
while b!=0:
    #temp =6
    #temp =4
    #temp=2
    temp = b
    #b = 4 % 6 =4
    #b =6 % 4 =2
    #b =4 %2 = 0 
    b = a % b
    #a =6
    #a =4
    #a =2
    a = temp

print("a",a)    
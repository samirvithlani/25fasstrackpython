no = int(input("enter no to check armstrong or not ::"))
digits =0
temp1 = no
temp2 = no

while temp1>0:
    temp1 = temp1 //10
    digits+=1

print("no of digits",digits)    

rem=0
sum=0
while temp2>0:
    rem = temp2 % 10
    sum = sum +(rem**digits)
    temp2 = temp2 // 10

print(sum)
if sum == no:
    print("armstrong no..")    
else:
    print("not armstrong no ...")    
    


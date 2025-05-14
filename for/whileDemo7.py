a = int(input("enter no 1 :"))
b = int(input("enter no 2 :"))
min =0
if a<b:
    min =a
else:
    min= b    

hcf = 0
#1 4
for i in range(1,min+1):
    # 4 % 1 ==0 and 6 %1 ==0
    # 4 % 2 ==0 and 6 %2 ==0
    # 4 %3
    #4 %4 and 6%4
    if a %i ==0 and b %i ==0:
        hcf =i #1 ,2

print("hcf = ",hcf)            
    
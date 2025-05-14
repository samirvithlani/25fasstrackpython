#lcm of 2 no

no1 =int(input("enter no1 :")) #10
no2 =int(input("enter no2 :")) #15

max =0
# 10 > 15
if no1>no2:
    max = no1
else:
    max = no2

#max = 15
lcm=0    
while True:
    # 15 % 10 ==0 and 15 %15 ==0
    # 16 % 10 ==0 and 16 %15 ==0
    # 17 % 10 ==0 and 17 %15 ==0
    # 25 % 10 ==0 and 25 %15 ==0
    # 30 % 10 ==0 and 30 %15 ==0
    if (max %no1==0) and (max %no2==0):
        lcm = max # 30
        break
    max+=1 #16

print("lcm of 2 no ",lcm)    
                

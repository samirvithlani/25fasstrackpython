#no1 = 0,no2=1
# 0 1
no1 =0
no2 =1

print(no1,no2,end=" ")
for i in range(1,10):
    #sum = 1 + 1 =2
    #sum = 1 + 2 =3
    #sum = 2 + 3 =5
    sum = no1 + no2
    print(sum,end=" ") #1 2 3 5
    #no1 = 0,#no2 =1
    no1 = no2 # no1 =2
    no2 = sum # no2 =3
    
    
    
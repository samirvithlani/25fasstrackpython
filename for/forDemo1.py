#1 to 10 using range()

#i++
#1 #2 #3
# for i in range(1,11):
#     print(i)

# 0 --> n-1
#increment part default +1
# for i in range(11):
#     print(i,end=" ")

#1 +3 
# for i in range(1,26,3):
#     print(i,end= " ")

for i in range(10,0,-1):
    print(i,end=" ")


#first task
#get 2 numbers from user    
#sp and ep : 1 20 print sum of that n
#and sum of number


sp = int(input("enter sp :"))
ep = int(input("enter ep :"))
sum =0

#1,10
for i in range(sp,ep+1):
    #1 2 3
    print(i,end=" ")
    #0 = 0 +1 =1
    #1 = 1 + 2 =3
    #3 = 3 + 3 = 6
    #6 = 6 +4 =10
    sum = sum + i

print("ans = ",sum)    

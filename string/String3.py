name = input("enter name")
revName = ""

#j a v a -4
#0 1 2 3
for i in range(len(name)-1,-1,-1):
    revName = revName + name[i]

if name == revName:
    print("palindrome")    
else:
    print("not palindrome..")    
    
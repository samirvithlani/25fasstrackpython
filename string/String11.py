data = "ahmedabad"
#x = data[::]
#x = data[1:3]
#x = data[1:6:2] #hea 1 skip
#x = data[::-1]# ahmedabad dabademha
#x = data[4::-1] # ahmedabad
x = data[1:1]
print(x)

name = input("enter name")

if name == name[::-1]:
    print("name is palindrome..")
else:
    print("name is not palindrome..")    

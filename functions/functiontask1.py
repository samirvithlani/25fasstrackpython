def findMax(*args):
    return max(args)


ans = findMax(100,1000,33,45,67,89)
print("ans = ",ans)

# create function which accept 2 parm first is threshold and second is args 
# eg 10,10,100,9,70,65,0


def filter_data(th,*args):
    return [i for i in args if i>th]


print(filter_data(10,90,67,89,100,1,2,3,4,67,6,5,4,1))


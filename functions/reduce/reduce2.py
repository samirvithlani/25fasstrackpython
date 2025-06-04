from functools import reduce

nums = [10,20,33,45,67,0,19]

maxno = reduce(lambda x,y : x if x>y else y, nums)
print(maxno)

#{k:v for i in iterableobject}

#{0:0,1:1,2:4,3:9,4:16}

data = {i:i**2 for i in range(6)}
print(data)

#{a:97,b:98}

alpha = {chr(i):i for i in range(97,123)}
print(alpha)

alphalist = ["a","b","c","X","E","f","g","h"]
alpha1 = {i : ord(i) for i in alphalist}
print(alpha1)

numbers = [i for i in range(1,100)]
#print(numbers)

filtdata  ={i : i for i in numbers if( (i%3 == 0 or i%5 ==0) and (i%2==0))}
print(filtdata)



#task
#names =["naman","racecar","amit","raj","bob"]
#{"naman":"yes","racecar":"yes","amit":"no"}
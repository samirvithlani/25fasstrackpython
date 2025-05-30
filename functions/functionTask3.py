def sumofnumbers(*args):
    sum =0
    for i in args:
        if type(i).__name__ =='int':
            sum+=i
    
    return sum        
             
    

print(sumofnumbers(10,20,"java","ok","90",True))
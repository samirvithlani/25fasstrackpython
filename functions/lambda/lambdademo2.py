users = ["ram","shyam","bob","madam","naman"]

#x == list
def checkPalindrome(x):
    flag = True
    for i in x:
        if i != i[::-1]:
            flag = False
    
    return flag        
            
    


test = lambda x: checkPalindrome(x)
print(test(users))
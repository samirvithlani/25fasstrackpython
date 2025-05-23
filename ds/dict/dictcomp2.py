ascii_char ={char:chr(char) for char in range(97,123)}
print(ascii_char)

#list
fruits =["apple","banana","watermelon","kiwi"]
#{apple:5}

fruits_len = {f:len(f) for f in fruits}
print(fruits_len)

alpha = ["A","B","C","D","a","E"]

char_ascii = {i: ord(i) for i in alpha}
print(char_ascii)

#["madam","racecar","amit","nope",""bob]
#{"madam":"yes",reaccar:"yes","amit":"No"}

names = ["madam","racecar","amit","nope","bob"]
palindromes = {i: "yes" if i == i[::-1] else "No" for i in names}
print(palindromes)

numbers =[121,222,34,56,789,111,90,434]

palindromes = {i: "yes" if str(i) == str(i)[::-1] else "No" for i in numbers}
print(palindromes)


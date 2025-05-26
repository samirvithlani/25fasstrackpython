
# numbers = {i  for i in range(1,11)}
# print(numbers)


data =["bob","ram","racecar","parth","naman"]

palindromes = {i for i in data if i == i[::-1]}
print(palindromes)

cities = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda"]
#{'a',s,r,b}

citiesint = {i[0] for i in cities}
print(citiesint)

cities = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda","baroda","rajkot"]

cities1 = {i.lower() for i in cities}
print(cities1)


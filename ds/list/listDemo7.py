'''

please entrt y for continue and 'n' for exit
y

enter movie name:
enter relese year:


please entrt y for continue and 'n' for exit
y


enter movie name:
enter relese year:

please entrt y for continue and 'n' for exit
n

[["chava",2025],["abc",2050],[]]

iteration :

for i,j in mopves:

'''

movieData =[]
while True:
    
    choice = input("press y for contiune and n for exit")
    if choice == "y":
        movieName = input("enter movie name :")
        releseYear = int(input("enter relese year"))
        movieData.append([movieName,releseYear])
    elif choice=="n":
        break
    else:
        print("invalid choice")    
        break

print(movieData)    
        


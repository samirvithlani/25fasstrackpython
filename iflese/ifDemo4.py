#condition ---> condtion -->

age = int(input("please enter age : "))

if age>=18:
    print("you are eligible for driving..")
    if age>=21:
        print("you are eligible for marrige..")
    else:
        print("you are not eligible for marrige..")    
else:
    print("you are not eligible for driving..") 
    if age>=16:
        print("you can drive EV")   
    else:
        print("stay at home...")    
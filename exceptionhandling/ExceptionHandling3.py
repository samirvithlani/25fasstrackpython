try:
    no1 = int(input("enter no 1 :"))
    no2 = int(input("enter no 2 :"))
    ans = no1/no2
    print(f"ans = {ans}")


except Exception as e:
    print(f"{e}")    
    #print(f"Cannot divide by zero")
    
except ZeroDivisionError as e:
    #print(f"{e}")    
    print(f"Cannot divide by zero")
except ValueError as e:
    print(f"value erorr cls{e}")    


#string array :

#"ram" 3 4 5 6
#name
#name[6]

name= "ram"
try:
    print(name[4])
except IndexError as e:
    print(f"{e}")    
try:
    no1 = int(input("enter no 1 :"))
    no2 = int(input("enter no 2 :"))
    ans = no1/no2
    print(f"ans = {ans}")
    
except ZeroDivisionError as e:
    #print(f"{e}")    
    print(f"Cannot divide by zero")
except ValueError as e:
    print(f"{e}")    
except Exception as e:
    print(f"{e}")    
    #print(f"Cannot divide by zero")
age = int(input("enter age : "))

try:
    if age<18:
        raise ValueError("age should be grt 18")
    else:
        print("age is not valid..c")
except ValueError as e:
    print(f"{e}")        

    
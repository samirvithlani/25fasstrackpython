try:
    age = int(input("enter age"))
except Exception as e:
    print(f"{e}")    
else:
    print(f"age= {age}")   
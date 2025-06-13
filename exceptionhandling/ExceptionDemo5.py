name = "amit "

try:
    if " " in name:
        raise ValueError("space must not be there iin str...")
    else:
        print(f"{name}")    
except ValueError as e:
    print(f"{e}")    
class InvalidAgeException(Exception):
    def __init__(self, message): #param message
        super().__init__(message) #



name = input("enter name")        

try:
    if " "in name:
        raise InvalidAgeException(" space is there in str...")
    else:
        print(f"{name}")
except InvalidAgeException as e:
    print(f"{e}")        
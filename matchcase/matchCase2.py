day = input("enter a day :")

match day:
    case "Mon" | "Monday" | "mon" | "monday":
        print("you have selected monday")
    case "Sun":
        print("you have selected sunday")    
    case _:
        print("no day avaiable go to mars")    
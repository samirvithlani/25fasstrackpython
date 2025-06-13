try:
    age = int(input("etner age "))
    print(f"age = {age}")
    #40 files.. open...
    #41...... path exce .. direct except
    #closing... all.......
except ValueError as e:
    print("error",e)    
#it will exceute compulsary    
finally:
    print("finally....") 
    #close... if file open...
    #transaction managment..  


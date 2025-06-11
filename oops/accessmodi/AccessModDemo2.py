class User:
    
    def __userData(self):
        print("user Data function called..")

    def get(self):
        self.__userData()


u = User()
#u.__userData()        
u.get()
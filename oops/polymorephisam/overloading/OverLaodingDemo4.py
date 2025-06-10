class Bird:
    
    def fly(self):
        print("bird is flying....")


class Airplane:
    
    def fly(self):
        print("airplane is flying...")



def lets_fly(thing):
    thing.fly()

lets_fly(Airplane())            
lets_fly(Bird())

        
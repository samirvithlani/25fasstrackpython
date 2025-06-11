#ABC abstract base class
from abc import ABC,abstractmethod #ABC class , abstractmethod

#ABSTRCAT CLASS
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(slef):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def test(self):
        print("test....")

class Car(Vehicle):
    
    def start_engine(slef):
        print("car engine starts...")    
     
    def stop_engine(self):
        print("car stop engine ...")    

audi = Car()
audi.start_engine()   
audi.test()     
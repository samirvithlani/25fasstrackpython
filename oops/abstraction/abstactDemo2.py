#ABC abstract base class
from abc import ABC,abstractmethod #ABC class , abstractmethod

#ABSTRCAT CLASS
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(slef):
        pass
    
    def test(self):
        print("test....")



v = Vehicle()
v.start_engine()
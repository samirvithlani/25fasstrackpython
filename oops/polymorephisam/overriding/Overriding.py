class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 10*10


class Rectangle(Shape):
    def area(self):
        return 10 *5


shapes =[Circle(),Rectangle()]
for s in shapes:
    print(s.area())        
        
class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __eq__(self, other):
        return self.marks == other.marks

    


s1 = Student("abc",24)    
s2 = Student("abc",23)

print(s1==s2) #ol __eq__
            
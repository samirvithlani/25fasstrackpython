class Student:
    
    collageName = "GUJARAT UNI" #class level variable...
    
    def getStudentName(self,name):
        #name = local bariable...
        #self.name = instance variable.
        self.name = name
        #pass



stu = Student()      
stu.getStudentName("RAM")
print(f"Collage name = {stu.collageName} student name  = {stu.name}")

        
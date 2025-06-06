class Demo:
    
    x=100 #class level variable..
    print("x",x)
    
    def test(self):
        a = 1000 #local variable...
        print("hello this is test function...")
         # print(self)
        print(f"value of x = {self.x}")
        print(f"value of x = {Demo.x}")
        print(f"valud of a = {a}")
        #print(f"valud of x = {x}")
        self.name = "ROYAL"
        
    def myTest(self):
        #print(f"value of a = {self.a}") error
        print(f"valud of name = {self.name}")

    

#object creation class    
d = Demo() #[room 1]
d.test() #d.test(d) d.test(object)
#print(d)
print(f"value of x = {d.x}")
d.myTest()
print(d.name)

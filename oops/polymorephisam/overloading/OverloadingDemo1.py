class Demo:
    def test(self,a):
        print("test with one arg called...",a)    

    def test(self):
        print("test without arg called...")

d = Demo()
d.test()        
        
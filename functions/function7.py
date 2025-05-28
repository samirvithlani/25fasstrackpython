def demo(*args,**kwargs):
    print(args)
    print(kwargs)


demo(10,True,"ok",name="java",price=1000) 



x =100 #int

t1 = type(x).__name__
print(t1)
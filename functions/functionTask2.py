# def group_by_type(*args):
#     data={'int':[],'float':[],'bool':[],'str':[]}
#     for i in args:
#         t = type(i).__name__
#         data[t].append(i)
    
#     return data    

def group_by_type(*args):
    return {t:[i for i in args if type(i).__name__ == t] for t in set(type(arg).__name__ for arg in args)}

print(group_by_type(10,20,"Java","ajay",20.30,"amit",False,30.40)    )
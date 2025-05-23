marksheets ={"std1":{"maths":29,"sci":28,"drawing":30},"std2":{"maths":28,"sci":28,"drawing":31}}
print(marksheets)

for i,j in marksheets.items():
    print(i) #std,dt2 , j dict
    for sub,marks in j.items():
        print(f"sub = {sub} marks = {marks}")
    
    print()    
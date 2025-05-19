data = ["ram","shyam","amit","venugopaliyyer","kunal","ajay"]
print(data)
#data.reverse()
#data.sort()
#data.sort(reverse=True) #desc
#data.sort(key=len) #length data...
data.sort(key=len,reverse=True) #length data...
print(data)


marks = [90,76,87,77,92,66]
print(marks)
marks.sort(reverse=True)
print(marks)

marks.clear()
print(marks)
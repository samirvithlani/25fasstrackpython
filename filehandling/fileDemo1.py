# file udf object
# relative path , absolute path
#D:\royal\25fasttrackpython\filehandling/fileDemo1.py
#./fileDemo1.py
#parent dir ../
#parent dir ../../

#file = open("demo1.txt","w")
# file = open("./filehandling/demo1.txt","w")
# file.write("Hello this is first file from prog....")
# file.close()

with open("./filehandling/demo2.txt","w") as file:
    file.write("Hello this is with...")

#reopen...
#file.write("ok")   ValueError: I/O operation on closed file.  
    
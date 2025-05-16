data = "hi this is malayalam in india #india #malayalam1"
current_word =""
longest_word = ""
current_len =0
longest_len =0


#1sttime  loop ch h
#datah i
for ch in data + " ": #hi this
    print(ch,end="")
    if ch!= " ": #true
        current_word+=ch  #is
        current_len+=1   #2
    else:#
        if(current_len>longest_len): #2>4
            longest_len = current_len #4
            longest_word = current_word  #malayalam1
        current_word=""    ""
        current_len=0     #0

print("longest word = ",longest_word)        
print(data)
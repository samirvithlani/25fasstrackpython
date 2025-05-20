# #comprehension
# data =[]

# for i in range(1,11):
#     data.append(i)
    

# print(data)    
#[i append ->data for i in range(1,11)return ]
data =[i for i in range(1,11)]
print(data)

#[1,4,9,16,25]

x = [i**2 for i in range(1,6)]
print(x)

#if part..
marks = [21,22,21,19,24,25,25,23]
marks2=[i for i in marks if i >=23]

# for i in marks:
#     if i>=23:
#         marks2.append(i)

print(marks2)        



lang = ["gujarati","hindi","english","martahi","malyalam"]
lang1 = [i for i in lang if len(i)>6]
print(lang1)




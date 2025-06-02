def get_users(batch_size=10):
    total_users = 100
    for i in range(0,total_users,batch_size): 
        #i =0
        #i =100
        
        batch=[] # 
        for j in range(i,min(i+batch_size,total_users)):    
            batch.append(f"user{j}")
        yield batch

for b in get_users():
    print(b)            
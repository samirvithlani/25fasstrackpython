firstName = ["ram","shyam","amit"]
lastName = ["sharma","prashad","patel"]

#["ram sharma","shyam ..."]

#fullName  = [f"{f} {l}" for f in firstName for l in lastName] zip
fullName = [f"{firstName[i]} {lastName[i]}"for i in range(len(firstName))]
print(fullName)
with open("./filehandling/advbadge.jpg","rb") as file:
    image_data = file.read()

with open("./filehandling/advbadgecopy.jpg","wb") as file1:
    file1.write(image_data)
    
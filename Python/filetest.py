




file_path = "test.txt"

file = open(file_path, "w+") 
file.write("abcde")
file.seek(0)  
first_five_characters = file.read(5)
print("First five characters:", first_five_characters)


file.seek(0)  
total_characters = len(file.read())
print("Total number of characters in the file:", total_characters)
file.close()  

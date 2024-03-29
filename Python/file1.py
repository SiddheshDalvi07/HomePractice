import os
isfile=os.path.isfile("example.txt")
print(isfile)

count = 0
file = open("example.txt","r")
for line in file:
    words=line.split(" ")
    count+=len(words)
file2=open("result.txt", "w")
file2.write("The number of words present in given file is " +str(count))
file.close()
file2.close()
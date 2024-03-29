#file handling in python

#opening a file for reading and writing
#if file is not present it will give error
#open will return file object
#"r" stands for read mode

f = open("example.txt", "r")   
print(f.read())
print(f.read(5))


#"w" is only write mode
#if the file is not present then it will create the file
#write mode will overwrite the file
f = open("example34.txt","w")
f.write("Hello World!")  

f = open("example34.txt", "r")
print(f.read())

f.close()   #closing the file

#"a" is append mode
#it will append the content at the end of the file
#if the file is not present then it will create the file

f = open("example.txt", "a")
f.write("\nI am appending some text.")  

f = open("example.txt", "r")
print(f.read())
f.close()

f = open("example2.txt", "a")
f.write("\nI am creating new file and appending some text.")  

f = open("example2.txt", "r")
print(f.read())

f.close()

#x mode 
#if the file is not present then it will create the file
# if the file is already present then it will raise an error

# f =  open("example3.txt", "x")
# f.write("This is a new file.")
# f.close()

#delete mode
import os 
# os.remove("example2.txt")

if  os.path.exists("example4.txt"):
    os.remove( "example4.txt")
else:
    print ("The file does not exist.")

if os.path.isfile('example4.txt'):
    print ("File exists")
else:
    print ("File does not exist")

"""

dictionary
if else 
for loop
functions

revise for django 


"""


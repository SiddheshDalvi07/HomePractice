# file = open("F:/coding practice/HomePractice/Python/example.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())
# file.close()

file = open("F:/coding practice/HomePractice/Python/example.txt","r")
print("current position :",file.tell())

#reposition pointer
print(file.seek(0,0))  #set to the beginning of the file (whence=0)
# print("after seek: current position :",file.tell())

print(file.seek(2,0))    #set to current poistion of the file (whence=1)
print(file.read(10))
file.close()

import os
fname="example2.txt"
print(fname)
print(os.path.abspath(fname))   #get absolute path of a filename

baseDir = os.path.dirname(os.path.abspath(__file__))     #get base directory of python script
print(baseDir)

templateDir = os.path.join(baseDir,"templates") 
print(templateDir)


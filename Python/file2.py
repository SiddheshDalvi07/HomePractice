file = open("example.txt","r")
print(file.read())
# lines = file.readlines() # read all lines in the file and store them as a list of strings
# print(lines) 
file.close()

file = open("F:/coding practice/HomePractice/Python/example.txt", 'w+') # create or overwrite the file named example.txt
file.write('Hello World! \n')
file.write('This is Python programming language.\n')
print(file.read())
file.close()

# file = open("F:/coding practice/HomePractice/Python/example.txt", 'x')

file = open("F:/coding practice/HomePractice/Python/example.txt", 'a')
file.write('\nAppending some text to the existing content.')
file.close()

file = open("F:/coding practice/HomePractice/Python/example.txt", 'rt')
print(file.read())
file.close()

file = open("F:/coding practice/HomePractice/Python/example.txt", 'rb')
print(file.read())
file.close()




# name="siddhesh"
# last='dalvi'
# print(name, last)
# print(f"{name} {last}")
# print("name={} last={}".format(name, last))

#multiline string
# multi="""sididsi    
# sdsds
# sds
# ds"""
# print(multi[1:10])

#string functions
s="hello wo rld"
print(s.__len__()) # returns the length
print(len(s)) # returns the length
print(s[len(s)-1])   #returns the last character of the string
print(s.find('o'))   #returns the first occurrence of 'o', -1 if not found in index format
print(s.count('l'))   # returns number of times 'l' occurs in the string 
print(s.upper()) #uppercase
print(s.lower()) #lowercase
print(s.replace('o', '*')) #replace  all o with *
print(s.split()) #convert to a list
print(s[2])  #indexing
print(s[2:8]) #slicing string_name[start:end:step] step default value is 1
print("swapcase : ",s.swapcase())  #swaps case of alphabets
print("title : ",s.title())     #capitalize first letter of each word
print("strip : ",s.strip()) 
#ss=multi.split()  # Return a list of the substrings in the string, using sep as the separator string.
# print(ss)
# print(ss.pop(2))
# print(ss)

s="Itvedant"
print("Index -  Character")
for i in range(0,len(s),1):
      print(i,"      -     ",s[i])

s1="Itvedant"
print("Character")
for x in s1:    
      print(x)




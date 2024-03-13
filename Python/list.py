list23=[1,2,-1,2.2,3,4,5,6,4,3,2,34,2,2]
print(list23)

list2=["apple","2",2,23,"ball"]
print(list2)

#accessing elements in the list23 by index  
element = list23[0]  #accessing first element of the list23
print("The first element is: ",element)

index = 3         #accessing fourth element of the list23
element = list2[index]
print("The fourth element is: ",element)

list23.append(4)    #adding an element to the end of the list23
print(list23)

list23.insert(1,5)   #inserting an element at a specific position
                   #the number before that position will shift one place forward
print(list23)       #and so now the second element becomes 5 and the third element becomes 6

del list23[1]        #deleting an element from the list23
print(list23)

list23.remove(2)     #removing an element with a specific value
                   #it removes only the first occurrence it encounters
print(list23)

list23.sort()        #sorts all the elements in ascending order
print(list23)

list23.reverse()    #reverses the entire list23
print(list23)

list2.remove(u"ball") #removes unicode string from the list23
print(list2)

list23.count(3)      #returns the count of how many times a particular value occurs in the list23
print(list23.count(3))

print(list23.clear( )); #this function clears the complete list23
                      #but if you try to print

list1=[1,2,-1,2.2,3,2,34,2,2,3,4]
print(list1)


list1.sort()
print(list1)

list1.sort(reverse=True)#sorts the list23 in descending
print(list1)             #order i.e., from highest to lowest or largest to smallest.

list1.extend([9,8])     #adds the elements of one list23 to another
print(list1)

list1.extend([2,3,4,5.6,45])
print(list1)

list1.pop(0)            #pops out the element at the given index
                       #if no index is provided then it pops out the last element
                       #If we provide -1 as  the index then it will remove the last element
print(list1)


list1.reverse()
print(list1)           #it reverses the list23

# del list1     # del keyword can be used to delete an entire list23 but not individual elements of the list23.
# print(list1) 

numbers=[10,20,40,30]
print("sum= ", sum(numbers))   # returns the sum of all values present inside the list23

print("max =", max(numbers))    # returns the maximum value present inside the list23

print("min =", min(numbers))    # returns the minimum value present inside the list23

print("Avg = ", (sum(numbers)//len(numbers))) #returns the average of numbers by dividing the sum with length of the list23


numbers.index(40)        #returns the first occurrence of the specified value
print(numbers.index(40))    # If the value is not found in the list23 then it raises a ValueError exception

lst1 = [1, 2, 3]
lst2 = [1, 20, 30]
print( lst1 > lst2 )

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3 )

numbers=[5,10,15,20,25]
product=1
for num in numbers:
    product *= num
print("Product of {} is {}".format(numbers,product))



squared = [ x**2 for x in range(1, 51) if x % 2 == 0 ]
print(squared)

squared1 = []
for x in range(1,51):
    if x % 2 == 0:
        squared1.append(x**2)
print(squared1)


names=["John","Alice","Bob"]
print(names)

# names=[name.upper() for name in names]
# print(names)

# for i in range(len(names)):
#     names[i] = names[i].upper()
# print(names)

str1 = "Hello, World!"
list1 = list(str1)
print(list1)

for name in names:
    print(name.upper())
 
num1 = [1,2,3,4,5]

for i in range(len(num1)):
    num1[i] += 100
print(num1)

print([i+100 for i in range(1,len(num1)+1,1)])

num2 = [i+100 for i in num1]
print(num2)


# Python program to demonstrate printing 
# of complete multidimensional list row 
# by row. 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
for record in a: 
    print(record) 

   
# Python program to demonstrate that we 
# can access multidimensional list using 
# square brackets 
a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  
          
for i in range(len(a)) :  
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()

for row in a:
    print(*row) # * operator is used to unpack the elements of the iterable (here it's a row from 'a') into positional

'''This code uses Python's built-in print function with the unpacking operator (*) to print each row of the list on a separate line. It's more readable and concise than the original code.'''



l=[10,20,[15,25,35],40]
print(l)
print(l[2])
print(l[2][1])

#multidimensional list
a = [ [2, 4, 6, 8 ],  
    [ 1, 3, 5, 7 ],  
    [ 8, 6, 4, 2 ],  
    [ 7, 5, 3, 1 ] ]  

print(a[1][3]) #  a[row][column]  row =  list as a index ,column = index of an element inside the list 

print(a[2][1])



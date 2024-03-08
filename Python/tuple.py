t1=(1,2,3,4,5)
print(t1)
print(type(t1))

#range
t2= tuple(range(1,20))
print(t2)
print(type(t2))

#empty_tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

#without bracket
x=10,"a",10.5
print(x)
print(type(x))

#single element
t4=(10,)
print(t4)
print(type(t4))

#single element without comma is int class
t4= (10)
print(t4)
print(type(t4))

#length of a tuple
t=(10,20,"Itvedant",67.8)
print(t)
n=len(t)
print("Total number of elements:",n)

#accessing the elements using indexing
print(t[2])
print(t[1])
print(t[-3])

#slicing
t=(10,20,"Itvedant",67.8,80,9000,"Tuple")
sub_t=t[1:4:1]
print("Original tuple:",t)
print("sub tuple after slicing:",sub_t)

#count
t=(10,20,20,10,30,90,10)
n=t.count(10)
print('Number of times elements 10 occurs:',n)

#index
t=(20,20,10,30,90,10)
i=t.index(10)
print("Index of first occurrence 10 is:",i)

#delete tuple
t=(20,20,10,30,90,10)
print(t)
del t
# print(t) # This will generate error as trying to print deleted tuple -undefined


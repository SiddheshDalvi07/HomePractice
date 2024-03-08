myset={10,20,30}
print((myset),type(myset))

#Using set constructor
s1=set(range(1,5))
print(s1,type(s1))

#If you try to make a set with more than once element the same, python will drop the identical values
ident_set = {"blue", "orange", "red", "orange", "orange", "blue"}
print(ident_set)

s2={1,4,2,5,7,8,9.10,55,50,70,80,10,50,10,30,"abc","abcdef"}
print(s2)

s2.add(777)
print("add : ",s2)

s2.update(('a','b','c'))
print("update : ",s2)

s2.pop()
print("pop :" ,s2)

#Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
s2.remove("abc")
print("remove : ",s2)

#Remove an element from a set if it is a member. Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.      
s2.discard("abcde")
print("discard: ",s2)
      
s2.clear()
print(s2)

s1={10,20,30,40}
s2={30,40,50,60}

#union means i.e. all elements that are in either set.
result=s1.union(s2)
result=s1|s2
print(result)

#The intersection means i.e. all elements that are in both sets.
r1=s1.intersection(s2)
r1=s1&s2
print(r1)


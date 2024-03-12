#dictionary is a collection of key pair values

d= {
    "name": "Dennis",
    "age": 30,
    "city": "New York"
}

print(d)
print(d["name"])

#add values in dict
d["email"]= "dennis@gmail.com"
print(d)

#update values in dict
d["age"] = 45
print(d)

#remove value from dictionary using del keyword
del d["city"]
print(d)

product1={
    "Name":"Laptop",
    "Price":5000,
    "Brand":"HP",
    "Warranty":2
}
print(product1)

# del product1["Warranty"], product1["Price"]
# print(product1)

#it will print the Key
for i in product1:
    print(i)

#it will print the value
    for i in product1.values():
        print(i)
        
#It will print both key and Value
for i,j in product1.items():
    # print(f"{i}:{j}")
    print(i,":",j)


d1 = {"s1":"v1","s2":"v2"}
d2 = {"name": "Dennis", "age":36 }

#copy one dict to another
d3 = {**d1, **d2}
print(d3)

#merge two dict to another with constructor
d3=dict(d1,**d2)
print(d3)


d7=dict({"name":"sid", "age":4})
print(d7,type(d7))


empty = {}
print(empty)


d7.pop("name")
print(d7)

d8= dict(((2,'a'), (5,'b')))  #using tuple as a parameter
print(d8)

d8.popitem()
print(d8)


































dd1={"name":"siddhesh","age":24,"city":"Mumbai"}
print(dd1,type(dd1))

dd2=dict((('a',1),('b',2),('c',3)))
print(dd2)

dd3={}
print(type(dd3))

employee={"name":"siddhesh","ANTI":"AVAST","age":30, "salary":50000}
print("Employee Name: ", employee["name"])

dd4={101:'John', 102:'Alice', 103:'Bob', 104: 'Charlie'}

value = dd4.setdefault(103,'Bobby')
print(value)

x = dd4.setdefault(105,'Bobby')
print(x)

x2 = dd4.setdefault(106)  #if value not assigned then it will give output as None
print(x2)

dd4.clear()
print(dd4)

dd4 = employee.copy()
print(dd4)

dd4 = {**employee}   #unpacking the dictionary into a new dictionary
print(dd4)

a = [1,2,3] #keys
b= ["siddhesh","dalvi"] #values

print(dict.fromkeys(a,b)) #from keys of one list with values from another list with pair

dd4.items()
print(dd4)

dd4.get(101,"Not Found")
#print(dd4[101])    #will raise error if key is not found in dict

key = "village"
val = employee.get(key,"Village not found")
print(f"{key}: {val}")

key = "city"
val = employee.get(key, "City Not Found")
print(f"{key}: {val}")

age = employee.get("age")
print("Age: {}".format(age))    

print(employee.get("name"))

print(employee.pop("age"))       #removes and returns the value of given key
print(employee)                              #If Key not present gives KeyError

print(employee.popitem()) #REMOVE LAST  ITEM AND RETURN IT AS DICTITEM  (KEY , VALUE)
print(employee)

employee.update({"gender":"male"})
print(employee)

print(employee.values())
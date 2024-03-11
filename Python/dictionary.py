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


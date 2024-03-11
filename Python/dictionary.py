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




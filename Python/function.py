def hello():
    print("hello world")

hello()


def name(name):
    print("hello", name)

name("siddhesh")


def add(a,b):
    print(a+b)

add(3,4)

#DEFAULT VALUE
def country(country="India"):
    print("I am from ", country)

country()
country("USA")

def mul(a,b):
    return a*b

m=mul(2,3)
print(m,type(m))

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return  sum,sub,mul,div

print(calc(10,5),type(calc))  
print(type(calc(10,5)))  


def student(name,age):
    print("Name :",name,"\nAge:",age)

student("Sid",26)


def sum(*args):
    for i in args:
        print(i)

sum(1,2,3,4,5,6,76,7,8)


def sum1(*args):
    s=0
    for i in args:
        s+=i
    print(s)

sum1(10,20,30,40,50,60)


def mul1(*args):
    m=1
    for i in args:
        m*=i
    print(m)

mul1(10,20,30)

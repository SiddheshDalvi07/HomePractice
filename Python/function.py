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

#unpacking opertor can take mulitple argument
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

#postional argument
#position of the argument is important
def func(a,b):
    print(a,b)

func(10,30)

#keyword argument
#position of the argument is not important
def func1(a,b):
    print(a,b)

func1(a=10, b=30)

#default argument value
#if we don't pass any value to this argument then it will take default value 

def func2(a,b=10):
    print(a,b)

func2(20)

#variable length argument
#we can use * before the name of the variable

def func3(*args):
    s=0
    for i in args:
        s+=i
    return s

func3(20,34,54,6576,75,45)

#global varible
#it is a variable which belongs to the script and not function.
g_var = "I am global"
print(g_var)



#local variable
#a variable declared inside the function is called local variable

def func5():
    b=20
    print(b)

func5()

def max_num(a,b):
    if a>b:
        return a
    else:
        return b
    
print(max_num(20,40))


unique_list = set((1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4))
print((unique_list)) #number of unique elements in list
                             #set() will remove duplicates from the list


def unique_list(l):
    new_list= []
    for i in l:
        if i not in new_list:
            new_list.append(i) 
    return  new_list

print(unique_list([1,2,3,1,2,3,4,5,3,3,3,3,4,5,4,6,]))



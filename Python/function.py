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
print("add",calc(10,5)[0])
print("sub",calc(10,5)[1])
print("mul",calc(10,5)[2])
print("div",calc(10,5)[3])


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

func1(b=10, a=30)

#default argument value
#if we don't pass any value to this argument then it will take default value 

def func2(a,b=10):
    print(a,b)

func2(20)

#arbitrary argument
#variable length argument
#we can use * before the name of the variable
#arbitrary positional arguments (*args):

def func3(*args):
    s=0
    for i in args:
        s+=i
    return s

func3(5,6,7,8,9)

#arbitrary keyword arguments (**kwargs)
def percentage(**kwargs):

    sum = 0

    for sub in kwargs:

        # get argument name

        sub_name = sub

        # get argument value

        sub_marks = kwargs[sub]

        print(sub_name, "=", sub_marks)

        _ = dict(kwargs)

    print(_)

# pass multiple keyword arguments

percentage(math=56, english=61, science=73)



#global varible
#it is a variable which belongs to the script and not function.
g_var = "I am global"
def func4():
    print(g_var,"inside function")

func4()


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


unique_list = list(set((1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4)))
print((unique_list)) #number of unique elements in list
                             #set() will remove duplicates from the list


def unique_list(l):
    new_list= []
    for i in l:
        if i not in new_list:
            new_list.append(i) 
    return  new_list

print(unique_list([1,2,3,1,2,3,4,5,3,3,3,3,4,5,4,6,]))

def unq_list(l):
    return list(set(l))

print(unq_list([1,2,3,1,2,3,4,5,"python","java"]))   #it will add all the non-duplicate element to the list

#lambda function
#lambda function is small anonymous function 
#it can take any number of arguments but can only have one expression

add = lambda x , y :x + y
print(add(5,7))

x = lambda a:a+10
y = lambda a:a-10
print(x(8),y(8))

my_list=[1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x:(x%2==0),my_list))
print(new_list)

#Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
my_list1=[1,2,3,4,5,6,7,8,9,10]
new_list1 = list(filter(lambda x:(x%3==0),my_list1))
print(new_list1)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

print(new_list)



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in my_list if x % 2 == 0]
print(new_list)


my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    uppered_pets.append(pet.upper())

print(uppered_pets)


#map function Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)




#reduce funtion -- Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)


lis = [1, 3, 5, 6, 2] 
  
# using reduce to compute sum of list 
print("The sum of the list elements is : ", end="") 
print(reduce(lambda a,b: a+b, lis)) 


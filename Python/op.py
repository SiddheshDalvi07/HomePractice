"""Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because '+' operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. """


a = 10
b = 10
print(a+b)
print(type(a))
print(int.__add__(a,b))  # int.__add__ is same as a+b
# print(float.__add__(a, b))   # TypeError: can't convert type 'float' to 'int'

s1 = "hello"
s2 = "world"
print(s1 + s2)
print(str.__add__(s1, s2))    # str.__add__ is the method that does string concatenation is same as s1 + s2  

#operator overloading means changing the behaviour of the operator
#we can use this operator with objects

class Student:
    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2
    
    def __add__(self,other):
        marks1 = self.marks1  + other.marks1
        marks2 = self.marks2  + other.marks2
        s3 = Student(marks1,marks2)
        return s3

s1 = Student(85,96)
s2 = Student(74,89)

s3 = s1 + s2
print(s3.marks1)
print(s3.marks2)


class Student:
    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2
    
    def __sub__(self,other):
        marks1 = self.marks1  - other.marks1
        marks2 = self.marks2  - other.marks2
        s3 = Student(marks1,marks2)
        return s3

s1 = Student(85,96)
s2 = Student(74,89)

s3 = s1 - s2
print(s3.marks1)
print(s3.marks2)